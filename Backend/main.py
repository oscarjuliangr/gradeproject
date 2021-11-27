import socketio
import arnic_dec
import time


start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))
arnic_dec.arn_dec('3764437209')

# create a Socket.IO server
sio = socketio.Server()

# wrap with a WSGI application
app = socketio.WSGIApp(sio)