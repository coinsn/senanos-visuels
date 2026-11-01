from common import *
BIG='class="fr" style="font-size:106px;line-height:1.05"'
CTA=lambda a,b: f'''<div class="sc" data-s="{a}" data-e="{b}"><div class="fr" style="font-size:84px;line-height:1.1" data-a="0">Le marché de tout,<br><span class="red">près de chez vous</span></div>
<div class="pill" style="margin-top:46px;font-size:36px;padding:16px 34px" data-a=".3">📍 Partout au Sénégal · sans commission</div>
<div class="cta" style="margin-top:56px;font-size:48px;padding:32px 58px" data-a=".6" data-k="pop">Publie ton annonce</div>
<div class="fr" style="font-size:62px;margin-top:46px" data-a=".9">senanos.com</div><div style="font-size:34px;color:#888;margin-top:14px" data-a="1.1">Lien dans la bio 👆</div></div>'''
row=lambda txt,a: f'<div class="card" style="padding:30px 40px;font-size:42px;font-weight:600;margin-bottom:20px;width:860px;text-align:left" data-a="{a}" data-k="left">{txt}</div>'
# Reel E : remise en main propre, 4 réflexes
sE=f'''
<div class="sc" data-s="0" data-e="3.2"><div style="font-size:150px" data-a="0" data-k="pop">📍</div><div {BIG} data-a=".2">Vous vous voyez<br><span class="red">où</span> pour<br>la vente ?</div></div>
<div class="sc" data-s="3.1" data-e="6.4"><div style="font-size:150px" data-a="0" data-k="pop">🏪</div><div class="fr" style="font-size:90px;line-height:1.08" data-a=".2">1. Un lieu public<br><span class="red">et fréquenté</span></div><div style="font-size:42px;color:#555;margin-top:30px" data-a=".7">Jamais dans un endroit isolé</div></div>
<div class="sc" data-s="6.3" data-e="9.4"><div style="font-size:150px" data-a="0" data-k="pop">☀️</div><div class="fr" style="font-size:90px;line-height:1.08" data-a=".2">2. En journée,<br><span class="red">pas la nuit</span></div></div>
<div class="sc" data-s="9.3" data-e="12.4"><div style="font-size:150px" data-a="0" data-k="pop">👥</div><div class="fr" style="font-size:90px;line-height:1.08" data-a=".2">3. Viens<br><span class="red">accompagné·e</span></div><div style="font-size:42px;color:#555;margin-top:30px" data-a=".7">Et préviens un proche</div></div>
<div class="sc" data-s="12.3" data-e="15.6"><div style="font-size:150px" data-a="0" data-k="pop">🔍</div><div class="fr" style="font-size:86px;line-height:1.08" data-a=".2">4. Vérifie le produit,<br><span class="red">puis paie</span></div><div style="font-size:42px;color:#555;margin-top:30px" data-a=".7">Wave / OM : jamais avant de voir</div></div>
<div class="sc" data-s="15.5" data-e="18.6"><div class="fr" style="font-size:80px;line-height:1.1;margin-bottom:46px" data-a="0">Les 4 réflexes</div>
{row('📍 Lieu public',.3)}{row('☀️ En journée',.6)}{row('👥 Accompagné·e',.9)}{row('🔍 Voir avant de payer',1.2)}</div>
{CTA(18.5,23)}'''
subsE=[[0,3.1,'Tu as trouvé un acheteur ou un vendeur ?'],[3.1,6.3,'Choisis un lieu public, avec du monde'],[6.3,9.3,'Donne rendez-vous en journée'],[9.3,12.3,'Viens avec quelqu’un de confiance'],[12.3,15.5,'Vérifie le produit avant de payer'],[15.5,18.5,'Envoie ça à quelqu’un qui achète en ligne'],[18.5,22,'Achète et vends en confiance sur senanos.com']]
if __name__=="__main__": reel('reelE-rendez-vous',23,sE,subsE,seed=5,bell_from=15.5)
# Reel F : combien vaut ton téléphone d'occasion
sF=f'''
<div class="sc" data-s="0" data-e="3.2"><div style="font-size:150px" data-a="0" data-k="pop">📱</div><div {BIG} data-a=".2">Ton ancien<br>téléphone dort<br><span class="red">dans un tiroir ?</span></div></div>
<div class="sc" data-s="3.1" data-e="5.8"><div class="fr" style="font-size:96px;line-height:1.08" data-a="0">Il vaut peut-être<br><span class="red">encore de l’argent</span> 💸</div></div>
<div class="sc" data-s="5.7" data-e="10.6"><div class="fr" style="font-size:76px;line-height:1.1;margin-bottom:46px" data-a="0">⬆️ Ce qui fait<br><span style="color:#2e9e5b">monter le prix</span></div>
{row('✨ Écran sans rayure',.4)}{row('🔋 Bonne batterie',.8)}{row('💾 Gros stockage',1.2)}{row('📦 Boîte, chargeur, facture',1.6)}</div>
<div class="sc" data-s="10.5" data-e="14.4"><div class="fr" style="font-size:76px;line-height:1.1;margin-bottom:46px" data-a="0">⬇️ Ce qui le fait<br><span class="red">baisser</span></div>
{row('💥 Écran fissuré',.4)}{row('🪫 Batterie faible',.8)}{row('🔒 Compte non déconnecté',1.2)}</div>
<div class="sc" data-s="14.3" data-e="18.4"><div style="font-size:150px" data-a="0" data-k="pop">🔎</div><div class="fr" style="font-size:84px;line-height:1.1" data-a=".2">Ton vrai prix ?<br><span class="red">Compare les annonces<br>similaires</span></div><div style="font-size:42px;color:#555;margin-top:30px" data-a=".7">Même modèle, même état</div></div>
{CTA(18.3,23)}'''
subsF=[[0,3.1,'Un téléphone que tu n’utilises plus ?'],[3.1,5.7,'Quelqu’un le cherche peut-être'],[5.7,10.5,'Ces points font monter son prix'],[10.5,14.3,'Ceux-là le font baisser : sois honnête'],[14.3,18.3,'Regarde les annonces du même modèle'],[18.3,22,'Publie ton annonce, 0 commission']]
if __name__=="__main__": reel('reelF-combien-vaut-telephone',23,sF,subsF,seed=6,bell_from=14.3)
