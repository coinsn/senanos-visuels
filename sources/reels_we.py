from reels_s46 import CTA,BIG,row
from common import reel
bub=lambda txt,me,a,extra='': f'''<div data-a="{a}" data-k="left" style="align-self:{'flex-end' if me else 'flex-start'};max-width:82%;background:{'#dcf8c6' if me else '#fff'};border-radius:28px;padding:22px 28px;font-size:34px;line-height:1.35;text-align:left;box-shadow:0 6px 14px rgba(0,0,0,.08);{extra}">{txt}</div>'''
# Reel G : prix trop beau pour être vrai
sG=f'''
<div class="sc" data-s="0" data-e="3.2"><div style="font-size:150px" data-a="0" data-k="pop">🤑</div><div {BIG} data-a=".2">Un iPhone<br>presque neuf…<br><span class="red">à moitié&nbsp;prix&nbsp;?</span></div></div>
<div class="sc" data-s="3.1" data-e="9.4"><div class="card" style="width:860px;padding:34px;background:#efeae2;display:flex;flex-direction:column;gap:22px" data-a="0">
<div style="display:flex;align-items:center;gap:18px;padding-bottom:18px;border-bottom:2px solid #ddd5ca"><div style="width:70px;height:70px;border-radius:50%;background:#ccc;display:flex;align-items:center;justify-content:center;font-size:38px">💬</div><div style="text-align:left"><div style="font-size:32px;font-weight:600">« Vendeur »</div><div style="font-size:24px;color:#888">en ligne</div></div></div>
{bub('Il est toujours dispo ? On peut se voir ?',True,.4)}
{bub('Je suis en voyage 🙏🏾 Envoie un acompte par Wave et le livreur te l’apporte demain.',False,1.6,'border:3px solid #d7263d')}
{bub('Vite, d’autres personnes sont intéressées !',False,3.4,'border:3px solid #d7263d')}
</div></div>
<div class="sc" data-s="9.3" data-e="15.2"><div class="fr" style="font-size:80px;line-height:1.1;margin-bottom:46px" data-a="0">🚩 3 signaux<br><span class="red">d’alerte</span></div>
{row('💸 Prix très bas',.4)}{row('🙈 Impossible de se voir',1)}{row('⏳ Acompte + pression',1.6)}</div>
<div class="sc" data-s="15.1" data-e="19.2"><div style="font-size:150px" data-a="0" data-k="pop">✅</div><div class="fr" style="font-size:86px;line-height:1.1" data-a=".2">Rencontre,<br>vérifie,<br><span class="red">puis paie.</span></div></div>
{CTA(19.1,24)}'''
subsG=[[0,3.1,'Une affaire trop belle pour être vraie ?'],[3.1,9.3,'Acompte, livreur, pression : méfiance'],[9.3,15.1,'Un prix très bas peut cacher une arnaque'],[15.1,19.1,'Jamais de Wave ou d’OM avant de voir le produit'],[19.1,23,'Envoie ça à quelqu’un qui achète en ligne']]
reel('reelG-prix-trop-beau',24,sG,subsG,seed=8,bell_from=15.1)
# Reel H : ta moto à vendre
sH=f'''
<div class="sc" data-s="0" data-e="3.2"><div style="font-size:160px" data-a="0" data-k="pop">🛵</div><div {BIG} data-a=".2">Ta moto dort<br><span class="red">dans la&nbsp;cour&nbsp;?</span></div></div>
<div class="sc" data-s="3.1" data-e="5.9"><div class="fr" style="font-size:94px;line-height:1.08" data-a="0">Vends-la sur<br><span class="red">SenAnos</span> 💸</div><div style="font-size:44px;color:#555;margin-top:30px" data-a=".5">En 3 étapes</div></div>
<div class="sc" data-s="5.8" data-e="9.6"><div style="font-size:150px" data-a="0" data-k="pop">📸</div><div class="fr" style="font-size:86px;line-height:1.08" data-a=".2">1. Les photos</div><div style="font-size:44px;color:#555;margin-top:30px;line-height:1.4" data-a=".6">Les 2 côtés, l’avant,<br>le compteur, le moteur</div></div>
<div class="sc" data-s="9.5" data-e="14.2"><div class="fr" style="font-size:80px;line-height:1.1;margin-bottom:46px" data-a="0">📝 2. Les infos</div>
{row('🏷️ Marque et modèle',.4)}{row('📅 Année',.8)}{row('🧭 Kilométrage',1.2)}{row('📄 Papiers à jour ?',1.6)}</div>
<div class="sc" data-s="14.1" data-e="17.6"><div style="font-size:150px" data-a="0" data-k="pop">💵</div><div class="fr" style="font-size:86px;line-height:1.08" data-a=".2">3. Un prix clair<br><span class="red">+ ta ville</span></div></div>
<div class="sc" data-s="17.5" data-e="20.2"><div class="fr" style="font-size:90px;line-height:1.08" data-a="0">0 commission<br><span class="red">sur ta vente.</span></div></div>
{CTA(20.1,25)}'''
subsH=[[0,3.1,'Une moto ou un scooter que tu n’utilises plus ?'],[3.1,5.8,'Publie ton annonce en 3 étapes'],[5.8,9.5,'Des photos nettes, sous tous les angles'],[9.5,14.1,'Toutes les infos que l’acheteur demande'],[14.1,17.5,'Un prix en FCFA et ta ville'],[17.5,20.1,'Tout l’argent de la vente reste pour toi'],[20.1,24,'Publie ton annonce sur senanos.com']]
reel('reelH-moto-a-vendre',25,sH,subsH,seed=9,bell_from=17.5)
