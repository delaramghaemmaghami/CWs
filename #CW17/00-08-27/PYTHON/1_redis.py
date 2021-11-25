import redis


r = redis.Redis(db=3)
# ping = r.ping()
# print(ping)

# r.set("user:1", "delaram")
# x = r.get("user:1")
# print(x)
# print(x.decode("UTF-8"))

# r.mset({"name": "delaram", "age": 23, "city": "tehran"})
# name = r.get("name")
# age = r.get("age")
# city = r.get("city")
# print(name.decode("UTF-8"), age.decode("UTF-8"), city.decode("UTF-8"))
