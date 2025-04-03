#!/usr/bin/python3
from turtle import fd, bk, rt, lt, pendown, penup, exitonclick
from math import acos, asin, atan, degrees, sqrt

vyska_bez_strechy = 500
sirka = 400
strana_strechy = 300
posun_dolu_navic = 100

uhlopricka = sqrt(vyska_bez_strechy**2 + sirka**2)
uhel_uhlopricka = 90 - degrees(atan(sirka / vyska_bez_strechy))
uhel_strechy1 = degrees(acos(sirka / 2 / strana_strechy))
uhel_strechy2 = degrees(asin(sirka / 2 / strana_strechy)) * 2

# Centrování
penup()
bk(sirka/2)
rt(90)
fd(vyska_bez_strechy/2 + posun_dolu_navic)
lt(90)
pendown()

# Kreslení
lt(uhel_uhlopricka)
fd(uhlopricka)
lt(180 - uhel_uhlopricka)
fd(sirka)
lt(180 - uhel_uhlopricka)
fd(uhlopricka)
rt(180 - uhel_uhlopricka)
fd(sirka)
rt(90)
fd(vyska_bez_strechy)
rt(90 - uhel_strechy1)
fd(strana_strechy)
rt(180 - uhel_strechy2)
fd(strana_strechy)
rt(90 - uhel_strechy1)
fd(vyska_bez_strechy)

exitonclick()
