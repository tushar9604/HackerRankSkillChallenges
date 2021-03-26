from math import atan,sin,pi
ab,bc = int(input()),int(input())
ac = (ab**2 + bc**2)**0.5
mc = ma = ac/2
angle_bca = atan(ab/bc)
angle_bac = atan(bc/ab)
me = mc*sin(angle_bca)
mf = ma*sin(angle_bac)
x = atan(me/mf)*(180/pi)
print(round(x),'°',sep='')