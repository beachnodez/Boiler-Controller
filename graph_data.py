#-*- coding: utf-8 -*-
import math

def get_data_from_file(filename):
    tempfile = open(filename, 'r')
    data = tempfile.read()
    tempfile.close()
    return data

def write_data_to_file(filename, data):
    f = open(filename, 'a')
    f.seek(0)
    f.truncate()
    f.write(str(data))
    f.flush()
    f.close()

def increase_slope():
    graph_type = int(get_data_from_file('graph_type.txt'))
    if graph_type == 0:
        slope = int(get_data_from_file('linear_slope.txt'))
        if slope >= 17:
            slope = 17
        else:
            slope += 1
        write_data_to_file('linear_slope.txt', slope)
    elif graph_type == 1:
        slope = int(get_data_from_file('exponential_slope.txt'))
        slope += 15
        write_data_to_file('exponential_slope.txt', slope)
    elif graph_type == 2:
        slope = round(float(get_data_from_file('sCurve_slope.txt')), 6)
        slope += 0.0005
        write_data_to_file('sCurve_slope.txt', round(slope, 6))

def decrease_slope():
    graph_type = int(get_data_from_file('graph_type.txt'))
    if graph_type == 0:
        slope = int(get_data_from_file('linear_slope.txt'))
        slope -= 1
        write_data_to_file('linear_slope.txt', slope)
    elif graph_type == 1:
        slope = int(get_data_from_file('exponential_slope.txt'))
        if slope <= 15:
            slope = 15
        else:
            slope -= 15
        write_data_to_file('exponential_slope.txt', slope)
    elif graph_type == 2:
        slope = round(float(get_data_from_file('sCurve_slope.txt')), 6)
        if slope <= 0.0005:
            slope = 0.0005
        else:
            slope -= 0.0005
        write_data_to_file('sCurve_slope.txt', round(slope, 6))

def generate_graph_data_linear():
    min_temp = 0.0
    max_temp = 1200.0
    min_rpm = 0.0
    max_rpm = 1630
    data_points = 96
    slope = float(get_data_from_file('linear_slope.txt'))
    temp_data = min_temp
    rpm_data = max_rpm
    temp_data_array = []
    rpm_data_array = []
    rpm_step = (max_rpm - min_rpm)/data_points
    temp_step = (max_temp - min_temp)/data_points

    for i in range(data_points + 1):
        temp_data_array.append(round(temp_data,2))
        rpm_data_array.append(round(rpm_data,2))
        temp_data += temp_step
        rpm_data = rpm_data - rpm_step + slope
        if rpm_data <= 0:
            rpm_data = 0

    return temp_data_array, rpm_data_array

def generate_graph_data_exponential():
    min_temp = 0.0
    max_temp = 1200.0
    min_rpm = 0.0
    max_rpm = 1630
    data_points = 96
    slope = float(get_data_from_file('exponential_slope.txt'))
    temp_data = min_temp
    rpm_data = max_rpm
    temp_data_array = []
    rpm_data_array = []
    rpm_step = (max_rpm - min_rpm)/data_points
    temp_step = (max_temp - min_temp)/data_points

    for i in range(data_points + 1):
        temp_data_array.append(round(temp_data,2))
        rpm_data_array.append(round(rpm_data,2))
        temp_data += temp_step
        rpm_data = max_rpm*(0.5**(temp_data/slope))

    return temp_data_array, rpm_data_array

def generate_graph_data_sCurve():
    min_temp = 0.0
    max_temp = 1200.0
    min_rpm = 0.0
    max_rpm = 1630
    data_points = 96
    slope = float(get_data_from_file('sCurve_slope.txt'))
    temp_data = min_temp
    rpm_data = max_rpm
    temp_data_array = []
    rpm_data_array = []
    rpm_step = (max_rpm - min_rpm)/data_points
    temp_step = (max_temp - min_temp)/data_points

    for i in range(data_points + 1):
        temp_data_array.append(round(temp_data,2))
        rpm_data = (max_rpm)/(1 + 2.718**(slope*(temp_data-(max_temp/2))))
        rpm_data_array.append(round(rpm_data,2))
        temp_data += temp_step

        #rpm_data = (max_rpm/2)*math.cos(temp_data*0.5) + (max_rpm/2)

    return temp_data_array, rpm_data_array
