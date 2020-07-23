v = int(input())
t = int(input())
if v >= 0 and v * t <= 109:
    print(v * t)
if v > 0 and v * t > 109:
    print(v * t % 109)
if v < 0 and v * t >= -109:
    print(109+(v * t))
if v < 0 and v * t < -109:
    print(109 - (v * t % 109))



