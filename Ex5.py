from datetime import datetime
import math
from EcoleIotRedis import r
from DataLoader import DataLoader


dataLoader = DataLoader("Exterieur_12_10_2020.csv")
data = dataLoader.load(header=True)

data_by_month = []

for d in data:
    strday = d[1][1:11]
    day_score = int(datetime.fromtimestamp(int(d[0])).strftime("%Y%m%d"))
    r.zadd("ext:days", {strday:day_score})

print("nb days in file = {}".format(len(r.zrange("ext:days", 0, -1))))
print("10 first days in file = {}".format(r.zrange("ext:days", 0, 9)))
print("10 first days in file = {}".format(r.zrange("ext:days",-10, -1)))
print("10 first days in file = {}".format(r.zrange("ext:days",10, 20)))