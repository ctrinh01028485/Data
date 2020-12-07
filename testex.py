import pandas as pd 

xl = pd.ExcelFile('trinhcong.xlsx')
df = pd.read_excel(xl, 0, header=None)

for i in range(2, 12):
    print(df.at[i, 11], '\t\t', df.at[i, 12])
""" 171.244.166.18
113.185.76.196
 """
 