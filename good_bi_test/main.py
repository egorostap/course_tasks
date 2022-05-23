import pandas as pd
df = pd.read_csv('keywords.csv', delimiter=';', quotechar="'")

for i in range(len(df['Keyword'])):

    df.loc[i, 'Keyword'] = " ".join(x for x in df.loc[i, 'Keyword'].split() if not x.startswith("-"))
    df.loc[i, 'Keyword'].replace('[', '')
    df.loc[i, 'Keyword'].replace(']', '')

df['Keyword_x'] = ''
df['AdGroupId_x'] = ''
df['Keyword_y'] = ''
df['AdGroupId_y'] = ''
df['crossed'] = ''

for i in range(len(df.Keyword.values)):

    my_set = set()
    Keyword_x = ''
    AdGroupId_x = ''
    Keyword_y = ''
    AdGroupId_y = ''

    for j in range(i + 1, len(df.Keyword.values)):
        if len(set(df.Keyword[i].split()).intersection(set(df.Keyword[j].split()))) >= 2 and df.AdGroupId[i] != df.AdGroupId[j]:
            my_set.update(set(df.Keyword[i].split()).intersection(set(df.Keyword[j].split())))
            Keyword_x = df.Keyword[i]
            AdGroupId_x = df.AdGroupId[i]
            Keyword_y = df.Keyword[j]
            AdGroupId_y = df.AdGroupId[j]

    df.loc[i, 'crossed'] = str(', '.join(my_set))
    df.loc[i, 'Keyword_x'] = str(Keyword_x)
    df.loc[i, 'AdGroupId_x'] = str(AdGroupId_x)
    df.loc[i, 'Keyword_y'] = str(Keyword_y)
    df.loc[i, 'AdGroupId_y'] = str(AdGroupId_y)

print(df)
df.to_csv('keywords_ext.csv', index=False)
