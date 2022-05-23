import csv
import pandas as pd
with open('keywords.csv', 'r') as file:
    keywords_reader = csv.DictReader(file, delimiter=';', quotechar="'")

    for row in keywords_reader:
        row["Keyword"] = " ".join(x for x in row["Keyword"].split() if not x.startswith("-"))
        row["Keyword"].replace('[', '')
        row["Keyword"].replace(']', '')

#        print(row, type(row["Keyword"]))

print(keywords_reader)


###test test test###


#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', None)

#    print(df.crossed[i])
#    print(df.AdGroupId_y[i])
#    print(df.Keyword_x[i])
#    print(df.AdGroupId_x[i])
#    print(df.Keyword_y[i])
#    print(df.AdGroupId_y[i])
#    df = df.append(df.AdGroupId_y[i])

#for i in range(len(df.Keyword.values)):
#    www = ' '
#    print(df.Keyword[i])
#    for j in range(i + 1, len(df.Keyword.values)):
#        www = df.apply(lambda x: set(df.Keyword[i].split().interspection(set(df.Keyword[i].split()), axis = 1)
#    print(df)

#print(df)

#print(df['Keyword'])

#x = df.Keyword[i]
#for i in range(len(df.Keyword.values)):
#    for j in range(i + 1, len(df.Keyword.values)):
#        df['crossed'] = df.apply(lambda x: x[i].interspection(x[j]), axis = 1)
#        print(df)


#for i in range(len(df.Keyword.values)):
#    www = ' '
#    for j in range(i + 1, len(df.Keyword.values)):
#        if len(set(df.Keyword[i].split()).intersection(set(df.Keyword[j].split()))) >= 2:
#            www += ' '.join(set(df.Keyword[i].split()).intersection(set(df.Keyword[j].split())))
#    df.Keyword[i] = www
#    print(df.Keyword[i])


#        if len(set(df.Keyword[i].split()).intersectionset(df.Keyword[j].split())) >= 2:
#            print(i)
#print(df.Keyword)
#df['k'] = [x[0].intersection(x[1])  for x in df.iloc['Keyword']]
#print (df)

#print(df) if len(x[0].intersection(x[1])) >= 2             df = df.drop(i,0)



#df['crossed'] = crossed



#    for row in keywords_reader:
#        row["Keyword"] = " ".join(x for x in row["Keyword"].split() if not x.startswith("-"))
#        row["Keyword"].replace('[', '')
#        row["Keyword"].replace(']', '')

#        print(row, type(row["Keyword"]))

#print(keywords_reader)

