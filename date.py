import datetime as dt

print(dt.date.today())
t = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(t)

t1 = dt.date(3024,8,15)
t2 = dt.date.today()
print(t1-t2)