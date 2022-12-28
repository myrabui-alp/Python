# Calculate the date 4 months from the current date
from datetime import datetime
import pandas as pd
# import numpy as np
given_date = datetime(2020, 2, 25).date()
new_date = pd.to_datetime(given_date)+pd.DateOffset(months=4)
print(str(new_date))
