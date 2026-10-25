from common import *
W,H=1080,1350
def frame(inner,num=None,total=None,swipe=True):
    n=f'<div style="position:absolute;top:70px;right:70px;font-size:26px;color:#999;font-weight:500">{num}/{total}</div>' if num else ''
    sw='<div style="position:absolute;bottom:64px;right:70px;font-size:26px;color:#999;font-weight:500">Glisse →</div>' if swipe else ''
    return f'''<div class="glow" style="width:800px;height:800px;right:-260px;top:-300px"></div><div class="glow2" style="width:700px;height:700px;left:-260px;bottom:-280px"></div>
<div style="position:absolute;top:60px;left:70px">{BRAND}</div>{n}
<div style="position:absolute;left:70px;right:70px;top:190px;bottom:140px;display:flex;flex-direction:column;justify-content:center">{inner}</div>{sw}'''
def tip(k,total,emoji,title,body,good):
    return frame(f'''<div style="display:flex;align-items:center;gap:26px"><div style="width:120px;height:120px;border-radius:32px;background:#fdecee;display:flex;align-items:center;justify-content:center;font-size:66px">{emoji}</div>
<div class="fr red" style="font-size:120px;line-height:1">{k-1}</div></div>
<div class="fr" style="font-size:78px;line-height:1.08;margin-top:40px">{title}</div>
<div style="font-size:36px;line-height:1.45;color:#555;margin-top:30px">{body}</div>
<div class="card" style="margin-top:44px;padding:28px 32px;display:flex;gap:20px;align-items:flex-start;font-size:32px;line-height:1.4"><span style="font-size:38px">✅</span><span><b>{good}</b></span></div>''',k,total)
