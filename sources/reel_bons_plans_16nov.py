import sys; sys.path.insert(0,'/home/claude/senanos-visuels/sources')
import reels_s46 as R
from common import reel
from annonce_card import annonce_card
items=[('📱','Électronique','iPhone 13 simple Authentique','175 000 FCFA','Dakar','Neuf'),
('💻','Électronique','MacBook Pro M2','950 000 FCFA','Dakar','Occasion'),
('🛵','Véhicules','Honda Lead très bon état','250 000 FCFA','Guédiawaye','Occasion'),
('🏢','Appartements à louer','Appartement 3 pièces à louer','250 000 FCFA','Dakar','Occasion'),
('🌳','Terrains','Terrain 8 256 m²','6 500 000 FCFA','Mboro (Touba Ndiaye)','Neuf')]
s=f'''<div class="sc" data-s="0" data-e="2.7"><div style="font-size:150px" data-a="0" data-k="pop">🔥</div><div {R.BIG} data-a=".15">Les bons plans<br><span class="red">du moment</span><br>sur SenAnos</div></div>'''
subs=[[0,2.6,'5 vraies annonces à voir cette semaine']]
t=2.6
for i,it in enumerate(items):
    s+=f'''<div class="sc" data-s="{t:.1f}" data-e="{t+3.1:.1f}"><div class="pill" style="font-size:38px;padding:16px 34px;margin-bottom:40px" data-a="0">👀 Annonce {i+1}/5</div>
<div data-a=".15" data-k="pop">{annonce_card(*it,width=900)}</div>
<div style="font-size:40px;color:#555;margin-top:36px" data-a=".6">À voir sur senanos.com</div></div>'''
    subs.append([t,t+3,f'{it[2]} · {it[4]}'])
    t+=3
s+=f'''<div class="sc" data-s="{t:.1f}" data-e="{t+3.1:.1f}"><div style="font-size:150px" data-a="0" data-k="pop">📣</div><div class="fr" style="font-size:92px;line-height:1.08" data-a=".2">Et ton annonce ?<br><span class="red">Elle peut passer ici.</span></div><div style="font-size:42px;color:#555;margin-top:30px" data-a=".7">0 commission sur ta vente</div></div>'''
subs.append([t,t+3,'Publie ton annonce pour plus de visibilité'])
t+=3
s+=R.CTA(round(t,1),25)
subs.append([t,24.5,'Publie ton annonce sur senanos.com'])
reel('reelBP-bons-plans',25,s,subs,seed=11,bell_from=17.6)
