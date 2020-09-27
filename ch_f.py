import pandas as pd
import datetime
import os, sys

newColumnNames = {'<TICKER>' : 'Nazwa',
                  '<DATE>' : 'Data',
                  '<LOW>' : 'Low',
                  '<OPEN>' : 'Otwarcie',
                  '<HIGH>' : 'Max',
                  '<LOW>' : 'Min',
                  '<CLOSE>' : 'Zamkniecie',
                  '<VOL>' : 'Wolumen',
                  '<OPENINT>' : 'Openint'
                 }

path = 'nc_wild/'


def take_list(path):
    dirs = os.listdir(path)
    list_name = []
    for i in dirs:
        list_name.append(i.replace('.txt', ''))
    return list_name


def change_data(data):
    it=0
    res = str(data)
    year = str()
    month = str()
    day = str()
    
    for i in res:
        if it == 0:
            year = year + i
            it+=1
            continue
        if it == 1:
            year = year + i
            it+=1
            continue
        if it == 2:
            year = year + i
            it+=1
            continue
        if it == 3:
            year = year + i
            it+=1
            continue
        if it == 4:
            month+=i
            it+=1
            continue
        if it == 5:
            month+=i
            it+=1
            continue
        if it == 6:
            day+=i
            it+=1
            continue
        if it == 7:
            day+=i
            it+=1
    year = int(year)
    month = int(month)
    day = int(day)
    x = datetime.datetime(year, month, day)
    return x  

def change_files(lista, path):
    for i in lista:
        url = path+i+'.txt'
        try:
            obj = pd.read_csv(url, usecols=['<DATE>', '<OPEN>', '<CLOSE>', '<LOW>', '<HIGH>', '<VOL>'])
            obj.rename(columns=newColumnNames, inplace=True)
            for j in range(len(obj['Data'])):
                obj.iloc[j, 0] = change_data(obj.iloc[j, 0])
            obj['year']=0
            for m in range(len(obj)):
                obj.loc[m, 'year'] = int(obj['Data'][m].year)
                obj['year']= obj['year'].astype('int')
            name = 'nc_clear/'+i+'.csv'
            obj.to_csv(name)
            print(i, 'Finish')
        except:
            pass



lista = take_list(path)
change_files(lista, path)
