# Carte « Annonce du jour » au style du site.
# photo = chemin absolu d'une vraie photo de l'annonce (dossier annonces/<id>/ du dépôt) ; sinon emoji de catégorie.
def annonce_card(emoji,cat,titre,prix,lieu,etat,width=860,scale=1.0,extra='',photo=None,photo_h=None):
    s=lambda v:int(v*scale)
    h=photo_h or (s(470) if photo else s(250))
    fond=f"background:#f1ede8 url('file://{photo}') center/cover no-repeat" if photo else 'background:linear-gradient(135deg,#fdecee,#fbf3e4)'
    return f'''<div class="card" style="width:{width}px;padding:{s(34)}px;text-align:left;box-shadow:0 14px 30px rgba(0,0,0,.07);{extra}">
<div style="height:{h}px;border-radius:{s(26)}px;{fond};display:flex;align-items:center;justify-content:center;font-size:{s(130)}px;position:relative;overflow:hidden">{'' if photo else emoji}
<span style="position:absolute;top:{s(18)}px;left:{s(18)}px;background:#fff;border-radius:999px;padding:{s(8)}px {s(20)}px;font-size:{s(24)}px;font-weight:600;color:#555">{cat}</span>
<span style="position:absolute;top:{s(18)}px;right:{s(18)}px;background:#d7263d;color:#fff;border-radius:999px;padding:{s(8)}px {s(20)}px;font-size:{s(24)}px;font-weight:600">{etat}</span></div>
<div style="font-size:{s(40)}px;font-weight:600;line-height:1.25;margin-top:{s(24)}px">{titre}</div>
<div class="fr red" style="font-size:{s(56)}px;margin-top:{s(10)}px">{prix}</div>
<div style="font-size:{s(30)}px;color:#666;margin-top:{s(8)}px">📍 {lieu}</div></div>'''
