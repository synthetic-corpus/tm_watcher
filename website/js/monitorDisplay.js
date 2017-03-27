
/*
This will be the Java Script File

Javascript file must be run after 'table/json-table.js' initaties a variable.
Variable is statusArray = {} which contains data from client check ins.

This file also refreshes the html index every ten minutes, thus redrwaing the page
with updated date from table/json-table.js
*/
// Helper HTML strings. To be used when appending to the table.
var HTMLtableHearder = "<tr><th>Status</th><th>Comp name</th><th>Last Check-in</th><th>Serial</th></tr>"
var HTMLrow = "<tr><td>%status%</td><td>%nomen%</td><td>%lastcheckin%</td><td>%serial%</td></tr>";
var statusGreen = "<div class='green-dot'><span>Working</span></div>";
var statusRed = "<div class='red-dot'><span>Disconnected</span></div>";
var statusYellow = "<div class='yellow-dot'><span>No recent back up</span></div>";
var statusBlack = "<div class='black-dot'><span>Overdue for Check in</span></div>";
// Last Variable indicates a problem with the tm_monitor.py running on a client computer
// Do not ever actually expect this to be displayed.
var statusWhat = "<span>Something is amiss...</span>"

// @param is the 'statusArray' variable Object written by TM_Listener.py
// running this function calls all others here and modifies index.HTML

function makeTable(statusArray) {
    statusArray.forEach(function(entry) {
        status = checkStatus(entry);
        name = entry.name;
        timestring = entry.timestring;
        serial = entry.serial;
        formatted_row = HTMLrow.replace("%status%", status).replace("%nomen%", name).replace("%serial%", serial).replace("%lastcheckin%", timestring);
        $("#putstuffhere").append(formatted_row);
    })
};

// Checks the time of the check initself.
// Ensure that the check in recent.
// @param entry is a single Object{} from the Status Array

function checkTime(entry) {
    var inputTime = new Date(entry.timestring);
    var currentTime = new Date(Date.now());
    var timeDelta = (currentTime - inputTime) / 1000 / 60; //Converted into minutes.
    var too_long = 12 * 60 // Twelve hours.
    if (timeDelta >= too_long) {
        return 'no check ins';
    } else {
        return 'recent';
    }
}

// This function checks the status.
// Returns statusBlack, statusGreen .. etc to be interpreted by makeTable()
// @Param is a single object from statusArray

function checkStatus(entry) {
    if (checkTime(entry) === 'no check ins') {
        return statusBlack; // i.e 'Have no network data from this computer recently'
    } else if (entry.status === "working") {
        return statusGreen; // i.e. Have network data. Back up is recent.
    } else if (entry.status === "disconnected") {
        return statusRed; // i.e. Have network data. Back up is disconnected.
    } else if (entry.status === "overdue") {
        return statusYellow; // ie. Have network data. Back up is not recent.
    } else if (entry.status === "problem") {
        return statusWhat; // ie. There is a problem with client file.
    };
}

// Reloads the page.
// Logs time in console for troubleshooting purposes.

function reloadpage() {
    var when = new Date(Date.now());
    console.log("page reloaded at...");
    console.log(when);
    location.reload();
}
makeTable(statusArray)
setInterval(reloadpage, 600000); //Page auto reloads every ten minutes
