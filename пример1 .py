sx = int(input())
sy = int(input())
sz = int(input())

bx = int(input())
by = int(input())
bz = int(input())

vmax = 0

v = (sx // bx) * (sy // by) * (sz // bz)
if v > vmax:
    vmax = v

v = (sx // bz) * (sy // bx) * (sz // by)
if v > vmax:
    vmax = v

v = (sx // by) * (sy // bz) * (sz // bx)
if v > vmax:
    vmax = v

v = (sx // by) * (sy // bx) * (sz // bz)
if v > vmax:
    vmax = v

v = (sx // bz) * (sy // by) * (sz // bx)
if v > vmax:
    vmax = v

v = (sx // bx) * (sy // bz) * (sz // by)
if v > vmax:
    vmax = v

print(vmax)
