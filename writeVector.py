import os, shutil, random
from osgeo import ogr, osr

if os.path.exists ("Тестовый_файл_фигур"):
    shutil.rmtree("Тестовый_файл_фигур")
os.mkdir("Тестовый_файл_фигур")

"""
Как и с библиотекой GDAL, мы сначала выбираем драйвер, который
соответствует типу источника данных, который мы хотим создать, и затем пору­
чаем драйверу создать источник данных.
"""
driver = ogr.GetDriverByName('ESRI Shapefile')
path = os.path.join("Тестовый_файл_фигур", "shapefile. shp")
datasource = driver.CreateDataSource(path)

"""
Затем нам нужно определить слой. Для этого мы сначала определяем простран
ственную привязку для использования в наших данных
"""
spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS('WGS84')

"""
И затем можно создать непосредственно сам слой
"""

layer = datasource.CreateLayer("layer", spatialReference)

"""
нам нужно сообщить библиотеке OGR, какие атрибуты будут исполь­
зоваться и какой тип данных будет храниться
"""
field = ogr.FieldDefn("ID", ogr.OFTInteger)
field.SetWidth(4)
layer.CreateField(field)
field = ogr.FieldDefn("NAME", ogr.OFTString)
field.SetWidth(20)
layer.CreateField (field)

"""
сгенерируем 100 геометрий точки и вычислим идентификатор и имя, которые свяжем
с каждым геообъектом
"""

for i in range(100):
    id = 1000 + i
    lat = random.uniform(-90, +90)
    long = random.uniform(-180, +180)
    name = "point-{} " . format(i)
    wkt = "POINT({} {}) ".format(long, lat)
    geometry = ogr.CreateGeometryFromWkt(wkt)

    """
    Затем для каждой точки нам нужносоздать объект ogr. Feature, обозначающий пространственный объект, и сохранить
    значения геометрии и атрибутов в этом объекте
    """

    feature = ogr.Feature(layer.GetLayerDefn())
    feature.SetGeometry(geometry) # задать геометрию объекта
    feature.SetField("ID", id) # установить значения его атрибутов
    feature.SetField("NAME", name)
    """
    Наконец, нужно разместить этот объект в слое, чтобы его можно было сохранить в файле
    """
    layer.CreateFeature(feature)
    feature.Destroy() # уничтожить объект, освободив ресурсы

