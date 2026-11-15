import sys; sys.path.insert(0,'/home/claude/senanos-visuels/sources')
import reels_s46 as R
from common import reel
from annonce_card import annonce_card
sE=R.sE.split('{CTA')[0] if '{CTA' in R.sE else None
# rebuild: keep scenes up to 18.6, add annonce scene, then CTA
base=R.sE[:R.sE.rfind('<div class="sc" data-s="18.5"')]
ann=f'''<div class="sc" data-s="18.5" data-e="21.6"><div class="pill" style="font-size:38px;padding:16px 34px;margin-bottom:40px" data-a="0">👀 Annonce du jour</div>
<div data-a=".25" data-k="pop">{annonce_card('🥭','Terrains & vergers','Verger avec manguiers · 1,91 ha','9 850 000 FCFA','Thiès (Tassette)','Neuf',width=900)}</div>
<div style="font-size:40px;color:#555;margin-top:36px" data-a=".7">À voir sur senanos.com</div></div>'''
s=base+ann+R.CTA(21.5,25)
subs=[x for x in R.subsE[:-1]]+[[18.5,21.5,'Une vraie annonce à découvrir sur SenAnos'],[21.5,24.5,'Achète et vends en confiance sur senanos.com']]
reel('reelE2-rendez-vous',25,s,subs,seed=5,bell_from=15.5)
