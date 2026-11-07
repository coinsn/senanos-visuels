# Reel Loulou "Jël ko foto" : vidéo IA du propriétaire + sous-titres wolof/français + carte de fin
import os,subprocess,sys
from common import *
import json
CFG=json.load(open(sys.argv[2])) if len(sys.argv)>2 else {}
SRC=sys.argv[1]; OUT=CFG.get('out','reel-loulou-jel-ko-foto')
V=7.93; E=4.0; D=V+E; FPS=30
subs=CFG.get('subs',[[1.8,4.3,'Jël ko foto,','Prends-le en photo,'],[4.3,6.4,'def sa prix,','fixe ton prix,'],[6.4,V,'jaay ko ci SenAnos.','vends-le sur SenAnos.']])
HOOK=CFG.get('hook','<div class="fr" style="font-size:64px;line-height:1.1">Am nga lu nelaw<br><span class="red">ci sa kër ?</span></div><div style="font-size:32px;color:#666;margin-top:10px">Tu as quelque chose qui dort chez toi ?</div>')
END=CFG.get('end','<div class="fr" style="font-size:84px;line-height:1.1" data-a="0">Amul commission !</div><div class="fr red" style="font-size:72px;line-height:1.1;margin-top:24px" data-a=".25">Sa anos moy sa khaliss</div><div style="font-size:38px;color:#666;margin-top:16px" data-a=".4">Ton annonce, ton argent. 0 commission.</div>')
MUSV=CFG.get('music_under',0.22)
ov=f'''<!doctype html><html><head><meta charset="utf-8"><style>{BASE}
html,body{{background:transparent!important;width:1080px;height:1920px}}
.hook{{position:absolute;top:140px;left:70px;right:70px;text-align:center}}
.hook .q{{display:inline-block;background:#fff;border-radius:34px;padding:26px 38px;box-shadow:0 12px 30px rgba(0,0,0,.18)}}
.sub{{position:absolute;left:60px;right:60px;bottom:330px;text-align:center}}
.sub .w{{display:inline-block;background:rgba(34,34,34,.9);color:#fff;font-size:54px;font-weight:700;padding:14px 30px;border-radius:20px}}
.sub .f{{display:block;margin:12px auto 0;width:max-content;background:#fff;color:#d7263d;font-size:36px;font-weight:600;padding:10px 24px;border-radius:16px}}
.bar{{position:absolute;left:0;bottom:0;height:12px;background:#d7263d}}
</style></head><body>
<div class="hook" id="hook"><div class="q">{HOOK}</div></div>
<div class="sub" id="sub"><span class="w" id="w"></span><span class="f" id="f"></span></div><div class="bar" id="bar"></div>
<script>const S={subs},DUR={D};
window.render=t=>{{const h=document.getElementById('hook');h.style.opacity=Math.min(1,t/.3)*Math.max(0,Math.min(1,(2.1-t)/.3));h.style.transform=`scale(${{0.9+0.1*Math.min(1,t/.35)}})`;
const s=S.find(x=>t>=x[0]&&t<x[1]);document.getElementById('sub').style.opacity=s?1:0;if(s){{document.getElementById('w').textContent=s[2];document.getElementById('f').textContent=s[3];}}
document.getElementById('bar').style.width=(t/DUR*100)+'%';}}</script></body></html>'''
open('ov.html','w').write(ov); os.makedirs('ov',exist_ok=True)
end=f'''<!doctype html><html><head><meta charset="utf-8"><style>{BASE}{REEL_CSS}</style></head><body>
<div class="glow" style="width:1100px;height:1100px;right:-400px;top:-350px"></div><div class="glow2" style="width:900px;height:900px;left:-350px;bottom:-300px"></div>
<div class="top" style="opacity:1">{BRAND}</div>
<div class="sc" data-s="0" data-e="99">{END}
<div class="cta" style="margin-top:56px;font-size:48px;padding:32px 58px" data-a=".6" data-k="pop">Publie ton annonce</div>
<div class="fr" style="font-size:62px;margin-top:46px" data-a=".9">senanos.com</div><div style="font-size:34px;color:#888;margin-top:14px" data-a="1.1">Lien dans la bio 👆</div></div>
<div class="sub" id="sub" style="opacity:0"><span id="subt"></span></div><div class="bar" id="bar"></div>
<script>const DUR={D},OFF={V};const SUBS=[];{REEL_JS}
const r0=window.render;window.render=t=>{{r0(t);document.getElementById('bar').style.width=((t+OFF)/DUR*100)+'%';document.querySelector('.top').style.opacity=1;}};render(0);</script></body></html>'''
open('end.html','w').write(end); os.makedirs('endf',exist_ok=True)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+os.path.abspath('ov.html')); pg.wait_for_timeout(800)
    for i in range(int(V*FPS)+1):
        pg.evaluate(f'render({i/FPS})'); pg.screenshot(path=f'ov/o{i:04d}.png',omit_background=True)
    pg.goto('file://'+os.path.abspath('end.html')); pg.wait_for_timeout(800)
    for i in range(int(E*FPS)):
        pg.evaluate(f'render({i/FPS})'); pg.screenshot(path=f'endf/e{i:04d}.jpg',type='jpeg',quality=92)
    b.close()
rhythm('beat.wav',D,bpm=120,seed=CFG.get('seed',10),bell_from=V)
fc=(f"[0:v]scale=1080:1920:flags=lanczos,fps=30,setsar=1,trim=duration={V},setpts=PTS-STARTPTS[bg];"
    f"[bg][1:v]overlay=0:0:shortest=1,format=yuv420p[a];[2:v]fps=30,setsar=1,format=yuv420p[b];[a][b]concat=n=2:v=1:a=0[v];"
    f"[0:a]atrim=duration={V},asetpts=PTS-STARTPTS,aresample=44100,apad=whole_dur={D},volume=1.0[voice];"
    f"[3:a]volume='if(lt(t,{V}),{MUSV},0.9)':eval=frame[mus];[voice][mus]amix=inputs=2:normalize=0:duration=longest,atrim=duration={D}[au]")
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',SRC,'-framerate','30','-i','ov/o%04d.png','-framerate','30','-i','endf/e%04d.jpg','-i','beat.wav',
 '-filter_complex',fc,'-map','[v]','-map','[au]','-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30','-c:a','aac','-b:a','192k','-movflags','+faststart',OUT+'.mp4'],check=True)
