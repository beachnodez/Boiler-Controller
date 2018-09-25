import configparser
config = configparser.ConfigParser()

def get_graph_type():
    config.read('data.ini')
    return int(config.get('GRAPH_DATA', 'graph_type'))

def set_graph_type(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'graph_type', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_linear_slope():
    config.read('data.ini')
    return float(config.get('GRAPH_DATA', 'linear_slope'))

def set_linear_slope(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'linear_slope', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_exponential_slope():
    config.read('data.ini')
    return float(config.get('GRAPH_DATA', 'exponential_slope'))

def set_exponential_slope(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'exponential_slope', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_sCurve_slope():
    config.read('data.ini')
    return float(config.get('GRAPH_DATA', 'scurve_slope'))

def set_sCurve_slope(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'scurve_slope', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_firebox_temp():
    config.read('data.ini')
    return float(config.get('TEMP_DATA', 'fire_box'))

def set_firebox_temp(value):
    config.read('data.ini')
    config.set('TEMP_DATA', 'fire_box', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_steambox_temp():
    config.read('data.ini')
    return float(config.get('TEMP_DATA', 'steam_box'))

def set_steambox_temp(value):
    config.read('data.ini')
    config.set('TEMP_DATA', 'steam_box', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_min_temp():
    config.read('data.ini')
    return float(config.get('GRAPH_DATA', 'min_temp'))

def set_min_temp(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'min_temp', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_max_temp():
    config.read('data.ini')
    return float(config.get('GRAPH_DATA', 'max_temp'))

def set_max_temp(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'max_temp', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_min_rpm():
    config.read('data.ini')
    return float(config.get('GRAPH_DATA', 'min_rpm'))

def set_min_rpm(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'min_rpm', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_max_rpm():
    config.read('data.ini')
    return float(config.get('GRAPH_DATA', 'max_rpm'))

def set_max_rpm(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'max_rpm', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)

def get_rpm():
    config.read('data.ini')
    return float(config.get('GRAPH_DATA', 'rpm'))

def set_rpm(value):
    config.read('data.ini')
    config.set('GRAPH_DATA', 'rpm', str(value))
    with open('data.ini', 'w') as datafile:
        config.write(datafile)
