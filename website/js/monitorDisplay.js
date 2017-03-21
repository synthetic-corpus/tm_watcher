/*
This will be the Java Script File
*/

// Helper HTML strings. To be used when appending to the table.
var HTMLrow = "<tr><td>%status%</td><td>%nomen%</td><td>%lastcheckin%</td><td>%serial%</td></tr>";
var statusGreen = "<div class='green-dot'>Working</div>";
var statusRed = "<div class='red-dot'>Disconnected</div>";
var statusYellow = "<div class='yellow-dot'>No recent back up</div>";
var statusBlack ="<div class='black-dot'>Overdue for Check in>/div>";

function makeTable(statusArray){
  statusArray.forEach(function(entry){
    status = checkStatus(entry.status);
    name = entry.name;
    timestring = entry.timestring;
    serial = entry.serial;
    formatted_row = HTMLrow.replace("%status%",status).replace("%nomen%",name).replace("%serial%",serial).replace("%lastcheckin%",timestring);
    $("#putstuffhere").append(formatted_row);
  })
};

function checkStatus(status){
  if (status === "working"){
    return statusGreen;
  }
  else if (status === "disconnected"){
    return statusRed;
  }
  else if (status === "overdue") {
    return statusYellow;
  };
}
makeTable(statusArray);
// Append statement. To be used much later.

// loadlist();
