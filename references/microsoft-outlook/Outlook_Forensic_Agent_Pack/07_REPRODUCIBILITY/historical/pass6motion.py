from pathlib import Path
import cv2 as c,numpy as n
c.setNumThreads(2)
p=str(Path(__file__).resolve().parents[2] / '08_SOURCE/reference.mp4');v=c.VideoCapture(p);v.set(1,165);frames={}
for f in range(165,242):
 ok,a=v.read(); assert ok;frames[f]=a
sift=c.SIFT_create(nfeatures=1800);bf=c.BFMatcher();ref=c.resize(c.cvtColor(frames[213],c.COLOR_BGR2GRAY),(664,372));mask=n.full(ref.shape,255,n.uint8);mask[245:,:]=0;mask[130:240,230:525]=0
k,d=sift.detectAndCompute(ref,mask);ali={}
for f,a in frames.items():
 gray=c.resize(c.cvtColor(a,c.COLOR_BGR2GRAY),(664,372));k2,d2=sift.detectAndCompute(gray,None);good=[m for m,q in bf.knnMatch(d2,d,k=2) if m.distance<.76*q.distance];x=n.float32([k2[m.queryIdx].pt for m in good]);y=n.float32([k[m.trainIdx].pt for m in good]);M,ind=c.estimateAffinePartial2D(x,y,method=c.RANSAC,ransacReprojThreshold=1.5);M[:,2]*=2;ali[f]=c.warpAffine(a,M,(1328,744)).astype(n.int16)
rois={'tray':(307,15,557,195),'holder':(610,130,906,190),'typography':(308,248,470,365),'panels':(495,271,1044,610),'swatches':(250,504,457,680),'avatars':(630,605,815,649),'sphere path':(1090,610,1328,740)}
print('aligned regional change % max RGB channel > 15 per 0.2 s')
print(list(rois))
for f in range(171,238,6):
 a=ali[f];b=ali[f-6];diff=n.max(n.abs(a-b),axis=2); print(f,round(f/30,2),*[round(100*(diff[y:Y,x:X]>15).mean(),1) for x,y,X,Y in rois.values()])
# patch medians compare stable color: RGB euclidean within 24 of reference, only threshold where colour distinguishable from initial
for x,ys in [(294,[514,533,551,570,588,608,628,646,666]),(408,[514,533,551,570,590,607,626,645,664])]:
 print('swatches',x)
 for y in ys:
  colors=n.array([n.median(ali[f][y-3:y+4,x-5:x+6],axis=(0,1)) for f in range(165,242)]);goal=colors[213-165];dist=n.linalg.norm(colors-goal,axis=1);first=next((i+165 for i in range(len(dist)-2) if n.all(dist[i:i+3]<24)),None);print(y,'target rgb',goal[::-1].astype(int),'initial dist',round(dist[0],1),'first stable',first, None if first is None else round(first/30,3))
