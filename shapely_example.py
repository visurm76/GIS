import shapely
import shapely.speedups

"""
Следующая ниже программа создает два геометрических объекта Shapely - круг
и квадрат - и вычисляет их пересечение.
"""
import shapely.geometry
import shapely.wkt

pt = shapely.geometry.Point(0, 0)
circle = pt.buffer(1.0)
square = shapely.geometry.Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])
intersect = circle.intersection(square)
for x, y in intersect.exterior.coordsgit :
    print(x, y)
print(shapely.wkt.dumps(intersect))
