const sio =io();
sio.on('connect',()=>{
    console.log('client connected');
    sio.emit('sum', {numbers: [1,2]});
});
sio.on('disconnect',()=>{
    console.log('disconnected');
});

sio.on('sum_res',(data)=>{
    console.log('the result of the sum is ');
    console.log(data);
})

var button= document.getElementById("empezar_envio");


import {
  airspeed,
  altimeter,
  attitude,
  heading,
  turn_coordinator,
  variometer,
} from './flightVars.js';


var increment = 0;
setInterval(function () {
  // Airspeed update
  airspeed.setAirSpeed(180); //0-160 knots

  // Attitude update
  attitude.setRoll(30 * Math.sin(increment / 10));
  attitude.setPitch(50 * Math.sin(increment / 20));

  // Altimeter update
  altimeter.setAltitude(10 * increment);
  altimeter.setPressure(1000 + 3 * Math.sin(increment / 50));

  increment++;

  // TC update - note that the TC appears opposite the angle of the attitude indicator, as it mirrors the actual wing up/down position
  turn_coordinator.setTurn(30 * Math.sin(increment / 10) * -1);

  // Heading update
  heading.setHeading(12);

  // Vario update
  variometer.setVario(2 * Math.sin(increment / 10));
  //console.log("el valor de la variable es: "+increment);
}, 50); //muestrea cada milisegundo
