from datetime import datetime, timedelta

# date = datetime.strptime("05/10/2020", "%d/%m/%Y")

d1 = datetime.strptime("20/04/1900 20:00:00", "%d/%m/%Y %H:%M:%S")
d2 = datetime.strptime("25/04/1900 22:33:00", "%d/%m/%Y %H:%M:%S")

dif = d2 - d1
print(dif)

# date = datetime.strptime("20/04/1900 20:00:00", "%d/%m/%Y %H:%M:%S")
# date += timedelta(days=5, seconds=50)
# print(date.strftime("%d/%m/%Y %H:%M:%S"))
# date = datetime.fromtimestamp(1601866800.0)
# print(date)
# print(date.timestamp())
# date = datetime(2020, 10, 5, 9, 50, 10)
# print(date.strftime('%d/%m/%Y %H:%M:%S'))
