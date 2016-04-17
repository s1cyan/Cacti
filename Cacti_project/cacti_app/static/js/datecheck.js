function areDatesCorrect(startDate, endDate) {
    var currentDate = new Date().toLocaleString().split('/');
    var dateStart = new Date(
        parseInt(currentDate[0]),
        parseInt(currentDate[1]),
        parseInt(currentDate[2]),
        parseInt(startDate[0]),
        parseInt(startDate[1])
    );

    var dateEnd = new Date(
        parseInt(currentDate[0]),
        parseInt(currentDate[1]),
        parseInt(currentDate[2]),
        parseInt(endDate[0]),
        parseInt(endDate[1])
    );
   
    return dateStart < dateEnd;
};
