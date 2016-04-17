function makeJSON(csrfValue, scheduleName, startTime, endTime, scheduleDescription) {
    var scheduleObject = new Object();
    
    scheduleObject['csrfmiddlewaretoken'] = csrfValue;
    scheduleObject['schedule_name'] = scheduleName;
    scheduleObject['start_time'] = startTime;
    scheduleObject['end_time'] = endTime;
    scheduleObject['schedule_description'] = scheduleDescription;
    
    return scheduleObject;
};