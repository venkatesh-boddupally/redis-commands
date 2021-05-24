import redis

r = redis.Redis()
r.set('name', 'hello')
name_bytes = r.get('name')
name = name_bytes.decode('utf-8')

print(name)
