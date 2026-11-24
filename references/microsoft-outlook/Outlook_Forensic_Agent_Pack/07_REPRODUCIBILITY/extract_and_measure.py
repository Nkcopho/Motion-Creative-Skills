from pathlib import Path
import csv,cv2,numpy as np,json
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent.parent; E=P/'03_EVIDENCE'; M=P/'04_MEASUREMENTS'; cv2.setNumThreads(2)
def savecsv(path,header,rows):
 with path.open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(header);w.writerows(rows)
ids=set([0,9,15,21,27,30,36,42,45,48,51,53,54,55,60,75,90,105,120,135,150,165,180,195,201,207,210,213,216,222,225,231,240,241,242,243,255,270,285,300,315,330,345,360,375,390,405,420,430,440,450,460,470,480,490,500,510,520,530,540,545,550,560,570,580,581,582,583,584,585,586,588,590,593,600,607,612,624,636,648,660,672,684,696,708,720,732,744,750,756,768,780,792,804,816,828,840,846,855,870,883,885,900,915,930,945,960,975,990,1005,1020,1035,1050,1065,1080,1095,1105,1106,1107,1110,1125,1140,1155,1185,1215,1245,1281,1284,1287,1290,1293,1296,1299,1302,1305,1308,1311,1314,1320,1350,1380,1383,1386,1389,1392,1395,1398,1401,1404,1407,1410,1413,1440,1446,1452,1458,1464,1470,1476,1482,1500,1530,1560,1590,1620,1658,1680,1692,1694,1695,1696,1698,1700,1702,1704,1706,1708,1710,1712,1733,1740,1764,1770,1776,1780,1788,1800,1812,1824,1831,1836,1848,1860,1872,1884,1896,1912])
cap=cv2.VideoCapture(str(P/'08_SOURCE/reference.mp4'));prev=None;data=[];index=[];masters={};i=0
while True:
 ok,f=cap.read()
 if not ok:break
 small=cv2.resize(f,(332,186),interpolation=cv2.INTER_AREA);g=cv2.cvtColor(small,cv2.COLOR_BGR2GRAY);diff=None if prev is None else float(np.mean(cv2.absdiff(g,prev)));eq=None if prev is None else int(np.array_equal(g,prev));blur=cv2.GaussianBlur(g,(3,3),.65);mag=np.hypot(cv2.Sobel(blur,cv2.CV_32F,1,0,ksize=3)/4,cv2.Sobel(blur,cv2.CV_32F,0,1,ksize=3)/4);sat=cv2.cvtColor(small,cv2.COLOR_BGR2HSV)[:,:,1]>=100
 data.append([i,round(i/30,6),None if diff is None else round(diff,6),eq,round(100*(mag>12).mean(),4),round(100*sat.mean(),4),float(np.median(g))]);prev=g
 if i in ids:
  path=E/'frames'/f'F{i:04d}.png';assert cv2.imwrite(str(path),f,[cv2.IMWRITE_PNG_COMPRESSION,1]);index.append([i,round(i/30,6),str(path.relative_to(P)),f.shape[1],f.shape[0]])
 if i in (0,213,540,660,840,1299,1695,1770,1872):masters[i]=f.copy()
 i+=1
cap.release();assert i==1913;assert len(index)==len(ids)
savecsv(E/'frame_index.csv',['frame','seconds','relative_path','width','height'],index);savecsv(M/'fresh_frame_metrics.csv',['frame','seconds','mean_abs_luma_diff_332x186','identical_downsampled_luma','edge_gt12_pct_332x186','hsv_sat_ge100_pct_332x186','median_luma_332x186'],data);savecsv(M/'fresh_transition_peaks.csv',['frame','seconds','mean_abs_luma_difference'],[(a[0],a[1],a[2]) for a in sorted(data[1:],key=lambda a:-a[2])[:40]])
results=[]
with (M/'colour_samples.csv').open() as f:
 for a in csv.DictReader(f):
  frame,x,y=int(a['frame']),int(a['x']),int(a['y']);im=masters[frame];rgb=np.median(im[y-3:y+4,x-3:x+4,::-1],axis=(0,1)).astype(int);old=np.array([int(a['hex'][j:j+2],16) for j in (0,2,4)]);results.append([frame,x,y,a['region'],a['hex'],''.join(f'{v:02X}' for v in rgb),round(float(np.linalg.norm(rgb-old)),3)])
savecsv(M/'fresh_colour_samples.csv',['frame','x','y','region','inherited_hex','fresh_median_7x7_hex','rgb_euclidean_difference'],results)
crops=[('opening_switch',0,(835,300,1105,480)),('light_tray',213,(280,0,580,235)),('light_rails',213,(585,0,1328,150)),('light_typography',213,(295,235,480,375)),('light_contrast',213,(265,380,465,475)),('light_swatches',213,(245,495,460,690)),('light_avatars',213,(625,600,825,655)),('light_unread_and_clips',213,(1085,150,1290,445)),('light_documents',213,(1090,320,1328,625)),('light_sphere',213,(1145,615,1280,744)),('macro_sphere',540,(320,0,490,140)),('macro_white_block_shadow',540,(665,0,875,175)),('macro_cube_cluster',540,(565,495,830,665)),('email_stack',660,(400,0,950,660)),('email_stationery',660,(0,250,340,744)),('inbox_focus',840,(0,0,1328,744)),('reaction_region',1299,(495,350,1030,490)),('task_pointer',1695,(375,285,495,405)),('dark_environment',1770,(0,0,1328,744)),('closing_accent',1872,(1015,225,1120,315))];ci=[]
for name,f,(x,y,X,Y) in crops:
 path=E/'crops'/f'{name}_F{f:04d}.png';cv2.imwrite(str(path),masters[f][y:Y,x:X]);ci.append([name,f,x,y,X,Y,str(path.relative_to(P))])
savecsv(E/'crop_index.csv',['name','frame','left','top','right_exclusive','bottom_exclusive','path'],ci)
for k in range(0,len(index),20):
 batch=index[k:k+20];sheet=Image.new('RGB',(4*332,((len(batch)+3)//4)*210),'#f3f4f6');d=ImageDraw.Draw(sheet)
 for j,(f,t,path,*_) in enumerate(batch):
  img=Image.open(P/path).convert('RGB').resize((332,186),Image.Resampling.LANCZOS);x=(j%4)*332;y=(j//4)*210;sheet.paste(img,(x,y));d.text((x+5,y+190),f'F{f:04d}   {t:.3f}s',fill='#222222')
 sheet.save(E/'contact_sheets'/f'contact_{k//20+1:02d}.jpg',quality=92)
summary={'decoded_frames':i,'exported_frames':len(index),'crops':len(ci),'near_identical_luma_pairs_lt_0.1':sum(a[2]<.1 for a in data[1:]),'exact_identical_downsampled_luma_pairs':sum(a[3] for a in data[1:]),'colour_samples_rechecked':len(results),'max_rgb_distance':max(r[-1] for r in results)};(M/'fresh_audit_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary)
