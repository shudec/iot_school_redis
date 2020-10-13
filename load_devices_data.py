from datetime import datetime
from redis import Redis

r = Redis(host='localhost', port=6379, db=0, password=None)

#open data file
try:
    #data_file = open("devices.data", mode='r', encoding='utf-8')
    data_file = open("Exterieur_12_10_2020.csv", mode='r', encoding='utf-8')
    for line in data_file:
            data = line.split(';')
            #print(data)
            r.set("ext:"+data[0], line[:-1])
finally:
    data_file.close


