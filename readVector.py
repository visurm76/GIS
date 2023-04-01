from osgeo import ogr

shapefile = ogr.Open("Тестовый_файл_фигур/shapefile.shp")
layer = shapefile.GetLayer(0)
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    id = feature.GetField("ID")
    name = feature.GetField("NAME")
    geometry = feature.GetGeometryRef()
    print(i, name, geometry.GetX(), geometry.GetY())

shapefile = None


