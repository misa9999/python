from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays


setlocale(LC_ALL, "en_US.UTF-8")

dt = datetime.now()
month = int(dt.strftime("%m"))
format_dt = dt.strftime("%A, %B %d, %Y")
format_dt2 = dt.strftime("%d/%m/%Y %H:%M:%S")
print(format_dt)
print(format_dt2)

print()
print(mdays[month])
