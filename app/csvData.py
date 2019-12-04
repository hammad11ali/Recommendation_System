import pandas
result = pandas.read_csv('MetaData.csv')

df1 = result.values.tolist()

print(result.columns)
r=''
for i in range(2, len(df1[1])):
    if df1[1][i]==1:
        r= r + "  " + result.columns[i]
        
print (r)

movie={"Name": "khjsfjksh" }