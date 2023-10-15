from faker import Faker
import random
import datetime

fake = Faker('en_IN')

order_date = datetime.datetime.strptime(fake.date(), "%Y-%m-%d")
required_date = order_date+datetime.timedelta(days=10)
print(fake.date_between(order_date, required_date))
# for i in range(10):
#     print(random.randint(110, 998)/100)

print(datetime.datetime.today())
print(datetime.datetime.strptime(fake.date(), "%Y-%m-%d"))

p = fake.profile()
print(p)
print(p['job'])
print(p['sex'])