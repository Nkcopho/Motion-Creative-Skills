from pathlib import Path
import cv2,numpy as np
cv2.setNumThreads(2)
p=str(Path(__file__).resolve().parents[2] / '08_SOURCE/reference.mp4');c=cv2.VideoCapture(p);c.set(1,165);frames={}
for f in range(165,242):
 ok,a=c.read();frames[f]=a
sift=cv2.SIFT_create(nfeatures=1800);bf=cv2.BFMatcher();ref=cv2.resize(cv2.cvtColor(frames[213],cv2.COLOR_BGR2GRAY),(664,372));mask=np.full(ref.shape,255,np.uint8);mask[245:,:]=0;mask[130:240,230:525]=0
k,d=sift.detectAndCompute(ref,mask);result=[];rois=[(637,610,673,647),(677,612,707,644),(718,616,742,640),(757,617,777,638),(795,619,812,636)];
for f,a in frames.items():
 gray=cv2.resize(cv2.cvtColor(a,cv2.COLOR_BGR2GRAY),(664,372));k2,d2=sift.detectAndCompute(gray,None);good=[m for m,n in bf.knnMatch(d2,d,k=2) if m.distance<.76*n.distance];x=np.float32([k2[m.queryIdx].pt for m in good]);y=np.float32([k[m.trainIdx].pt for m in good]);M,ind=cv2.estimateAffinePartial2D(x,y,method=cv2.RANSAC,ransacReprojThreshold=1.5);sel=ind.ravel().astype(bool);err=np.linalg.norm(x[sel]@M[:,:2].T+M[:,2]-y[sel],axis=1);M[:,2]*=2; aligned=cv2.warpAffine(a,M,(1328,744));hsv=cv2.cvtColor(aligned,cv2.COLOR_BGR2HSV);ms=cv2.inRange(hsv,(86,90,50),(135,255,255));areas=[int(cv2.countNonZero(ms[y:y2,x:x2])) for x,y,x2,y2 in rois];result.append([f,sel.sum(),round(np.median(err)*2,2),*areas]);
r=np.array(result);refareas=r[r[:,0]==213,3:][0];print('refareas',refareas);print('f inlier err, relative counts');
for row in r[::3]:print(int(row[0]),int(row[1]),row[2],np.round(row[3:]/refareas,2))
for i in range(5):
 for thr in [.1,.5,.9]:
  eligible=[int(row[0]) for j,row in enumerate(r) if j+2<len(r) and np.all(r[j:j+3,3+i]/refareas[i]>=thr)]; print('avatar',i+1,'threshold',thr,'first',min(eligible) if eligible else None)
