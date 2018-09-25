import configparser
config = configparser.ConfigParser()
config['GRAPH_DATA'] = {'GraphType': '0',
                   'LinearSlope': '0',
                   'ExponentialSlope': '225',
                   'ScurveSlope': '0.0075'}
config['TEMP_DATA'] = {'FireBox': '75',
                       'SteamBox': '75'}
with open('data.ini', 'w') as datafile:
    config.write(datafile)

# #config.sections()
# config.read('data.ini')
# #config.sections()
# result = config['GRAPH']['GraphType']
# print(result)
