/*
This will be the Java Script File
*/
var dataList = {};

/*
This function will take network json objects.
It will compare them to the data list.
It will append accordingly.
*/
function net_input(json_in){
  console.log(json_in);
  var inputted_serial = json_in.serial;
  if (dataList.hasOwnProperty(inputted_serial)) {
    // Add all the inputed data to the datalist
  } else {
    // updated what the list already has.
  }
};

/*
Simulated Network input objects
*/
var simulation = [
  {
    "status":"disconnected",
    "serial":"C02JP0B4DKQ2",
    "computerName":"Joel's Imac Here",
    "timestamp":"2017-03-14 16:59:47"
  },
  {
    "status":"working",
    "serial":"XX2JP0B4DKQ2",
    "computerName":"Wolverine's Imac",
    "timestamp":"2017-03-14 10:11:47"
  },
  {
    "status":"working",
    "serial":"C02JP0B4DKQ2",
    "computerName":"Joel's Imac Here",
    "timestamp":"2017-03-14 16:59:47"
  },
  {
    "status":"working",
    "serial":"QQ2JP0B4DKQ2",
    "computerName":"Batman's Imac",
    "timestamp":"2017-03-14 12:10:47"
  },
  {
    "status":"working",
    "serial":"QQ2JP0B4DKQ2",
    "computerName":"Batman's Imac",
    "timestamp":"2017-03-14 13:10:47"
  },
  {
    "status":"disconnected",
    "serial":"XX2JP0B4DKQ2",
    "computerName":"Wolverine's Imac",
    "timestamp":"2017-03-14 10:11:47"
  }
];
/*
@param. A list of json_out objects from the network monitor.
This function simulates network input.
When project is fully ready, this function will be replaced.
*/
function input_network_sim(simulatedInput){

}
