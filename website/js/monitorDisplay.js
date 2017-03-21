/*
This will be the Java Script File
*/

console.log(statusArray);

// Helper HTML strings. To be used when appending to the table.
var HTMLrow = "<tr><td>%status%</td><td>%nomen%</td><td>%lastcheckin%</td><td>%serial%</td></tr>";
var statusGreen = "<div class='green-dot'>Working</div>";
var statusRed = "<div class='red-dot'>Disconnected</div>";
var statusYellow = "<div class='yellow-dot'>No recent back up</div>";
var statusBlack ="<div class='black-dot'>Overdue for Check in>/div>";

// Append statement. To be used much later.
$("#putstuffhere").append(HTMLrow);
// loadlist();
