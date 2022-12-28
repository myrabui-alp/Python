# Calculate the date 4 months from the current date
from datetime import datetime
# import numpy as np
given_date = datetime(2020, 2, 25).date()
new_date = given_date.strftime("%Y, %m, %d")
new_date = new_date[:7] + "6" + new_date[8:]
print(new_date)
print(datetime.strptime(new_date, "%Y, %m, %d"))
