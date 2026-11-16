import sys; sys.path.insert(0,'/home/claude/senanos-visuels/sources')
import reels_s46 as R
from common import reel
P='/home/claude/work/honda/'
ph=lambda f,h,pos,a: f'''<div data-a="{a}" data-k="pop" style="width:900px;height:{h}px;border-radius:44px;border:10px solid #fff;box-shadow:0 18px 40px rgba(0,0,0,.14);background:#eee url('file://{P}{f}') {pos}/cover no-repeat"></div>'''
s=f'''
<div class="sc" data-s="0" data-e="3.6" style="justify-content:flex-start;padding-top:250px"><div class="pill" style="font-size:38px;padding:16px 34px;margin-bottom:34px" data-a="0">👀 Annonce de la semaine</div>
{ph('1.jpg',680,'center',.1)}
<div class="fr" style="font-size:92px;line-height:1.06;margin-top:44px" data-a=".4">Honda Lead<br><span class="red">très bon état</span></div></div>
<div class="sc" data-s="3.5" data-e="7.1" style="justify-content:flex-start;padding-top:250px"><div class="pill" style="font-size:38px;padding:16px 34px;margin-bottom:34px" data-a="0">🛵 Véhicules · Occasion</div>
{ph('2.jpg',860,'center bottom',.1)}
<div class="fr red" style="font-size:104px;line-height:1;margin-top:40px" data-a=".4" data-k="pop">250 000 FCFA</div></div>
<div class="sc" data-s="7.0" data-e="10.6" style="justify-content:flex-start;padding-top:250px">
{ph('1.jpg',680,'center',0)}
<div class="card" style="width:900px;padding:36px 40px;margin-top:36px;text-align:left" data-a=".3"><div style="font-size:44px;font-weight:600">Honda Lead très bon état</div><div class="fr red" style="font-size:64px;margin-top:8px">250 000 FCFA</div><div style="font-size:36px;color:#666;margin-top:10px">📍 Guédiawaye</div></div>
<div style="font-size:42px;color:#555;margin-top:34px" data-a=".7">À voir sur senanos.com</div></div>
<div class="sc" data-s="10.5" data-e="13.1"><div style="font-size:150px" data-a="0" data-k="pop">📣</div><div class="fr" style="font-size:92px;line-height:1.08" data-a=".2">Et ton annonce ?<br><span class="red">Elle peut passer ici.</span></div><div style="font-size:42px;color:#555;margin-top:30px" data-a=".6">0 commission sur ta vente</div></div>
{R.CTA(13.0,17)}'''
subs=[[0,3.5,'Une moto à vendre à Guédiawaye'],[3.5,7,'Annonce publiée sur SenAnos'],[7,10.5,'Envoie ça à quelqu’un qui cherche une moto'],[10.5,13,'Publie ton annonce pour plus de visibilité'],[13,16.5,'Publie ton annonce sur senanos.com']]
reel('reelA1-honda-lead',17,s,subs,seed=12,bell_from=10.5)
