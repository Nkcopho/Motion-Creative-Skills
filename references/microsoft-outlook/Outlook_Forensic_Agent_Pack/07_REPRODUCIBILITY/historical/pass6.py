from pathlib import Path
import cv2 as c,numpy as n
p=str(Path(__file__).resolve().parents[2] / '08_SOURCE/reference.mp4')
v=c.VideoCapture(p)
def frame(f):
 v.set(c.CAP_PROP_POS_FRAMES,f); ok,a=v.read(); assert ok; return a
L=frame(213); D=frame(1770)
# rough manually located landmarks, center coordinates
names=['pencil holder','portrait cyan','portrait green','portrait pink','unread center','isolated clip','document blue','document white','large regular Aa','large bold Aa','disc left','disc right','avatar1','avatar2','avatar3','avatar4','avatar5']
a=n.array([[756,164],[978,188],[1022,158],[1026,201],[1191,234],[1118,414],[1164,517],[1211,563],[433,273],[428,337],[309,427],[419,427],[655,628],[692,628],[730,628],[767,628],[803,628]],float)
b=n.array([[754,102],[1012,134],[1061,101],[1067,150],[1245,195],[1170,401],[1215,521],[1271,575],[260,326],[258,363],[112,433],[238,434],[595,626],[640,626],[687,626],[734,626],[780,626]],float)
# compare common scaling/translation model based on avatar row
for label,ix in [('all',range(len(a))),('avatar row',range(12,17)),('right portraits',range(1,4)),('left samples',range(8,12)),('right objects',range(1,8))]:
 x=a[list(ix)];y=b[list(ix)];xc=x-x.mean(0);yc=y-y.mean(0);s=(xc*yc).sum()/(xc*xc).sum();t=y.mean(0)-s*x.mean(0);err=n.linalg.norm(y-(s*x+t),axis=1);print(label,'scale',s,'translation',t,'rms',n.sqrt(n.mean(err**2)))
 if label=='avatar row':
  print('avatar-based residuals',[(name,tuple(n.round(yx-(s*xx+t),1))) for name,xx,yx in zip(names,a,b)])
# zonal color / edge distributions; same edge threshold for light and dark, no interpretation as saliency
for f,im,roi in [(213,L,(495,271,1044,610)),(1770,D,(333,196,1019,565))]:
 h,w=im.shape[:2]; mask=n.zeros((h,w),bool); mask[8:,:]=1; x0,y0,x1,y1=roi; inner=n.zeros_like(mask);inner[y0:y1,x0:x1]=1; outer=mask&~inner
 hsv=c.cvtColor(im,c.COLOR_BGR2HSV); gray=c.cvtColor(im,c.COLOR_BGR2GRAY); blur=c.GaussianBlur(gray,(3,3),.65); gx=c.Sobel(blur,c.CV_32F,1,0,ksize=3)/4;gy=c.Sobel(blur,c.CV_32F,0,1,ksize=3)/4; mag=n.hypot(gx,gy); sat=hsv[:,:,1]>=100
 print('\nFRAME',f)
 for name,m in [('all',mask),('central',inner),('outer',outer)]:
  print(name,'area',m.sum(),'sat%',100*sat[m].mean(),'edge>12%',100*(mag[m]>12).mean(),'mean edge',mag[m].mean(),'median hsv',n.median(hsv[m],axis=0),'median gray',n.median(gray[m]))
 print('share saturated outside',100*(sat&outer).sum()/(sat&mask).sum())
 # 3x3 tile values saturated + edge
 for yy in n.array_split(n.arange(8,h),3):
  print([(round(100*sat[n.ix_(yy,xx)].mean(),1),round(100*(mag[n.ix_(yy,xx)]>12).mean(),1)) for xx in n.array_split(n.arange(w),3)])
# check state sequence for compositional motion: difference per fixed region / global transform via stable earlier script later
