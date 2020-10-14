from EcoleIotRedis import r
import DataLoader


dataLoader = DataLoader("Exterieur_12_10_2020.csv")
data = dataLoader.load()

r.set("ext:line:count", data.size())