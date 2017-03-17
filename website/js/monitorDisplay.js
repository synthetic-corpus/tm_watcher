/*
This will be the Java Script File
*/
var dataList = {};

var HTMLrow = "<tr><td>%status%</td><td>%nomen%</td><td>%lastcheckin%</td><td>%serial%</td></tr>"

$("#putstuffhere").append(HTMLrow);
$("#putstuffhere").append(HTMLrow.replace("%status%","something else"));
$("#putstuffhere").append(HTMLrow);
$("#putstuffhere").append(HTMLrow);
