from datetime import datetime
import math
from EcoleIotRedis import r
from DataLoader import DataLoader


dataLoader = DataLoader("Exterieur_12_10_2020.csv")
data = dataLoader.load(header=True)

r.delete('ext:temperatures:month:1')
r.delete('ext:temperatures:month:2')
r.delete('ext:temperatures:month:3')
r.delete('ext:temperatures:month:4')
r.delete('ext:temperatures:month:5')
r.delete('ext:temperatures:month:6')
r.delete('ext:temperatures:month:7')
r.delete('ext:temperatures:month:8')
r.delete('ext:temperatures:month:9')
r.delete('ext:temperatures:month:10')

data_by_month = []

for d in data:
    m = datetime.fromtimestamp(int(d[0])).month
    r.lpush("ext:temperatures:month:"+str(m), d[2])

    #calculate the mean
    temps_of_month = [float(temp) for temp in r.lrange("ext:temperatures:month:"+str(m), 0, -1)]
    mean_of_month = sum(temps_of_month) / len(temps_of_month)

    r.set("ext:temperatures:month:mean:"+str(m), mean_of_month)

print(r.lrange("ext:temperatures:month:1",0,-1))