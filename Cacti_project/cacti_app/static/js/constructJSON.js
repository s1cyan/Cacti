// makeJSON converts information from a form and passes it into a Javascript Object
function makeJSON(scheduleName, startTime, endTime, scheduleDescription, daysOfWeek) {
    var scheduleObject = new Object();
    
    scheduleObject['schedule_name'] = scheduleName;
    scheduleObject['start_time'] = startTime;
    scheduleObject['end_time'] = endTime;
    scheduleObject['schedule_description'] = scheduleDescription;
    scheduleObject['weekdays'] = daysOfWeek;
    
    return scheduleObject;
}