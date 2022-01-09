import socketio

import arnic_dec
import serial
import threading
import time
from serial import Serial


ser= serial.Serial('/dev/ttyUSB0',57600)
p=[]
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
        #print(p)


        
t=threading.Thread(target=serial_data_receive);
t.start(); ## just in case

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './'
})


@sio.event
async def connect(sid, environ):
    print(sid, 'connected')


@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')