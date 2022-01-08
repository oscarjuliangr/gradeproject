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
var to_check=12;
setInterval(function () {
  // Airspeed update
  airspeed.setAirSpeed(180); //0-160 knots label 210 Position 1

  // Attitude update
  attitude.setRoll(30 * Math.sin(increment / 10)); // label 325 position 2
  attitude.setPitch(50 * Math.sin(increment / 20)); // label 324 position 3

  // Altimeter update
  altimeter.setAltitude(10 * increment); // label 312 position 4
  altimeter.setPressure(1000 + 3 * Math.sin(increment / 50)); // label 217 position 5

  increment++;

  // TC update - note that the TC appears opposite the angle of the attitude indicator, as it mirrors the actual wing up/down position
  turn_coordinator.setTurn(30 * Math.sin(increment / 10) * -1);  // label 325 position 2


  
  // Heading update
  heading.setHeading(to_check); // label 320 position 6
  to_check=to_check+2;
  // Vario update
  variometer.setVario(0); // label 364 position 7
  // label 125 position 8  this is universal time
  // label  310 position  9 this is latitude
  // label 311  position 10 this is Longitude



}, 50); //muestrea cada milisegundo
