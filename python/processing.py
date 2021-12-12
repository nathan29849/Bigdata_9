import pandas as pd

raw = pd.read_excel('WtoData.xlsx')

# column 이름 바꾸기
year = []
for i in range(1948, 2021):
    year.append(str(i))
columns_title = ['ReporingEconomy', 'Product/Sector', 'PartnerEconomy'] + year
raw.columns = columns_title

# 의미없는 row 삭제
raw = raw.iloc[2:]

# 연도 전처리 (1990 ~ 2019)
year = []
for i in range(1990, 2020):
    year.append(str(i))    
filter_temp = ['ReporingEconomy', 'Product/Sector', 'PartnerEconomy'] + year
df = raw.loc[:, filter_temp]

# Product/Sector 에서 SI3_AGG - TO - Total merchandise 인 부분(행)만 골라내기
total_df = df.loc[df['Product/Sector'] == 'SI3_AGG - TO - Total merchandise']

# Product/Sector 에서 SI3_AGG - MI - Fuels and mining products 인 부분(행)만 골라내기
fuels_and_mining_df = df.loc[df['Product/Sector'] == 'SI3_AGG - MI - Fuels and mining products']
print(fuels_and_mining_df)
