import geocoder

addr = "Sao Paulo, Brazil"
coord = geocoder.arcgis(addr)
geo = geocoder.arcgis(addr)
print(geo.latlng)
print(geo)

geo2 = geocoder.arcgis([-23.562859999999944, -46.65465999999998], method="reverse")
print("\n Teste com coordenadas \n")
print(geo2)
print("\n \n")

