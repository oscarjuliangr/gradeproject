import {
  airspeed,
  altimeter,
  attitude,
  heading,
  turn_coordinator,
  variometer,
} from './flightVars.js';

const stopButton = document.getElementById('stop');
const startButton = document.getElementById('start');

const sio = io();
sio.on('connect', () => {
  console.log('client connected');
  sio.emit('sum', { numbers: [1, 2] });
});
sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('sum_res', ({ result }) => {
  console.log(result);
  updateData(result);
});

const updateData = (data) => {
  if (typeof data[0] === 'number') {
    airspeed.setAirSpeed(data[0]);
  }
  if (typeof data[1] === 'number') {
    attitude.setRoll(data[1]);
    turn_coordinator.setTurn(data[1] * -1);
  }
  if (typeof data[2] === 'number') {
    attitude.setPitch(data[2]);
  }
  if (typeof data[3] === 'number') {
    altimeter.setAltitude(data[3]);
  }
  if (typeof data[4] === 'number') {
    altimeter.setPressure(data[4]); // Revisar, sale de la escala y no se ve
  }
  if (typeof data[5] === 'number') {
    heading.setHeading(data[5]);
  }
  if (typeof data[6] === 'number') {
    variometer.setVario(data[6]);
  }
  if (typeof data[7] === 'number') {
    let times = data[7].toString();    
    let hour = times.substring(0,2);
    let minutes = times.substring(2,4);
    let sec =  Number.parseInt(times.substring(5,6),10)*6;
    let seconds = sec.toString(); 
    if (isNaN(sec)){
      let seconds = " "      
      return seconds;
    } 
    
    let f_time = hour + ":" + minutes + ":" + seconds;
    document.getElementById("tiempo").innerText = f_time;

  }
  if (typeof data[8] === 'number') {
    document.getElementById("latitude").innerHTML = data[8];
  }
  if (typeof data[9] === 'number') {
    document.getElementById("longitude").innerHTML = data[9];
  }
};

stopButton.addEventListener('click', () => {
  sio.emit('stop','stop');
});

startButton.addEventListener('click', () => {
  sio.emit('stop','start');
});