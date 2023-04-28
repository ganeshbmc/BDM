import pandas as pd
exp = [5,5,5.5,6]
skill = [2,1,1,1]
proj = [2,1,2,1]
avail = [2,2,2,3]

df = pd.DataFrame(zip(exp, skill, proj, avail))
df.columns = ['exp', 'skill', 'proj', 'avail']
df.index=['p', 's', 'a', 'l']
# print(df)

df = df/df.max()
# print(df)

df['composite'] = df[['exp', 'skill', 'proj']].sum(axis=1) - df['avail']
# print(df)

df['rank'] = df['composite'].rank(ascending=False)
print(df)
