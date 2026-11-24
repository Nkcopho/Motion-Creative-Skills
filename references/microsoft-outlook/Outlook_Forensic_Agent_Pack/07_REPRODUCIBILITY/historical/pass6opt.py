from pathlib import Path
exec(open(Path(__file__).resolve().parent/'pass6.py').read().split('# compare common')[0])
# fit global affine and projective, compare in-sample residuals; limited manual pts
for model in ['similarity','affine','homography']:
 if model=='similarity':
  # least squares rotation scale translation
  X=n.zeros((2*len(a),4));X[0::2,:]=n.c_[a[:,0],-a[:,1],n.ones(len(a)),n.zeros(len(a))];X[1::2,:]=n.c_[a[:,1],a[:,0],n.zeros(len(a)),n.ones(len(a))];p=n.linalg.lstsq(X,b.ravel(),rcond=None)[0];pred=(X@p).reshape(-1,2)
 elif model=='affine': pred=n.c_[a,n.ones(len(a))]@n.linalg.lstsq(n.c_[a,n.ones(len(a))],b,rcond=None)[0]
 else:
  H,_=c.findHomography(a,b,0);pred=c.perspectiveTransform(a[None].astype(n.float32),H)[0]
 e=n.linalg.norm(b-pred,axis=1);print(model,'RMS',n.sqrt(n.mean(e**2)),'max',e.max(),'median',n.median(e))
# sample direct RGB & luminance
pts={'light disc center':(309,427),'light disc substrate':(285,398),'dark disc center':(419,427),'dark disc substrate':(449,400),'ground left':(365,470),'ground right':(1069,500),'UI panel':(911,399),'white panel left':(521,465),'cyan cavity':(1175,261),'white top unread':(1175,206),'cyan rail':(961,102),'pencil tray white':(750,145),'dark disc light backing':(112,433),'dark light substrate':(81,405),'dark disc dark backing':(238,434),'dark ground':(275,445),'dark UI panel':(855,487)}
def lum(rgb):
 v=rgb/255.; return n.dot(n.where(v<=.04045,v/12.92,((v+.055)/1.055)**2.4),[.2126,.7152,.0722])
for name,(x,y) in pts.items():
 im=D if name in ['dark disc light backing','dark light substrate','dark disc dark backing','dark ground','dark UI panel'] else L
 rgb=n.median(im[y-3:y+4,x-3:x+4],axis=(0,1))[::-1];print(name,tuple(rgb.astype(int)),round(lum(rgb),4))
# sensitivity check with chroma and alternate edge thresholds
for f,im,roi in [(213,L,(495,271,1044,610)),(1770,D,(333,196,1019,565))]:
 mask=n.ones(im.shape[:2],bool);mask[:8]=False;inner=n.zeros_like(mask);x,y,X,Y=roi;inner[y:Y,x:X]=1;outer=mask&~inner
 gr=c.GaussianBlur(c.cvtColor(im,c.COLOR_BGR2GRAY),(3,3),.65);mag=n.hypot(c.Sobel(gr,c.CV_32F,1,0,ksize=3)/4,c.Sobel(gr,c.CV_32F,0,1,ksize=3)/4)
 chroma=im.max(2)-im.min(2)
 print('frame',f)
 for th in [8,12,20]: print('edge',th,*[round(100*(mag[m]>th).mean(),2) for m in [inner,outer]])
 for th in [30,50,80]:print('chroma',th,*[round(100*(chroma[m]>th).mean(),2) for m in [inner,outer]])
