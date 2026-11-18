import json,os,random
from urllib.request import Request,urlopen
from urllib.error import HTTPError
W=[0,100,320,330,500,900,0];PW=[0,0,1,1,2,4,0]
PM="<<<<<<<<DDDDDDDD@@ABBA@@==>AA>==<<=@@=<<<<<>><<<<<<<<<<<<<<<<<<<"
NM="479999747:<<<<:79<>??><99=?@@?=99=?@@?=99<>??><97:<==<:747999974"
BM="8::::::8:=<<<<=::>>>>>>::<>>>><::==>>==::<=>>=<::<<<<<<:8::::::8"
RM="<<=>>=<<>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<=>>=<<"
QM=":;;;;;;:;<<<<<<;;<====<;;<=>>=<;;<=>>=<;;<====<;;<<<<<<;:;;;;;;:"
KM="64422446644224466442244686644668:888888:<<;::;<<@A><<>A@@B><<>B@"
KE=":;<<<<;:;<====<;<=>??>=<<=?@@?=<<=?@@?=<<=?@@?=<<=>??>=<;<====<;:"
def tb(s):
 a=[0]*128
 for i,c in enumerate(s):a[(7-(i>>3))*16+(i&7)]=(ord(c)-60)*5
 return a
MG={1:tb(PM),2:tb(NM),3:tb(BM),4:tb(RM),5:tb(QM),6:tb(KM)}
EG={1:MG[1],2:MG[2],3:MG[3],4:MG[4],5:MG[5],6:tb(KE)}
SQ=[r*16+f for r in range(8)for f in range(8)]
ND=[31,33,14,18,-14,-18,-31,-33];KD=[15,16,17,1,-1,-15,-16,-17]
BD=[15,17,-15,-17];RD=[16,1,-16,-1]
_r=random.Random(987654321)
Z=[[_r.getrandbits(64)for _ in range(128)]for _ in range(15)]
ZS=_r.getrandbits(64);ZC=[_r.getrandbits(64)for _ in range(16)]
CM=[15]*128
for _s,_m in((4,12),(0,13),(7,14),(116,3),(112,7),(119,11)):CM[_s]=_m
B=[0]*128;S=0;C=0;E=-1;H=0;HM=0;KS=[4,116];NP=[0,0]
TT={};KL=[0]*1024;NL=30000;nd=0;PA=set()
class X(Exception):pass
def a(s,by):
 for d in((-15,-17)if by==0 else(15,17)):
  t=s+d
  if not t&0x88 and B[t]==1|by:return 1
 for ds,ts in((ND,(2,)),(KD,(6,)),(BD,(3,5)),(RD,(4,5))):
  for d in ds:
   t=s+d
   while not t&0x88:
    p=B[t]
    if p:
     if p&8==by and(p&7)in ts:return 1
     break
    if ts==(2,)or ts==(6,):break
    t+=d
 return 0
def g():
 ms=[]
 def ap(f,to,last,r):
  if r==last:
   for pr in(5,4,3,2):ms.append(f|to<<7|pr<<14)
  else:ms.append(f|to<<7)
 for f in SQ:
  p=B[f]
  if not p or p&8!=S:continue
  t=p&7
  if t==1:
   d=16 if S==0 else-16;r=f>>4;home=1 if S==0 else 6;last=6 if S==0 else 1;o=f+d
   if not B[o]:
    ap(f,o,last,r)
    if r==home and not B[f+2*d]:ms.append(f|(f+2*d)<<7)
   for dd in(d-1,d+1):
    to=f+dd
    if to&0x88:continue
    q=B[to]
    if q and q&8!=S:ap(f,to,last,r)
    elif to==E:ms.append(f|to<<7)
  elif t==2 or t==6:
   for d in(ND if t==2 else KD):
    to=f+d
    if to&0x88:continue
    q=B[to]
    if not q or q&8!=S:ms.append(f|to<<7)
  else:
   for d in(BD if t==3 else RD if t==4 else KD):
    to=f+d
    while not to&0x88:
     q=B[to]
     if q:
      if q&8!=S:ms.append(f|to<<7)
      break
     ms.append(f|to<<7);to+=d
 for bit,ks,rk,em,th in((1,4,7,(5,6),(4,5,6)),(2,4,0,(1,2,3),(4,3,2)),(4,116,119,(117,118),(116,117,118)),(8,116,112,(113,114,115),(116,115,114))):
  if C&bit and B[ks]==6|S and B[rk]==4|S and not any(B[s]for s in em)and not any(a(s,S^8)for s in th):ms.append(ks|th[2]<<7)
 return ms
UN=[]
def m(mv):
 global S,C,E,H,HM
 if mv==0:
  UN.append((0,0,0,C,E,H,HM));H^=ZS;E=-1;HM+=1;S^=8;return
 f=mv&127;t=(mv>>7)&127;pr=(mv>>14)&7;p=B[f];cap=B[t];cs=t
 if(p&7)==1 and t==E and not cap and(f&7)!=(t&7):cs=t-16 if S==0 else t+16;cap=B[cs]
 UN.append((mv,cap,cs,C,E,H,HM));H^=Z[p][f]^ZC[C]
 if cap:
  H^=Z[cap][cs];B[cs]=0;HM=0
  if(cap&7)!=1:NP[cap>>3]-=1
 elif(p&7)!=1:HM+=1
 else:HM=0
 B[t]=S|pr if pr else p;B[f]=0;H^=Z[B[t]][t]
 if pr:NP[S>>3]+=1
 if(p&7)==6:
  KS[S>>3]=t
  if t-f==2:B[f+1]=B[f+3];B[f+3]=0;H^=Z[B[f+1]][f+3]^Z[B[f+1]][f+1]
  elif f-t==2:B[f-1]=B[f-4];B[f-4]=0;H^=Z[B[f-1]][f-4]^Z[B[f-1]][f-1]
 C&=CM[f]&CM[t];E=-1
 if(p&7)==1 and abs(t-f)==32:E=f+(16 if S==0 else-16)
 H^=ZC[C]^ZS;S^=8
def u():
 global S,C,E,H,HM
 mv,cap,cs,oC,oE,oH,oM=UN.pop();S^=8;C=oC;E=oE;H=oH;HM=oM
 if mv==0:return
 f=mv&127;t=(mv>>7)&127;pr=(mv>>14)&7;p=B[t]
 if pr:p=1|S;NP[S>>3]-=1
 B[f]=p;B[t]=0
 if(p&7)==6:
  KS[S>>3]=f
  if t-f==2:B[f+3]=B[f+1];B[f+1]=0
  elif f-t==2:B[f-4]=B[f-1];B[f-1]=0
 if cap:
  B[cs]=cap
  if(cap&7)!=1:NP[cap>>3]+=1
def e():
 mg=0;eg=0;ph=0;wb=0;bb=0
 for s in SQ:
  p=B[s]
  if not p:continue
  t=p&7;ph+=PW[t]
  if p&8:mg-=W[t]+MG[t][s^112];eg-=W[t]+EG[t][s^112];bb+=t==3
  else:mg+=W[t]+MG[t][s];eg+=W[t]+EG[t][s];wb+=t==3
 if wb>1:mg+=25;eg+=35
 if bb>1:mg-=25;eg-=35
 if ph>24:ph=24
 sc=(mg*ph+eg*(24-ph))//24
 return sc if S==0 else-sc
def o(ms,ttm,ply):
 def key(mv):
  if mv==ttm:return 1<<30
  f=mv&127;t=(mv>>7)&127;cap=B[t]
  if cap:return(1<<22)+W[cap&7]*32-(B[f]&7)
  if(mv>>14)&7:return(1<<22)+900
  if ply<1024 and mv==KL[ply]:return 1<<19
  return 0
 ms.sort(key=key,reverse=True)
def n(d,al,be,ply):
 global nd
 if d>0 and ply>0 and(H in PA or HM>=100):return 0
 nd+=1
 if nd>=NL:raise X
 inc=a(KS[S>>3],S^8)
 if d<=0:
  best=-100000
  if not inc:
   best=e()
   if best>=be:return best
   if best>al:al=best
  ms=g();o(ms,0,ply);legal=0
  for mv in ms:
   f=mv&127;t=(mv>>7)&127
   if not inc:
    if not B[t]and t!=E and not(mv>>14)&7:continue
    if B[t]and best+W[B[t]&7]+200<al and not(mv>>14)&7:continue
   m(mv)
   if a(KS[(S>>3)^1],S):u();continue
   legal+=1;sc=-n(0,-be,-al,ply+1);u()
   if sc>best:best=sc
   if sc>al:al=sc
   if al>=be:break
  if inc and not legal:return-99000+ply
  return best
 if inc:d+=1
 tt=TT.get(H);ttm=0
 if tt:
  ttm=tt[3]
  if ply>0 and tt[0]>=d:
   if tt[1]==0:return tt[2]
   if tt[1]==1 and tt[2]>=be:return tt[2]
   if tt[1]==2 and tt[2]<=al:return tt[2]
 if ply>0 and d>=3 and not inc and NP[S>>3]>0:
  m(0);sc=-n(d-3,-be,-be+1,ply+1);u()
  if sc>=be:return sc
 ms=g();o(ms,ttm,ply);PA.add(H);best=-100000;bm=0;legal=0;a0=al
 for mv in ms:
  f=mv&127;t=(mv>>7)&127;cap=B[t]or(mv>>14)&7
  m(mv)
  if a(KS[(S>>3)^1],S):u();continue
  legal+=1
  if d>=3 and legal>3 and not inc and not cap and not(mv>>14)&7:
   sc=-n(d-2,-al-1,-al,ply+1)
   if sc>al:sc=-n(d-1,-be,-al,ply+1)
  elif legal>1:
   sc=-n(d-1,-al-1,-al,ply+1)
   if al<sc<be:sc=-n(d-1,-be,-al,ply+1)
  else:sc=-n(d-1,-be,-al,ply+1)
  u()
  if sc>best:best=sc;bm=mv
  if sc>al:al=sc
  if al>=be:
   if not cap:KL[ply]=mv
   break
 PA.discard(H)
 if not legal:return-99000+ply if inc else 0
 TT[H]=(d,0 if a0<best<be else(1 if best>=be else 2),best,bm)
 return best
def F(fen):
 global B,S,C,E,H,HM
 ps=fen.split();B=[0]*128;NP[0]=NP[1]=0
 for i,row in enumerate(ps[0].split('/')):
  r=7-i;f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:
    p='PNBRQK'.index(ch.upper())+1
    if ch.islower():p+=8
    sq=r*16+f;B[sq]=p
    if(p&7)==6:KS[p>>3]=sq
    elif(p&7)!=1:NP[p>>3]+=1
    f+=1
 S=0 if ps[1]=='w'else 8;C=sum(1<<'KQkq'.index(ch)for ch in ps[2]if ch in'KQkq')
 E=-1
 if ps[3]!='-':E=(int(ps[3][1])-1)*16+(ord(ps[3][0])-97)
 HM=int(ps[4])if len(ps)>4 else 0;H=0
 for s in SQ:
  if B[s]:H^=Z[B[s]][s]
 H^=ZC[C]
 if S:H^=ZS
def x(mv):
 f=mv&127;t=(mv>>7)&127;pr=(mv>>14)&7
 u=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
 return u+('nbrq'[pr-2]if pr else'')
def choose(fen,gh):
 global nd,PA
 F(fen);PA=set(gh);ms=[];rh=H
 for mv in g():
  m(mv)
  if not a(KS[(S>>3)^1],S):ms.append(mv)
  u()
 if not ms:return[]
 o(ms,0,0);nd=0
 try:
  for d in range(1,100):
   n(d,-100000,100000,0)
   if nd>=NL:break
 except X:pass
 tt=TT.get(rh)
 if tt and tt[3]in ms:ms.remove(tt[3]);ms.insert(0,tt[3])
 return[x(mv)for mv in ms]
def post(pth,body):
 with urlopen(Request(os.environ['MAKEFUN_ENV_URL']+pth,data=json.dumps(body).encode()))as res:return json.load(res)
def main():
 gh=[];cur=None
 while True:
  g=post('/game',{})
  if g['status']=='done':break
  if g['game']!=cur:cur=g['game'];gh=[]
  while g['status']=='your_move':
   F(g['fen']);gh.append(H)
   try:cands=choose(g['fen'],gh)
   except Exception:cands=[]
   done=False
   for u2 in cands:
    try:g=post('/move',{'game':g['game'],'move':u2});done=True;break
    except HTTPError as ex:
     if ex.code!=400:raise
   if not done:g=post('/move',{'game':g['game'],'move':g['legal_moves'][0]})
if __name__=='__main__':main()
