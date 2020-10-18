from EcoleIotRedis import r
from DataLoader import DataLoader


dataLoader = DataLoader("Exterieur_12_10_2020.csv")
data = dataLoader.load(header=True)

for d in data:
    #max
    max = r.get("ext:temperature:max")
    if max is None or float(d[2]) > float(max):
        r.set("ext:temperature:max", d[2])
    #min
    min = r.get("ext:temperature:min")
    if min is None or float(d[2]) < float(min):
        r.set("ext:temperature:min", d[2])