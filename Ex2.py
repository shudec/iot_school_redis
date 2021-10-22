from EcoleIotRedis import r
from DataLoader import DataLoader


dataLoader = DataLoader("Exterieur_12_10_2020.csv")
data = dataLoader.load(header=True)

r.delete('ext:timestamps')
r.delete('ext:temperatures')
r.delete('ext:alldata')

for d in data:
    #method 1
    r.rpush("ext:timestamps", d[0])
    r.rpush("ext:temperatures", d[2])
    #method 2
    r.sadd("ext:alldata", "{},{}".format(d[0],d[2]))