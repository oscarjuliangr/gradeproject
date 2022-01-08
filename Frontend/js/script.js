import { io } from 'https://cdn.socket.io/4.3.2/socket.io.esm.min.js';
import { PORT, URL } from './const.js';
import {
  airspeed,
  altimeter,
  attitude,
  heading,
  turn_coordinator,
  variometer,
} from './flightVars.js';

const socket = io(`${URL}:${PORT}`);

var increment = 0;
setInterval(function () {
  // Airspeed update
  airspeed.setAirSpeed(180); //0-160 knots

  // Attitude update
  attitude.setRoll(30 * Math.sin(increment / 10));
  attitude.setPitch(50 * Math.sin(increment / 20));

  // Altimeter update
  altimeter.setAltitude(10 * increment); // variable 203
  altimeter.setPressure(1000 + 3 * Math.sin(increment / 50)); // variable 217

  increment++;

  // TC update - note that the TC appears opposite the angle of the attitude indicator, as it mirrors the actual wing up/down position
  turn_coordinator.setTurn(30 * Math.sin(increment / 10) * -1);

  // Heading update
  heading.setHeading(12);

  // Vario update
  variometer.setVario(2 * Math.sin(increment / 10));
}, 50); //muestrea cada milisegundo
