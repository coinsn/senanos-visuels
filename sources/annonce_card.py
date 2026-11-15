# Carte « Annonce du jour » au style du site (sans photo du vendeur)
def annonce_card(emoji,cat,titre,prix,lieu,etat,width=860,scale=1.0,extra=''):
    s=lambda v:int(v*scale)
    return f'''<div class="card" style="width:{width}px;padding:{s(34)}px;text-align:left;box-shadow:0 14px 30px rgba(0,0,0,.07);{extra}">
<div style="height:{s(250)}px;border-radius:{s(26)}px;background:linear-gradient(135deg,#fdecee,#fbf3e4);display:flex;align-items:center;justify-content:center;font-size:{s(130)}px;position:relative">{emoji}
<span style="position:absolute;top:{s(18)}px;left:{s(18)}px;background:#fff;border-radius:999px;padding:{s(8)}px {s(20)}px;font-size:{s(24)}px;font-weight:600;color:#555">{cat}</span>
<span style="position:absolute;top:{s(18)}px;right:{s(18)}px;background:#d7263d;color:#fff;border-radius:999px;padding:{s(8)}px {s(20)}px;font-size:{s(24)}px;font-weight:600">{etat}</span></div>
<div style="font-size:{s(40)}px;font-weight:600;line-height:1.25;margin-top:{s(24)}px">{titre}</div>
<div class="fr red" style="font-size:{s(56)}px;margin-top:{s(10)}px">{prix}</div>
<div style="font-size:{s(30)}px;color:#666;margin-top:{s(8)}px">📍 {lieu}</div></div>'''
