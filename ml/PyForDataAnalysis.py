import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import quandl
import pickle
style.use('ggplot')

# web_stats = {'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#              'Visitors': [43, 54, 67, 33, 34, 98, 54, 72, 11, 76, 56, 87],
#              'Bounce_rate': [65, 72, 75, 65, 87, 32, 43, 76, 65, 72, 72, 65]}

# df = pd.DataFrame(web_stats)

# print(df.head())
# print(df.tail())
# print(df.set_index('Day'))
# print(df['Visitors'])
# print(df[['Visitors', 'Bounce_rate']])
# print(df.Visitors.tolist())
# print(np.array(df[['Visitors', 'Bounce_rate']]))


# data/ZILLOW-Z7006_MLPTT.csv
# df = pd.read_csv('data/ZILLOW-Z7006_MLPTT.csv')
# # df.set_index('Date', inplace=True)
# # print(df.head())
# df.rename(columns={'Value': '77006_HPI'}, inplace=True)
# print(df.head())


# https://www.quandl.com/data/FMAC/HPI_AK-House-Price-Indices-Alaska
# api_key = open('data/quandlapikey.txt', 'r').read()
# df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
# print(df.head())


# https://simple.wikipedia.org/wiki/List_of_U.S._states
# df = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')[0]
# df.to_csv('data/List_of_U.S._states.csv', index=False)
# print(df.head())

# df = pd.read_csv('data/List_of_U.S._states.csv', header=1)
# df = df[['Name &postal abbreviation[1]', 'Name &postal abbreviation[1].1', 'Capital', 'Largest[5]',
#          'Established[upper-alpha 1]']]
# df.rename(columns={'Name &postal abbreviation[1]': 'Name', 'Name &postal abbreviation[1].1': 'Abbreviation',
#                    'Largest[5]': 'Largest', 'Established[upper-alpha 1]': 'Established'}, inplace=True)

# print(df.head())
# print(df.loc[:, 'Abbreviation'])
# print(df.iloc[:, 1])

# api_key = open('data/quandlapikey.txt', 'r').read()
#
#
# def state_list():
#     fs = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states',
#                       skiprows=[0],
#                       header=[0])[0]
#     return fs.iloc[:, 1]
#
#
# def grab_initial_state_data():
#     states = state_list()
#     main_df = pd.DataFrame()
#
#     for abbv in states:
#         query = 'FMAC/HPI_' + str(abbv)
#         df = quandl.get(query, authtoken=api_key)
#         df = df.pct_change()
#         # df.rename(columns={'Value': str(abbv)}, inplace=True)
#         df.rename(columns={'NSA Value': str(abbv) + ' NSA Value', 'SA Value': str(abbv) + ' SA Value'}, inplace=True)
#         if main_df.empty:
#             main_df = df
#         else:
#             main_df = main_df.join(df)
#
#     print(main_df.head())
#
#     pickle_out = open('data/fiddy_states.pickle', 'wb')
#     pickle.dump(main_df, pickle_out)
#     pickle_out.close()


# grab_initial_state_data()

# pickle_in = open('data/fiddy_states.pickle', 'rb')
# HPI_data = pickle.load(pickle_in)
# print(HPI_data)
# HPI_data.to_pickle('data/pickle.pickle')
# HPI_data2 = pd.read_pickle('data/pickle.pickle')
# print(HPI_data2)

# HPI_data2.plot()
# plt.legend().remove()
# plt.show()


# df1 = pd.DataFrame({
#     'HPI': [80, 85, 88, 85],
#     'Ind_rate': [2, 3, 2, 2],
#     'US_GDP_Thousands': [50, 55, 65, 55]
# }, index=[2001, 2002, 2003, 2004])
#
# df2 = pd.DataFrame({
#     'HPI': [80, 85, 88, 85],
#     'Ind_rate': [2, 3, 2, 2],
#     'US_GDP_Thousands': [50, 55, 65, 55]
# }, index=[2005, 2006, 2007, 2008])
# df3 = pd.DataFrame({
#     'HPI': [80, 85, 88, 85],
#     'Ind_rate': [7, 8, 9, 6],
#     'Low_tear_HPI': [50, 52, 50, 53]
# }, index=[2009, 2010, 2011, 2012])

# concat = pd.concat([df1, df2, df3])
# print(concat)

# df4 = df1.append(df2)
# print(df4)

# s = pd.Series([80, 2, 50], index=['HPI', 'Ind_rate', 'US_GDP_Thousands'])
# df5 = df1.append(s, ignore_index=True)
# print(df5)

# print(pd.merge(df1, df2, on='HPI'))
# print(pd.merge(df1, df2, on=['HPI', 'Ind_rate']))

# df1.set_index('HPI', inplace=True)
# df3.set_index('HPI', inplace=True)
# joined = df1.join(df3)
# print(joined)

# data = pd.read_json('data/Untitled.json', )

import json

d = {}

with open('/Users/aleksandr/Desktop/Untitled.json', 'r', encoding='utf-8') as read_file:
    data = json.load(read_file)
    for k, v in data['data'].items():
        d[k] = v
        print(k, v)
