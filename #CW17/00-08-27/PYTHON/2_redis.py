import redis


r = redis.Redis(db=5)
# ping = r.ping()
# print(ping)

# r.set("name", "delaram")
# x = r.get("name")
# print(x)
# print(x.decode("UTF-8"))

# r.mset({"user1": "delaram", "user2": "RM"})
# x = r.get("user1").decode("UTF-8")
# z = r.get("user2").decode("UTF-8")
# print(x, z)

# from datetime import timedelta
# r.setex("timer", timedelta(seconds=30), value="HEY THERE!")
# print(r.ttl("timer"))

# r.rpush("names", "delaram")
# r.rpush("names", "RM")
# r.rpush("names", "Jhope")
# print(r.lrange(0, -1))

# for i in range(10):
#     r.lpush("numbers", i)
# print(r.lrange("numbers", 0, -1))

# import datetime
# today = datetime.date.today()  # defines the date of today
# visitors = {"zahra", "elham", "samaneh"}  # defines a set with some names in it
# stoday = today.isoformat()  # converting today date to iso format
# r.sadd(stoday, *visitors)
# a = r.smembers(stoday)
# print(a)

# import json
# restaurant = {
#     "name": "deli",
#     "type": "Persian",
#     "address": {
#         "street": {
#             "line1": "11 E 30th St",
#             "line2": "APT 1",
#         },
#         "city": "New York",
#         "state": "NY",
#         "zip": 10016,
#     }
# }
# r.set(484272, json.dumps(restaurant))
# from pprint import pprint
# pprint(json.loads(r.get(484272)))
