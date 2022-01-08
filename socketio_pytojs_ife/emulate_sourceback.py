import numpy as np

import socketio
import serial
import threading
import time

file=open("sim_data_post.csv")
numpy_array = np.loadtxt(file, delimiter=",")


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './',
    '/img/altitude_pressure.svg': {'filename':'./img/altitude_pressure.svg','content_type': 'image/svg+xml'},
    '/img/altitude_ticks.svg': {'filename':'./img/altitude_ticks.svg','content_type': 'image/svg+xml'},
    '/img/fi_box.svg': {'filename':'./img/fi_box.svg','content_type': 'image/svg+xml'},
    '/img/fi_circle.svg': {'filename':'./img/fi_circle.svg','content_type': 'image/svg+xml'},
    '/img/fi_needle_small.svg': {'filename':'./img/fi_needle_small.svg','content_type': 'image/svg+xml'},
    '/img/fi_needle.svg': {'filename':'./img/fi_needle.svg','content_type': 'image/svg+xml'},
    '/img/fi_tc_airplane.svg': {'filename':'./img/fi_tc_airplane.svg','content_type': 'image/svg+xml'},
    '/img/heading_mechanics.svg': {'filename':'./img/heading_mechanics.svg','content_type': 'image/svg+xml'},
    '/img/heading_yaw.svg': {'filename':'./img/heading_yaw.svg','content_type': 'image/svg+xml'},
    '/img/horizon_back.svg': {'filename':'./img/horizon_back.svg','content_type': 'image/svg+xml'},
    '/img/horizon_ball.svg': {'filename':'./img/horizon_ball.svg','content_type': 'image/svg+xml'},
    '/img/horizon_circle.svg': {'filename':'./img/horizon_circle.svg','content_type': 'image/svg+xml'},
    '/img/horizon_mechanics.svg': {'filename':'./img/horizon_mechanics.svg','content_type': 'image/svg+xml'},
    '/img/speed_mechanics.svg': {'filename':'./img/speed_mechanics.svg','content_type': 'image/svg+xml'},
    '/img/turn_coordinator.svg': {'filename':'./img/turn_coordinator.svg','content_type': 'image/svg+xml'},  
    '/img/vertical_mechanics.svg': {'filename':'./img/vertical_mechanics.svg','content_type': 'image/svg+xml'}  
})        


def serial_data_receive():
    i=0
    global numpy_array
    global sio
    while  True:
        if i==len(numpy_array):
            i=0
        j=[numpy_array[i,0],numpy_array[i,1],numpy_array[i,2],numpy_array[i,3],numpy_array[i,4],numpy_array[i,5],numpy_array[i,6],numpy_array[i,7],numpy_array[i,8],numpy_array[i,9]]
        sio.emit('sum_res',{'result':j})
        print(j)
        time.sleep(2)
        i=i+1
        


        
t=threading.Thread(target=serial_data_receive)
t.start() ## just in case

        
@sio.event
def connect(sid, environ):
    print(sid,'connected')

@sio.event
def disconnect(sid):
    print(sid,'disconnected')


