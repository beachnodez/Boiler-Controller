import atexit
import eventlet
eventlet.monkey_patch()
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from flask import Flask, render_template, url_for, redirect, session
from flask_socketio import SocketIO, emit, disconnect
from datetime import datetime
import graphs
import data_ini
import numpy as np

DEGREES_FAREN = u"\u00b0" + 'F'
threads = ThreadPoolExecutor(1)

async_mode = None
app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

#Find source
def find_nearest(array, value):
    array = np.asarray(array)
    index = (np.abs(array - value)).argmin()
    return index

#Index route
@app.route('/')
def tempURL():
    return redirect(url_for('boiler'))

#Parameters route
@app.route('/boiler_parameters')
def boiler_parameters():
    return render_template('boiler_parameters.html')

#Main page route
@app.route('/boiler')
def boiler():
    return render_template('boiler.html')

#Get thermocouple data from ini and update UI
def update_temp_rpm():
    fire_temp = 'Fire Temp: ' + str(data_ini.get_firebox_temp()) + DEGREES_FAREN
    water_temp = 'Water Temp: ' + str(data_ini.get_steambox_temp()) + DEGREES_FAREN
    rpm = 'Rpm: ' + str(data_ini.get_rpm())
    socketio.emit('tempRpmData', {'fireTemp': fire_temp, 'waterTemp': water_temp, 'rpm': rpm}, namespace='/test', broadcast=True)

#Handle for params button event
@socketio.on('edit_params_event', namespace='/test')
def edit_params():
    print(url_for('boiler_parameters'))
    socketio.emit('redirectParams', {'url': url_for('boiler_parameters')}, namespace='/test', broadcast=True)
    update_params_page()

#Handle for connect event
@socketio.on('connect_event', namespace='/test')
def connect():
    update_params_page()
    update_graph()

#Handle for linear button event
@socketio.on('linear_graph_event', namespace='/test')
def linear_graph():
    data_ini.set_graph_type(0)
    update_graph()

#Handle for exponential button event
@socketio.on('exponential_graph_event', namespace='/test')
def exponential_graph():
    data_ini.set_graph_type(1)
    update_graph()

#Handle for S-Curve button event
@socketio.on('sCurve_graph_event', namespace='/test')
def sCurve_graph():
    data_ini.set_graph_type(2)
    update_graph()

#Handle for increase rate button event
@socketio.on('increase_slope_event', namespace='/test')
def increment_slope():
    graphs.increase_slope()
    update_graph()

#Handle for decrease rate button event
@socketio.on('decrease_slope_event', namespace='/test')
def decrement_slope():
    graphs.decrease_slope()
    update_graph()

#Handle for increase minimum temperature button event
@socketio.on('increase_min_temp_event', namespace='/test')
def increase_min_temp():
    print('here')
    temp = data_ini.get_min_temp()
    temp = temp + 10
    data_ini.set_min_temp(temp)
    update_params_page()

#Handle for decrease minimum temperature button event
@socketio.on('decrease_min_temp_event', namespace='/test')
def decrease_min_temp_event():
    print('here')
    temp = data_ini.get_min_temp()
    temp = temp - 10
    data_ini.set_min_temp(temp)
    update_params_page()

#Handle for increase maximum temperature button event
@socketio.on('increase_max_temp_event', namespace='/test')
def increase_max_temp_event():
    print('here')
    temp = data_ini.get_max_temp()
    temp = temp + 10
    data_ini.set_max_temp(temp)
    update_params_page()

#Handle for decrease maximum temperature button event
@socketio.on('decrease_max_temp_event', namespace='/test')
def decrease_max_temp_event():
    print('here')
    temp = data_ini.get_max_temp()
    temp = temp - 10
    data_ini.set_max_temp(temp)
    update_params_page()

#Handle for increase minimum rpm button event
@socketio.on('increase_min_rpm_event', namespace='/test')
def increase_min_rpm_event():
    print('here')
    temp = data_ini.get_min_rpm()
    temp = temp + 10
    data_ini.set_min_rpm(temp)
    update_params_page()

#Handle for decrease minimum rpm button event
@socketio.on('decrease_min_rpm_event', namespace='/test')
def decrease_min_rpm_event():
    print('here')
    temp = data_ini.get_min_rpm()
    temp = temp - 10
    data_ini.set_min_rpm(temp)
    update_params_page()

#Handle for increase maximum rpm button event
@socketio.on('increase_max_rpm_event', namespace='/test')
def increase_max_rpm_event():
    print('here')
    temp = data_ini.get_max_rpm()
    temp = temp + 10
    data_ini.set_max_rpm(temp)
    update_params_page()

#Handle for decrease maximum rpm button event
@socketio.on('decrease_max_rpm_event', namespace='/test')
def decrease_max_rpm_event():
    print('here')
    temp = data_ini.get_max_rpm()
    temp = temp - 10
    data_ini.set_max_rpm(temp)
    update_params_page()

#Update graph depending on selected line type
def update_graph():
    graph_type = data_ini.get_graph_type()
    if graph_type == 0:
        curveType = 'Linear Ramp'
        temperature_graph_data, rpm_graph_data = graphs.generate_graph_data_linear()

    elif graph_type == 1:
        curveType = 'Exponential Ramp'
        temperature_graph_data, rpm_graph_data = graphs.generate_graph_data_exponential()

    elif graph_type == 2:
        curveType = 'S-Curve Ramp'
        temperature_graph_data, rpm_graph_data = graphs.generate_graph_data_sCurve()

    current_temp = data_ini.get_firebox_temp()
    index_closest = find_nearest(temperature_graph_data, current_temp)
    y_point = rpm_graph_data[index_closest]
    data_ini.set_rpm(y_point)
    point_array = []

    for i in range(len(temperature_graph_data)):
        point_array.append('NaN')

    point_array[index_closest] = y_point
    socketio.emit('tempGraphData', {'temps': temperature_graph_data, 'rpms': rpm_graph_data, 'type': curveType, 'pointArray': point_array}, namespace='/test', broadcast=True)
    update_temp_rpm()

#Get ini data and push to UI
def update_params_page():
    min_temp = str(data_ini.get_min_temp()) + DEGREES_FAREN
    max_temp = str(data_ini.get_max_temp()) + DEGREES_FAREN
    min_rpm = str(data_ini.get_min_rpm())
    max_rpm = str(data_ini.get_max_rpm())

    socketio.emit('updateParams', {'minTemp': min_temp,
                                   'maxTemp': max_temp,
                                   'minRpm': min_rpm,
                                   'maxRpm': max_rpm},
                                   namespace='/test',
                                   broadcast=True)


#This section is for testing refer to boiler_control_gpio.py for actual control I/O
def travel():
    x = 0
    const_time = 1.0
    delta = 0.0
    while True:
        data_ini.set_firebox_temp(x)
        x += 2
        update_graph()

#end testing

if __name__ == '__main__':

    #thread1 = threads.submit(travel)
    socketio.run(app)
