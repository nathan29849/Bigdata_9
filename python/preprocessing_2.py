import pandas as pd

raw = pd.read_csv('./WtoDataCSV/WtoDataCSV.csv', encoding='latin1', low_memory=False)
temp_column = ['Indicator', 'Reporting Economy', 'Product/Sector', 'Partner Economy', 'Value', 'Year', 'Unit Code', 'Indicator Code']

# 칼럼 걸러내기 : Indicator | Reporting Economy | Partner Economy | Product/Sector | Year | Value
df = raw.loc[:, temp_column]

# Partner Economy == World 골라내기 및 Product/Sector 골라내기 
df = df.loc[df['Partner Economy'] == 'World']
condition_1 = df['Product/Sector'] == 'Total merchandise'
condition_2 = df['Product/Sector'] == 'Fuels and mining products'
df = df.loc[condition_1 | condition_2]

# Year == 1990 ~ 2019 외 행 제거
condition_3 = df['Year'] >= 1990
condition_4 = df['Year'] < 2020
df = df.loc[condition_3 & condition_4]

# Partner Economy == World 골라내기 및 Product/Sector 골라내기
condition_5 = df['Unit Code'] == 'USM'
condition_6 = df['Indicator Code'] == 'ITS_MTV_AX'
df = df.loc[condition_5 & condition_6]
 
# Reporting Economy | Partner Economy | Product/Sector | Value per Year 
pivot_df = df.pivot(index=['Reporting Economy', 'Product/Sector', 'Partner Economy'], \
    columns='Year', values='Value')

df = pivot_df
df.reset_index(inplace = True)
# df.set_index('index', inplace=True)

print(df.head())

# Product/Sector : Total merchandise, Fuels and mining products
condition_7 = df['Product/Sector'] == 'Total merchandise'
condition_8 = df['Product/Sector'] == 'Fuels and mining products'
total_df = df.loc[condition_7]
fuels_and_mining_df = df.loc[condition_8]

total_df.reset_index(inplace=True)
total_df.set_index('index', inplace=True)

fuels_and_mining_df.reset_index(inplace=True)
fuels_and_mining_df.set_index('index', inplace=True)

    
total_df.to_excel('total_df.xlsx', index=False)
fuels_and_mining_df.to_excel('fuels_and_mining_df.xlsx', index=False)