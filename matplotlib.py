import matplotlib.pyplot as plt
import pandas as pd
length = pd.Series([10,20,30,40,50])
width = pd.Series([1,2,3,4,5])
df = pd.concat([length,width],axis=1)
print(df)