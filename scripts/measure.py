#!/usr/bin/env python3
"""Generic decoded frame metrics and optional frame extraction; no segmentation or camera solving implied."""
import argparse,csv,hashlib,json,pathlib,cv2,numpy as np
p=argparse.ArgumentParser();p.add_argument('video');p.add_argument('output');p.add_argument('--every',type=int,default=30);a=p.parse_args();assert a.every>0
out=pathlib.Path(a.output);out.mkdir(parents=True,exist_ok=True);frames=out/'frames';frames.mkdir(exist_ok=True);cap=cv2.VideoCapture(a.video);assert cap.isOpened(),'Cannot open source';fps=cap.get(cv2.CAP_PROP_FPS);assert fps>0;prev=None;i=0;near=0
with (out/'metrics.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['frame','nominal_time_s','mean_luma_delta','edge_percent','saturation_percent'])
 while True:
  ok,bgr=cap.read()
  if not ok:break
  gray=cv2.resize(cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY),(332,186),interpolation=cv2.INTER_AREA); delta=None if prev is None else float(cv2.absdiff(gray,prev).mean());near+=int(delta is not None and delta<.1);prev=gray
  blur=cv2.GaussianBlur(gray,(3,3),.65);gx=cv2.Sobel(blur,cv2.CV_32F,1,0,ksize=3)/4;gy=cv2.Sobel(blur,cv2.CV_32F,0,1,ksize=3)/4;edge=float((np.hypot(gx,gy)>12).mean()*100);sat=float((cv2.cvtColor(bgr,cv2.COLOR_BGR2HSV)[:,:,1]>=100).mean()*100)
  w.writerow([i,i/fps,delta,edge,sat]);
  if i%a.every==0:assert cv2.imwrite(str(frames/f'F{i:06d}.png'),bgr)
  i+=1
cap.release(); assert i>0
h=hashlib.sha256();
with open(a.video,'rb') as f:
 for b in iter(lambda:f.read(1048576),b''):h.update(b)
(out/'metadata.json').write_text(json.dumps({'source':str(a.video),'sha256':h.hexdigest(),'decoded_frames':i,'nominal_fps':fps,'near_identical_pairs':near,'method':'332x186 area-resampled grayscale; mean abs difference <0.1; Gaussian 3x3 sigma .65; Sobel /4 magnitude >12; full-frame HSV S>=100. Nominal times may not reflect VFR timestamps. Proxies not optical or gaze metrics.'},indent=2));print(f'Decoded {i} frames')
