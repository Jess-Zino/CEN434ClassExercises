import pandas  as pd
import numpy as np
df = pd.read_csv('Book1.csv')
a = df.to_numpy()
a = np.array(df).reshape(3,3)
print(a) 