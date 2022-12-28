# Calculate number of days between two given dates
from datetime import datetime
# 2020-02-25
date_1 = datetime(2020, 2, 25)

# 2020-09-17
date_2 = datetime(2020, 9, 17)

range = date_2 - date_1
if date_2 > date_1:
    print(range.days, "days")
else:
    print(-range.days, "days")
