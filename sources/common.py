import re, os, subprocess, numpy as np, wave
SRC=open('/home/claude/pub2/pub.html').read()
LOGO=re.search(r'<svg viewBox="150 140 900 560">.*?</svg>',SRC,re.S).group(0)
FONTS=re.search(r'(@font-face.*?)(:root)',SRC,re.S).group(1)
BASE=FONTS+r'''
:root{--foreground:#222;--primary:#d7263d;--background:#f7f5f2}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#f7f5f2;font-family:I,sans-serif;color:#222;overflow:hidden;position:relative}
.red{color:#d7263d}
.brand{display:flex;align-items:center;gap:12px}.brand svg{width:80px;height:50px}
.word{font-family:DS;font-weight:700;font-size:48px;line-height:1}.word b{color:#d7263d}
.fr{font-family:Fraunces;font-weight:700;letter-spacing:-1.5px}
.glow{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(215,38,61,.14),rgba(215,38,61,0) 65%)}
.glow2{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(246,190,90,.2),rgba(246,190,90,0) 65%)}
.pill{display:inline-flex;gap:12px;align-items:center;border:2px solid #ead9d9;background:#fdf6f6;border-radius:999px;padding:12px 26px;font-size:28px;color:#555;font-weight:500}
.card{background:#fff;border:2px solid #ece8e3;border-radius:36px}
.cta{display:inline-block;background:#d7263d;color:#fff;border-radius:999px;padding:24px 46px;font-size:38px;font-weight:600}
'''
BRAND=f'<div class="brand">{LOGO}<div class="word">Sen<b>Anos</b></div></div>'
def shoot_pages(pages,w,h,prefix):
    from playwright.sync_api import sync_playwright
    out=[]
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':w,'height':h})
        for i,body in enumerate(pages):
            fn=f'{prefix}-{i+1}.html'
            open(fn,'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}body{{width:{w}px;height:{h}px}}</style></head><body>{body}</body></html>')
            pg.goto('file://'+os.path.abspath(fn)); pg.wait_for_timeout(400)
            png=f'{prefix}-{i+1}.png'; pg.screenshot(path=png)
            from PIL import Image; jpg=f'{prefix}-{i+1}.jpg'; Image.open(png).convert('RGB').save(jpg,quality=93); out.append(jpg)
        b.close()
    return out
def rhythm(path,D,bpm=118,seed=7,bell_from=None):
    sr=44100; beat=60/bpm; sub=beat/3; N=int(sr*D); out=np.zeros(N); rng=np.random.default_rng(seed)
    env=lambda n,d: np.exp(-(np.arange(n)/sr)/d)
    def drum(f0,f1,dec,dur,noise=0,nf=.03):
        n=int(sr*dur); t=np.arange(n)/sr; f=f1+(f0-f1)*np.exp(-t*30)
        s=np.sin(2*np.pi*np.cumsum(f)/sr)*env(n,dec)
        if noise: w=np.diff(np.concatenate([[0],rng.standard_normal(n)])); s+=noise*w*env(n,nf)
        return s
    def put(s,t,g):
        i=int(t*sr); j=min(N,i+len(s))
        if i<N: out[i:j]+=g*s[:j-i]
    pats=[("x.....x..x..","..x.x.....x.","...x.....x.x"),("x..x..x.....",".x...x..x.x.","..x..x.....x"),("x.....x.x...","...x.x.....x",".x.......xx.")]
    B,T,S=pats[seed%3]
    for k in range(int(D/sub)):
        t=k*sub;p=k%12
        if B[p]=='x': put(drum(120,62,.18,.5),t,.9)
        if T[p]=='x': put(drum(330,250,.08,.3,.35),t,.45)
        if S[p]=='x' and t>1: put(drum(520,420,.03,.2,.9,.025),t,.5)
        if t>2.5: put(.25*np.diff(np.concatenate([[0],rng.standard_normal(int(sr*.06))]))*env(int(sr*.06),.015),t,.35 if p%3==0 else .17)
        if bell_from and t>bell_from and k%3==0: put(np.sin(2*np.pi*(880 if (k//3)%2 else 660)*np.arange(int(sr*.25))/sr)*env(int(sr*.25),.06),t,.12)
    fi=int(.3*sr);fo=int(1.2*sr); out[:fi]*=np.linspace(0,1,fi); out[-fo:]*=np.linspace(1,0,fo)
    out/=np.max(np.abs(out))*1.15; st=np.stack([out,out],1)
    w=wave.open(path,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype('<i2').tobytes()); w.close()
REEL_CSS=r'''
body{width:1080px;height:1920px}
.sc{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 90px;opacity:0}
.top{position:absolute;top:110px;left:0;right:0;display:flex;justify-content:center}
.top .brand svg{width:90px;height:56px}.top .word{font-size:56px}
.sub{position:absolute;left:60px;right:60px;bottom:330px;text-align:center}
.sub span{background:rgba(34,34,34,.88);color:#fff;font-size:40px;font-weight:600;padding:14px 26px;border-radius:18px;line-height:1.7;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.bar{position:absolute;left:0;bottom:0;height:12px;background:#d7263d}
[data-a]{opacity:0}
'''
REEL_JS=r'''
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)); const e=x=>1-Math.pow(1-cl(x),3);
const back=x=>{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
window.render=function(t){
 document.querySelectorAll('.glow,.glow2').forEach((g,i)=>g.style.transform=`translate(${Math.sin(t*.5+i)*40}px,${Math.cos(t*.4+i)*40}px)`);
 document.querySelectorAll('.sc').forEach(s=>{const a=+s.dataset.s,b=+s.dataset.e;s.style.opacity=cl((t-a)/.3)*cl((b-t)/.3);
   s.querySelectorAll('[data-a]').forEach(el=>{const d=a+(+el.dataset.a);const k=el.dataset.k||'up';const x=(t-d)/.5;
     el.style.opacity=cl((t-d)/.25);
     if(k=='pop')el.style.transform=`scale(${back(x)})`; else if(k=='left')el.style.transform=`translateX(${(1-e(x))*-200}px)`; else el.style.transform=`translateY(${(1-e(x))*70}px)`;
     if(el.dataset.type){const s0=el.dataset.type;const n=Math.floor(cl((t-d)/(+el.dataset.dur||1))*s0.length);el.textContent=s0.slice(0,n);}
   });});
 const s=SUBS.find(x=>t>=x[0]&&t<x[1]);document.getElementById('subt').textContent=s?s[2]:'';document.getElementById('sub').style.opacity=s?cl((t-s[0])/.25)*cl((s[1]-t)/.25):0;
 document.getElementById('bar').style.width=(t/DUR*100)+'%';
 document.querySelector('.top').style.opacity=e(t/.6);
};
'''
def reel(name,D,scenes_html,subs,seed,bell_from):
    html=f'''<!doctype html><html><head><meta charset="utf-8"><style>{BASE}{REEL_CSS}</style></head><body>
<div class="glow" style="width:1100px;height:1100px;right:-400px;top:-350px"></div><div class="glow2" style="width:900px;height:900px;left:-350px;bottom:-300px"></div>
<div class="top">{BRAND}</div>{scenes_html}
<div class="sub" id="sub"><span id="subt"></span></div><div class="bar" id="bar"></div>
<script>const DUR={D};const SUBS={subs};{REEL_JS}render(0);</script></body></html>'''
    open(f'{name}.html','w').write(html)
    os.makedirs(f'fr_{name}',exist_ok=True)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
        pg.goto('file://'+os.path.abspath(f'{name}.html')); pg.wait_for_timeout(800)
        for i in range(int(30*D)):
            pg.evaluate(f'render({i/30})'); pg.screenshot(path=f'fr_{name}/f{i:04d}.jpg',type='jpeg',quality=92)
        b.close()
    rhythm(f'{name}.wav',D,bpm=112+seed*4,seed=seed,bell_from=bell_from)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','30','-i',f'fr_{name}/f%04d.jpg','-i',f'{name}.wav','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',f'{name}.mp4'],check=True)
    from PIL import Image
    idx=[int(30*x) for x in np.linspace(1,D-1,6)]
    ims=[Image.open(f'fr_{name}/f{i:04d}.jpg').resize((270,480)) for i in idx]
    s=Image.new('RGB',(280*6,480),'white')
    for k,im in enumerate(ims): s.paste(im,(k*280,0))
    s.save(f'{name}-contact.jpg')
