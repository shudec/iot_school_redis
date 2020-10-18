from redis import Redis

r = Redis(host='localhost', port=6379, db=0, password=None, decode_responses=True)