/*
This will be the Java Script File
*/

// Helper HTML strings. To be used when appending to the table.
var HTMLrow = "<tr><td>%status%</td><td>%nomen%</td><td>%lastcheckin%</td><td>%serial%</td></tr>";
var statusGreen = "<div class='green-dot'>Working</div>";
var statusRed = "<div class='red-dot'>Disconnected</div>";
var statusYellow = "<div class='yellow-dot'>No recent back up</div>";
var statusBlack ="<div class='black-dot'>Overdue for Check in</div>";

function makeTable(statusArray){
  statusArray.forEach(function(entry){
    status = checkStatus(entry);
    name = entry.name;
    timestring = entry.timestring;
    serial = entry.serial;
    formatted_row = HTMLrow.replace("%status%",status).replace("%nomen%",name).replace("%serial%",serial).replace("%lastcheckin%",timestring);
    $("#putstuffhere").append(formatted_row);
  })
};

function checkTime(entry){
  var inputTime = new Date(entry.timestring);
  var currentTime = new Date(Date.now());
  var timeDelta = (currentTime - inputTime)/1000/60; //Converted into minutes.
  var too_long = 12 * 60 // Twelve hours.
  if (timeDelta >= too_long){
    return 'no check ins';
  }
  else{
    return 'recent';
  }
}

function checkStatus(entry){
  if (checkTime(entry) === 'no check ins'){
    return statusBlack;
  }
  else if (entry.status === "working"){
    return statusGreen;
  }
  else if (entry.status === "disconnected"){
    return statusRed;
  }
  else if (entry.status === "overdue") {
    return statusYellow;
  };
}
makeTable(statusArray);
// Append statement. To be used much later.

// loadlist();
