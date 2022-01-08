import socketio
import arnic_dec
import serial
import threading
import time
from serial import Serial


ser= serial.Serial('/dev/ttyUSB0',57600)
p=[(324,'67')]
def serial_data_receive():
    while  True:
        global p
        f= ser.readline()
        data=f.decode("utf-8")
        #print(data)
        tab=[i for i, x in enumerate(data) if x == "\t"]
        l_data=len(tab)
        if ("\n" in data) and l_data==3:
            GRS77=data[0:tab[0]]
            GDC74A=data[tab[0]+1:tab[1]]
            GTN50=data[tab[1]+1:tab[2]]
            p0=arnic_dec.arn_dec(GRS77)
            p1=arnic_dec.arn_dec(GDC74A)
            p2=arnic_dec.arn_dec(GTN50)
            p=[p0,p1,p2]
        print(p)


        
t=threading.Thread(target=serial_data_receive);
t.start(); ## just in case

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

@sio.event
def connect(sid, environ):
    print(sid,'connected')
    
@sio.event
def disconnect(sid):
    print(sid,'disconnected')

@sio.event
def sum(sid,data):
    #print(sid, data)
    #result= data['numbers'][0]+data['numbers'][1]
    
    sio.emit('sum_res',{'result':p}, to=sid)

@sio.event
def communicate(sid):
    sio.emit('p_data',{'data is:',1}, to=sid)


