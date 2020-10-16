import pandas as pd

import pandas as pd
import pandas_profiling

INPUT='data/train.csv'
OUTPUT='data/report.html'

df = pd.read_csv(INPUT)

profile = pandas_profiling.ProfileReport(df)
profile.to_file(OUTPUT)
