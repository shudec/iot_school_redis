from EcoleIotRedis import r
from DataLoader import DataLoader

r.flushall()

dataLoader = DataLoader("Exterieur_12_10_2020.csv")
data = dataLoader.load(header=True)

r.set("ext:line:count", len(data))