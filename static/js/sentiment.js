// News Gauge
var opts = {
  angle: 0, // The span of the gauge arc
  lineWidth: 0.3, // The line thickness
  radiusScale: 0.9, // Relative radius
  pointer: {
    length: 0.42, // // Relative to gauge radius
    strokeWidth: 0.029, // The thickness
    color: '#000000' // Fill color
  },
  limitMax: true,     // If false, max value increases automatically if value > maxValue
  limitMin: true,     // If true, the min value of the gauge will be fixed
  colorStart: '#6F6EA0',   // Colors
  colorStop: '#C0C0DB',    // just experiment with them
  strokeColor: '#EEEEEE',  // to see which ones work best for you
  generateGradient: true,
  highDpiSupport: true,     // High resolution support
  // renderTicks is Optional
  // renderTicks: {
  //   divisions: 0,
  //   divWidth: 0.1,
  //   divLength: 0.41,
  //   divColor: '#333333',
  //   subDivisions: 0,
  //   subLength: 0.14,
  //   subWidth: 3.1,
  //   subColor: '#ffffff'
  // },
  staticZones: [
   {strokeStyle: "#F03E3E", min: -10, max: -5}, // Red from 70 to 80
   {strokeStyle: "orange", min: -5, max: 0}, // Yellow 80 to 90
   {strokeStyle: "#FFDD00", min: 0, max: 5}, // Green 90 to 100
    {strokeStyle: "#30B32D", min: 5, max: 10}, // Green 90 to 100
  ],
  staticLabels: {
  font: "10px sans-serif",  // Specifies font
  labels: [-10,-5,0,5,10],  // Print labels at these values
  color: "#000000",  // Optional: Label text color
  fractionDigits: 0  // Optional: Numerical precision. 0=round off.
},
  
};
var target = document.getElementById('foo1'); // your canvas element
let senti_news_score = document.getElementById('sentinews').innerHTML;
var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
gauge.maxValue = 10; // set max gauge value
gauge.setMinValue(-10);  // Prefer setter over gauge.minValue = 0
gauge.animationSpeed = 10; // set animation speed (32 is default value)
gauge.set(senti_news_score); // set actual value


