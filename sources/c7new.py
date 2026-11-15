import sys; sys.path.insert(0,'/home/claude/senanos-visuels/sources')
from posts_lib import *
from annonce_card import annonce_card
T=7
p=frame(f'''<div class="pill" style="align-self:flex-start">👀 Annonce du jour sur SenAnos</div>
<div style="margin-top:28px">{annonce_card('🏢','Appartements à louer','Appartement 3 pièces à louer','250 000 FCFA','Dakar','Occasion',width=940,scale=.9)}</div>
<div class="fr" style="font-size:60px;line-height:1.08;margin-top:40px">Ton logement est prêt ?<br><span class="red">Publie ton annonce.</span></div>
<div style="margin-top:30px;display:flex;align-items:center;gap:30px"><span class="cta" style="font-size:34px;padding:22px 40px">Publie ton annonce</span><span class="fr" style="font-size:40px">senanos.com</span></div>
<div style="font-size:28px;color:#888;margin-top:18px">Sans commission · 📤 Envoie à un propriétaire que tu connais</div>''',7,T,swipe=False)
shoot_pages([p],W,H,'c7new')
