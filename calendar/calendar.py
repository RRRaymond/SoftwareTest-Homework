# -*- coding: UTF-8 -*-
import time
import datetime
import sys

a = sys.argv[1]
t = time.strptime(a, "%Y-%m-%d")
y, m, d = t[0:3]
print(datetime.date(y, m, d) + datetime.timedelta(days=1))
