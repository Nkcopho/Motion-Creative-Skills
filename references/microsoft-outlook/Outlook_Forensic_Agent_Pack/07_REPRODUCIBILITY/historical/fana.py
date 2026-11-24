from pathlib import Path
import cv2 as c, numpy as np, os
p=str(Path(__file__).resolve().parents[2] / '08_SOURCE/reference.mp4'); cap=c.VideoCapture(p)
frames={}; dif=[]; prev=None
for i in range(1913):
 r,f=cap.read()
 if not r: break
 g=c.resize(f,(332,186),interpolation=c.INTER_AREA); g=c.cvtColor(g,c.COLOR_BGR2GRAY)
 if prev is not None: dif.append((i,float(np.mean(c.absdiff(g,prev)))))
 prev=g
 if i%15==0 or 150<=i<=260 and i%3==0 or i<=60 and i%3==0: frames[i]=f
print('strong frame changes', sorted(dif,key=lambda x:-x[1])[:30]);
# template matching around master stationary regions: local patch no scale correction
ref=frames[213]; gray=lambda f:c.cvtColor(f,c.COLOR_BGR2GRAY)
rois={'type_Aa':(395,249,468,295),'tray':(391,10,551,195),'pencil':(607,129,908,198),'unread':(1100,160,1278,308),'dark_square':(384,391,459,468),'panel_right':(810,320,1046,578),'avatar1':(637,608,675,648),'sphere':(1159,629,1260,726),'paperclips':(1098,310,1185,380),'upper_rail':(750,55,870,90)}
for name,(x,y,X,Y) in rois.items():
 t=gray(ref)[y:Y,x:X]; print(name,end=' ')
 for i in [165,180,195,201,207,210,213,216,222,225,231,240,246,255]:
  a=gray(frames[i]); pad=180 if name=='sphere' else 90; xx=max(0,x-pad); yy=max(0,y-pad); XX=min(1328,X+pad); YY=min(744,Y+pad)
  m=c.matchTemplate(a[yy:YY,xx:XX],t,c.TM_CCOEFF_NORMED); _,v,_,pos=c.minMaxLoc(m); print(f'{i}:{pos[0]+xx-x:+d},{pos[1]+yy-y:+d}/{v:.2f}',end=' ')
 print()
# opening blue region
for i in range(0,61,3):
 f=frames[i]; h=c.cvtColor(f,c.COLOR_BGR2HSV); mask=c.inRange(h,(90,90,60),(130,255,255)); n,l,st,cen=c.connectedComponentsWithStats(mask); j=1+np.argmax(st[1:,4]); print('switch',i,st[j].tolist())
# color area and distribution source master; shadow profile across ground
for name,box in {'ground':(350,460,470,500),'white_panel':(850,365,1010,430),'tray_floor':(316,35,375,175),'sphere':(1164,632,1258,722),'dark_disc':(397,408,442,446),'light_disc':(287,407,330,446)}.items():
 x,y,X,Y=box; rgb=ref[y:Y,x:X,::-1].reshape(-1,3); print('color',name,np.percentile(rgb,[5,50,95],axis=0).round(1).tolist())
