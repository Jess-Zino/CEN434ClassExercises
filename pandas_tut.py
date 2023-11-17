import pandas  as pd
import matplotlib.pyplot as plt
data ={'x':[1,2,3,4,5,6], 'y':[3,6,1,3,7,4]}
df = pd.DataFrame(data)
print(df)
plt.plot(df)
print(df.loc[[0,1]])



