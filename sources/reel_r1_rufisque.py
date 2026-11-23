import sys; sys.path.insert(0,'/home/claude/senanos-visuels/sources')
import common, reels_s46 as R
P='/home/claude/senanos-visuels/annonces/cmwt6ewy2000401ld6r897cnz/'
# Effet « Ken Burns » : zoom lent dans chaque photo (data-z = sens du zoom)
common.REEL_JS+=r'''
const _r=window.render;window.render=function(t){_r(t);document.querySelectorAll('[data-z]').forEach(el=>{const sc=el.closest('.sc');const a=+sc.dataset.s,b=+sc.dataset.e;const p=Math.max(0,Math.min(1,(t-a)/(b-a)));const z=el.dataset.z=='in'?1+.12*p:1.12-.12*p;el.style.transform=`scale(${z}) translateX(${(+el.dataset.px||0)*p}px)`;});};
'''
def ph(f,w,h,pos,a,z='in',px=0,extra=''):
    return f'''<div data-a="{a}" data-k="pop" style="width:{w}px;height:{h}px;border-radius:44px;border:10px solid #fff;box-shadow:0 18px 40px rgba(0,0,0,.16);overflow:hidden;{extra}"><div data-z="{z}" data-px="{px}" style="width:100%;height:100%;background:#eee url('file://{P}{f}') {pos}/cover no-repeat"></div></div>'''
chip=lambda t,a: f'<div class="pill" data-a="{a}" data-k="pop" style="font-size:40px;padding:16px 30px;background:#fff;color:#222;font-weight:600">{t}</div>'
s=f'''
<div class="sc" data-s="0" data-e="3.7" style="justify-content:flex-start;padding-top:240px"><div class="pill" style="font-size:38px;padding:16px 34px;margin-bottom:30px" data-a="0">🏡 À vendre · Rufisque</div>
{ph('6.jpg',900,820,'35% center',.05,'in',-20)}
<div class="fr" style="font-size:104px;line-height:1.02;margin-top:36px" data-a=".35">R+1 à vendre<br><span class="red">Neuf</span></div></div>
<div class="sc" data-s="3.6" data-e="7.6" style="justify-content:flex-start;padding-top:240px">
{ph('5.jpg',900,640,'center',.05,'out')}
<div style="display:flex;flex-wrap:wrap;gap:18px;justify-content:center;width:940px;margin-top:40px">{chip('🚪 5 pièces',.4)}{chip('📐 150 m²',.6)}{chip('🛏️ 4 chambres',.8)}{chip('🛁 4 salles de bain',1.0)}</div></div>
<div class="sc" data-s="7.5" data-e="11.1" style="justify-content:flex-start;padding-top:240px"><div class="pill" style="font-size:38px;padding:16px 34px;margin-bottom:30px" data-a="0">👀 Visite en photos</div>
<div style="display:flex;gap:20px">{ph('1.jpg',440,640,'center',.1,'in')}{ph('2.jpg',440,640,'center',.3,'in')}</div>
{ph('3.jpg',900,330,'center 78%',.6,'out',0,'margin-top:20px')}</div>
<div class="sc" data-s="11" data-e="14.6" style="justify-content:flex-start;padding-top:240px">
{ph('4.jpg',900,760,'center 60%',.05,'in')}
<div style="font-size:44px;color:#555;margin-top:40px" data-a=".3">Prix affiché</div>
<div class="fr red" style="font-size:112px;line-height:1;margin-top:10px" data-a=".5" data-k="pop">97 000 000<br>FCFA</div></div>
<div class="sc" data-s="14.5" data-e="18.1" style="justify-content:flex-start;padding-top:250px">
{ph('5.jpg',900,600,'center',0,'in')}
<div class="card" style="width:900px;padding:36px 40px;margin-top:34px;text-align:left" data-a=".3"><div style="font-size:46px;font-weight:600">R+1 à vendre · Neuf</div><div class="fr red" style="font-size:66px;margin-top:8px">97 000 000 FCFA</div><div style="font-size:36px;color:#666;margin-top:10px">📍 Rufisque / Ndiakhirate</div></div>
<div style="font-size:42px;color:#555;margin-top:30px" data-a=".7">À voir sur <b class="red">senanos.com</b></div></div>
{R.CTA(18,22.5)}'''
subs=[[0,3.6,'Une maison R+1 neuve à Rufisque'],[3.6,7.5,'5 pièces, 150 m², 4 chambres'],[7.5,11,'Annonce publiée sur SenAnos'],[11,14.5,'Envoie ça à quelqu’un qui cherche une maison'],[14.5,18,'Tous les détails sur senanos.com'],[18,22,'Publie ton annonce, 0 commission']]
common.reel('reel-r1-rufisque',22.5,s,subs,seed=9,bell_from=11)
