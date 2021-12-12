import numpy as np
import pandas as pd

boonja = pd.read_excel("원자재.xlsx", engine="openpyxl")
boonmo = pd.read_excel("전체.xlsx", engine="openpyxl")

SubSahara = ["Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Congo", "Côte d'Ivoire", "Djibouti", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia",
             "Ethiopia (+ Eritrea)", "Gabon", "The Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tomé and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "Sudan", "Tanzania", "Togo", "Uganda", "Zambia", "Zimbabwe"]

SubSahDF = pd.DataFrame()

boonja1 = boonja.drop([0], axis=0)
rename_col = np.array(boonja.iloc[1])
rename_col[3:] = np.array(rename_col[3:], dtype=np.int16)
boonja1.columns = rename_col

country_num = len(boonja1)

for i in range(1, country_num):
    if boonja1.iloc[i]["Reporting Economy"] in SubSahara:
        SubSahDF = SubSahDF.append(boonja1.iloc[i], ignore_index=True)

SubSahDF = SubSahDF.drop(['Product/Sector', 'Partner Economy'], axis=1)
print(SubSahDF.iloc[43])
