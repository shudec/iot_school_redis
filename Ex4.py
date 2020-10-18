from datetime import datetime
import math
from EcoleIotRedis import r
from DataLoader import DataLoader


dataLoader = DataLoader("Exterieur_12_10_2020.csv")
data = dataLoader.load(header=True)

data_by_month = []

for d in data:
    m = datetime.fromtimestamp(int(d[0])).month
    r.lpush("ext:temperatures:month:"+str(m), d[2])

    #calculate the mean
    temps_of_month = [float(temp) for temp in r.lrange("ext:temperatures:month:"+str(m), 0, -1)]
    mean_of_month = sum(temps_of_month) / len(temps_of_month)

    r.set("ext:temperatures:month:mean:"+str(m), mean_of_month)