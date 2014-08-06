var events = [];
var exit = false;
var tempString = '';
while(exit == false) {
    var selection = prompt('Menu Options:\r\n1) Add Event\r\n2) Edit Event\r\n3) Delete Event\r\n4) View Events\r\n5) Exit');
    switch(selection) {
        case "1":
            var name = prompt("Enter the name of the event: ");
            var hour = prompt("Enter the hour of the day when the new event will take place: ");
            events[hour] = name;
            break;
        case "2":
            tempString = '';
            for(i=0;i<=23;i++) {
                if (events[i] != undefined) {
                    tempString += events[i] + " @ " + i + "\r\n";
                }
            }
            var edit = prompt(tempString+"\r\nWhich event would you like to edit?");
            if (events[edit] != undefined) {
                var newName = prompt(events[edit]+"\r\nWhat should the event's new name be?");
                var newTime = prompt(edit+"\r\nWhat time will the event take place?");
                if (newTime != edit) {
                    events[edit] = undefined;
                    events[newTime] = newName;
                } else {
                    events[edit] = newName;
                }
            } else {
                alert('There is no event planned for this time!');
            }
            break;
        case "3":
            tempString = '';
            for(i=0;i<=23;i++) {
                if (events[i] != undefined) {
                    tempString += events[i] + " @ " + i + "\r\n";
                }
            }
            var deleteEvent = prompt(tempString+'\r\nWhich event would you like to delete?')
            if (events[deleteEvent] != undefined) {
                events[deleteEvent] = undefined;
                alert('Event Deleted');
            } else {
                alert('There is no event planned for this time!');
            }
            break;
        case "4":
            tempString = '';
            for(i=0;i<=23;i++) {
                if (events[i] != undefined) {
                    tempString += events[i] + " @ " + i + "\r\n";
                }
            }
            alert(tempString);
            break;
        case "5":
            exit = true;
            break;
        default:
            break;
    }
}
