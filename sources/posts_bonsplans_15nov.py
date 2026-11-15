import sys; sys.path.insert(0,'/home/claude/senanos-visuels/sources')
from posts_lib import *
from annonce_card import annonce_card
items=[('📱','Électronique','iPhone 13 simple Authentique','175 000 FCFA','Dakar','Neuf'),
('💻','Électronique','MacBook Pro M2','950 000 FCFA','Dakar','Occasion'),
('🌳','Terrains','Terrain 8 256 m²','6 500 000 FCFA','Mboro (Touba Ndiaye)','Neuf'),
('🌾','Terres agricoles','Terre agricole 2,23 ha','10 058 000 FCFA','Mbour (Ndiaganiao)','Neuf')]
cards=''.join(f'<div style="width:455px">{annonce_card(*it,width=455,scale=.52)}</div>' for it in items)
p=f'''<div class="glow" style="width:800px;height:800px;right:-260px;top:-300px"></div><div class="glow2" style="width:700px;height:700px;left:-260px;bottom:-280px"></div>
<div style="position:absolute;inset:0;padding:60px 70px 56px;display:flex;flex-direction:column">
<div>{BRAND}</div>
<div class="pill" style="align-self:flex-start;margin-top:34px">👀 En ce moment sur SenAnos</div>
<div class="fr" style="font-size:78px;line-height:1.04;margin-top:20px">Les bons plans<br><span class="red">près de chez toi</span></div>
<div style="display:flex;flex-wrap:wrap;gap:30px;margin-top:36px">{cards}</div>
<div style="font-size:34px;color:#555;margin-top:44px;text-align:center">Et toi, qu’est-ce que tu vends ?<br><b>0 commission</b> sur ta vente.</div>
<div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between"><span class="cta" style="font-size:34px;padding:22px 40px">Publie ton annonce</span><span class="fr" style="font-size:40px">senanos.com</span></div></div>'''
shoot_pages([p],W,H,'bp')
