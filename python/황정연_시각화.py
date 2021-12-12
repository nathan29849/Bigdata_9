import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df1 = pd.read_excel("의존율_사하라이남.xlsx")
df1.columns = np.arange(31)
country_name = df1[0]
df1.index = country_name
df1 = df1.drop(columns = [0])

df1.columns = np.arange(1990,2020)

fig = plt.figure(figsize=(30,30))
fig.set_facecolor('white')

plt.pcolor(df1.values, cmap='Reds')
plt.xticks(range(len(df1.columns)),df1.columns)
plt.yticks(range(len(df1.index)),df1.index)
plt.colorbar()
plt.show()

#위에거 다 주석처리하고 아래거 주석처리 풀 것

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt 

# df1 = pd.read_excel("의존율_사하라이남_제외.xlsx") 
# df1.columns = np.arange(31)
# country_name = df1[0]
# df1.index = country_name
# df1 = df1.drop(columns = [0])

# df1.columns = np.arange(1990,2020)

# fig = plt.figure(figsize=(30,31))
# fig.set_facecolor('white')

# plt.pcolor(df1.values, cmap='Reds')
# plt.xticks(range(len(df1.columns)),df1.columns)
# plt.yticks(range(len(df1.index)),df1.index)
# plt.colorbar()
# plt.show()