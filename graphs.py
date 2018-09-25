import math
import data_ini

#Increase rate depending on curve type
#Change numbers to modify performance
def increase_slope():
    graph_type = data_ini.get_graph_type()
    if graph_type == 0:
        slope = data_ini.get_linear_slope()
        if slope >= 0.8:
            slope = 0.8
        else:
            slope += 0.05
        data_ini.set_linear_slope(round(slope, 6))
    elif graph_type == 1:
        slope = data_ini.get_exponential_slope()
        slope += 15
        data_ini.set_exponential_slope(slope)
    elif graph_type == 2:
        slope = round(data_ini.get_sCurve_slope(), 6)
        slope += 0.0005
        data_ini.set_sCurve_slope(round(slope, 6))

#Decrease rate depending on curve type
#Change numbers to modify performance
def decrease_slope():
    graph_type = data_ini.get_graph_type()
    if graph_type == 0:
        slope = data_ini.get_linear_slope()
        slope -= 0.05
        data_ini.set_linear_slope(round(slope, 6))
    elif graph_type == 1:
        slope = data_ini.get_exponential_slope()
        if slope <= 15:
            slope = 15
        else:
            slope -= 15
        data_ini.set_exponential_slope(slope)
    elif graph_type == 2:
        slope = round(data_ini.get_sCurve_slope(), 6)
        if slope <= 0.0005:
            slope = 0.0005
        else:
            slope -= 0.0005
        data_ini.set_sCurve_slope(round(slope, 6))

#Calculate linear graph data from inputs
def generate_graph_data_linear():
    min_temp = data_ini.get_min_temp()
    max_temp = data_ini.get_max_temp()
    min_rpm = data_ini.get_min_rpm()
    max_rpm = data_ini.get_max_rpm()
    data_points = 1200
    slope = data_ini.get_linear_slope()
    temp_data = 0
    rpm_data = max_rpm
    temp_data_array = []
    rpm_data_array = []
    rpm_step = (max_rpm - min_rpm)/data_points

    for i in range(data_points + 1):
        if i < int(min_temp) or i > int(max_temp):
            temp_data_array.append(i)
            rpm_data_array.append('NaN')
        else:
            temp_data_array.append(i)
            rpm_data_array.append(round(rpm_data,2))
            rpm_data = (rpm_data - rpm_step) + slope
            if rpm_data <= min_rpm:
                rpm_data = min_rpm

    return temp_data_array, rpm_data_array

#Calculate exponential graph data from inputs
def generate_graph_data_exponential():
    min_temp = data_ini.get_min_temp()
    max_temp = data_ini.get_max_temp()
    min_rpm = data_ini.get_min_rpm()
    max_rpm = data_ini.get_max_rpm()
    data_points = 1200
    slope = data_ini.get_exponential_slope()
    temp_data = 0
    rpm_data = max_rpm
    temp_data_array = []
    rpm_data_array = []
    rpm_step = (max_rpm - min_rpm)/data_points
    temp_step = (max_temp - min_temp)/data_points

    for i in range(data_points + 1):
        if i < int(min_temp) or i > int(max_temp):
            temp_data_array.append(i)
            rpm_data_array.append('NaN')
        else:
            temp_data_array.append(i)
            rpm_data_array.append(round(rpm_data,2))
            temp_data += temp_step
            rpm_data = (max_rpm - min_rpm)*(0.5**((i - min_temp)/slope)) + min_rpm

    return temp_data_array, rpm_data_array

#Calculate S-Curve graph data from inputs
def generate_graph_data_sCurve():
    min_temp = data_ini.get_min_temp()
    max_temp = data_ini.get_max_temp()
    min_rpm = data_ini.get_min_rpm()
    max_rpm = data_ini.get_max_rpm()
    data_points = 1200
    slope = data_ini.get_sCurve_slope()
    temp_data = 0
    rpm_data = max_rpm
    temp_data_array = []
    rpm_data_array = []
    rpm_step = (max_rpm - min_rpm)/data_points
    temp_step = (max_temp - min_temp)/data_points

    for i in range(data_points + 1):
        if i < int(min_temp) or i > int(max_temp):
            temp_data_array.append(i)
            rpm_data_array.append('NaN')
        else:
            temp_data_array.append(i)
            rpm_data = (max_rpm - min_rpm)/(1 + 2.718**(slope*(i-((max_temp + min_temp)/2)))) + min_rpm
            rpm_data_array.append(round(rpm_data,2))
            temp_data += temp_step

    return temp_data_array, rpm_data_array
