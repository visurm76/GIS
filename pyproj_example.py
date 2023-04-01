"""
Следующий ниже пример начинается с указания географического положения
в координатах 17-й зоны проекции Меркатора (UTM) и затем при помощи двух
объектов Proj, один с заданной 17-й зоной UTM и другой с координатной про
екцией (широта и долгота), выполняет перевод прямоугольных координат этого
географического положения в значения широты и долготы:

"""

import pyproj

UTM_X = 565718.523517
UTM_Y = 3980998.9244

srcProj = pyproj.Proj(proj="utm", zone="17", ellps="clrk66", units="m")
dstProj = pyproj.Proj(proj='longlat', ellps='WGS84', datum='WGS84')
long, lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)
print("Координата 17-й зоны UTM " + " ({:.4f}, {:.4f}) ".format(UTM_X, UTM_Y) + "= {:.4f}, {:.4f}".format(long, lat))

"""
Второй пример принимает эти расчетные значения широты и долготы и при по
мощи объекта Geod вычисляет еще одну точку в 10 км к северо-востоку от этого
географического положения
"""

angle = 315  # 315 градусов = северо-восток
distance = 10000
geod = pyproj.Geod(ellps='clrk66')
long2, lat2, invAngle = geod.fwd(long, lat, angle, distance)

print("Координата {:.4f}, {:.4f}" .format(lat2, long2) + " находится в 10 км к северо-востоку от " +\
"{:.4f}, {:.4f}".format(lat, long))
