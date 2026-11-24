from pathlib import Path
import cv2 as c,numpy as np
p=str(Path(__file__).resolve().parents[2] / '08_SOURCE/reference.mp4');cap=c.VideoCapture(p)
F={}
for i in [0,3,6,9,15,30,45,48,51,53,54,55,165,180,195,201,207,210,213,216,222,225,231,240,241,242,243,270,540,660,1105,1106,1107,1769,1770]:
 cap.set(c.CAP_PROP_POS_FRAMES,i);r,f=cap.read();F[i]=f
r=F[213]; gray=lambda a:c.cvtColor(a,c.COLOR_BGR2GRAY);s=c.SIFT_create(nfeatures=3000,contrastThreshold=.008); mask=np.ones(r.shape[:2],np.uint8)*255;mask[580:,:]=0;mask[235:390,290:480]=0;mask[270:580,480:1055]=0
k,d=s.detectAndCompute(gray(r),mask); bf=c.BFMatcher()
for i in [165,180,195,201,207,210,216,225,240]:
 k2,d2=s.detectAndCompute(gray(F[i]),None); m=[a for a,b in bf.knnMatch(d,d2,k=2) if a.distance<.72*b.distance]; a=np.float32([k[x.queryIdx].pt for x in m]);b=np.float32([k2[x.trainIdx].pt for x in m]); M,inl=c.estimateAffinePartial2D(a,b,method=c.RANSAC,ransacReprojThreshold=2.5); ii=inl.ravel().astype(bool); pred=c.transform(a[None],M)[0]; e=np.linalg.norm(pred-b,axis=1); print(i,'matches',len(m),'inliers',sum(ii),'scale',np.linalg.norm(M[:,0]),'rot',np.degrees(np.arctan2(M[1,0],M[0,0])),'center shift', (M@np.array([664,372,1])-np.array([664,372])).round(2),'median err',np.median(e[ii]))
# show montage transition and later frame samples
ids=[0,3,6,9,45,48,51,53,54,55,241,242,243,1105,1106,1107]; out=np.zeros((4*200,4*332,3),np.uint8)
for j,i in enumerate(ids):
 f=c.resize(F[i],(332,186)); y=j//4*200;x=j%4*332;out[y:y+186,x:x+332]=f;c.putText(out,str(i)+' '+str(round(i/30,2)),(x+4,y+197),c.FONT_HERSHEY_SIMPLEX,.35,(255,255,255),1)
c.imwrite(str(Path(__file__).resolve().parents[2]/'03_EVIDENCE/contact_sheets/historical_transition_montage.jpg'),out)
# source sample switch thumbnail colors central housing and thumb
for i in [0,3,6,9,15,30,45,48,51]:
 f=F[i]; print('frame',i,'mean',f.mean(axis=(0,1)).round(1).tolist())
