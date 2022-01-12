// Dynamic examples
export const attitude = $.flightIndicator('#attitude', 'attitude', {
  roll: 0,
  pitch: -20,
  size: 200,
  showBox: true,
});
export const heading = $.flightIndicator('#heading', 'heading', {
  heading: -180,
  showBox: true,
});
export const variometer = $.flightIndicator('#variometer', 'variometer', {
  vario: -5,
  showBox: true,
});
export const airspeed = $.flightIndicator('#airspeed', 'airspeed', {
  showBox: false,
});
export const altimeter = $.flightIndicator('#altimeter', 'altimeter');
export const turn_coordinator = $.flightIndicator(
  '#turn_coordinator',
  'turn_coordinator',
  { turn: 0 }
);
