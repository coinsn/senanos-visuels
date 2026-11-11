import numpy as np, wave
sr=44100; D=27.5; N=int(sr*D); L=np.zeros(N); R=np.zeros(N); rng=np.random.default_rng(11)
env=lambda n,d: np.exp(-(np.arange(n)/sr)/d)
hp=lambda x: np.diff(np.concatenate([[0],x]))
noise=lambda n: rng.standard_normal(n)
def put(s,t,g=1.0,pan=0.0):
    i=int(round(t*sr))
    if i>=N or i<0: return
    j=min(N,i+len(s)); seg=s[:j-i]*g
    L[i:j]+=seg*(1-max(0,pan)); R[i:j]+=seg*(1+min(0,pan))
def sweep(f0,f1,rate,n): t=np.arange(n)/sr; return np.sin(2*np.pi*np.cumsum(f1+(f0-f1)*np.exp(-t*rate))/sr)
def kick(): n=int(sr*.4); return sweep(160,48,28,n)*env(n,.16)
def clap():
    n=int(sr*.22); e2=np.zeros(n)
    for d in (0,.012,.024):
        k=int(d*sr); e2[k:]+=env(n-k,.045)
    return hp(noise(n))*e2*.5
def shaker(): n=int(sr*.05); return hp(hp(noise(n)))*env(n,.012)*.3
def tom(f0,f1,dec=.09): n=int(sr*.3); return sweep(f0,f1,35,n)*env(n,dec)+.25*hp(noise(n))*env(n,.02)
def slap(): n=int(sr*.15); return .6*sweep(550,430,60,n)*env(n,.03)+.7*hp(noise(n))*env(n,.02)
def ks(f,dur,decay=.996):
    P=int(sr/f); n=int(sr*dur); buf=rng.uniform(-1,1,P); buf=.5*(buf+np.roll(buf,1)); out=np.zeros(n)
    for i in range(0,n,P):
        m=min(P,n-i); out[i:i+m]=buf[:m]; buf=decay*.5*(buf+np.roll(buf,1))
    return out
def bass(f,dur):
    n=int(sr*dur); t=np.arange(n)/sr
    s=np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*2*f*t)+.25*np.sin(2*np.pi*3*f*t)
    return s*np.minimum(1,t/.008)*np.exp(-t/(dur*.9))
def pad(fs,dur):
    n=int(sr*dur); t=np.arange(n)/sr; s=sum(np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*2*f*t) for f in fs)
    return s*np.minimum(1,t/.35)*np.minimum(1,(dur-t)/.35)/len(fs)
def riser(dur):
    n=int(sr*dur); a=(np.arange(n)/n)**2
    return hp(noise(n))*a*.6+.3*np.sin(2*np.pi*np.cumsum(np.linspace(200,1400,n))/sr)*a
def boom(): n=int(sr*1.2); return sweep(100,38,10,n)*env(n,.45)
def crash(): n=int(sr*1.6); return hp(noise(n))*env(n,.45)*.5
PROG=[dict(b=110.0,pl=[440,523.25,659.25,880],pd=[220,261.63,329.63]),
      dict(b=87.31,pl=[349.23,440,523.25,698.46],pd=[174.61,220,261.63]),
      dict(b=130.81,pl=[392,523.25,659.25,783.99],pd=[196,261.63,329.63]),
      dict(b=98.0,pl=[392,493.88,587.33,783.99],pd=[196,246.94,293.66])]
s16=.125; ARP=[0,1,2,3,2,1,2,1]
for b in range(-1,13):
    tb=1.5+2*b; ch=PROG[0] if b==12 else PROG[(b-1)%4]
    for st in range(16):
        t=tb+st*s16
        if t<0 or t>=D: continue
        intro=t<3.5; drop=12.5<=t<13.5; half=13.5<=t<15.5; outro=t>=25.5; full=not(intro or drop or half or outro)
        if drop: continue
        if outro:
            if st in (0,8):
                put(kick(),t,.9); put(boom(),t,.5)
                for k,f in enumerate(ch['pl']): put(ks(f,1.8,.998),t+k*.03,.3,(-.4+.27*k))
                put(bass(ch['b'],1.0),t,.34)
            continue
        if full and st in (0,4,8,12): put(kick(),t,.9)
        if full and st==10: put(kick(),t,.5)
        if half and st in (0,8): put(kick(),t,.9)
        if (full or half) and st in (4,12): put(clap(),t,.35)
        put(shaker(),t,(.16 if st%4==2 else .09)*(0.7 if intro else 1),.3)
        if (intro or full) and st in (3,6,7,11,14,15): put(tom(330,250) if st in (3,7,14) else tom(240,170),t,.3,-.3 if st%2 else .3)
        if not intro and st in (0,3,6,8,11,14): put(bass(ch['b']*(2 if st in (6,14) else 1),.3),t,.32)
        if st%2==0:
            k=st//2
            if intro or half:
                if k%2==0: put(ks(ch['pl'][ARP[k]],.9),t,.26,.25)
            else: put(ks(ch['pl'][ARP[k]],.6),t,.26,.35 if k%2 else -.35)
    pd=2.0
    if tb<12.5<tb+2: pd=12.5-tb
    if b<12 and tb+pd>0: put(pad(ch['pd'],pd),max(tb,0),.1)
put(riser(1.0),2.5,.2); put(boom(),3.5,.8); put(crash(),3.5,.22)
for i in range(5): put(slap(),3.5+.5*i,.45)
put(boom(),6.0,.7); put(crash(),6.0,.25)
for k,d in enumerate([0,.25,.5,.625,.75,.8125,.875,.9375]): put(slap(),12.5+d,.3+.06*k)
put(riser(1.0),12.5,.25); put(boom(),13.5,.9); put(crash(),13.5,.3)
for i in range(5): put(slap(),16.0+.5*i,.3,.4)
put(boom(),19.5,.6); put(crash(),19.5,.2); put(crash(),21.5,.25); put(boom(),21.5,.5)
x=np.stack([L,R],1); x=np.tanh(x*1.15); fo=int(1.0*sr); x[-fo:]*=np.linspace(1,0,fo)[:,None]; x/=np.max(np.abs(x))/.94
w=wave.open('music.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((x*32767).astype('<i2').tobytes()); w.close()
