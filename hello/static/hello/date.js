function addMonths(dateObj, num) {
	var currentMonth = dateObj.getMonth() + dateObj.getFullYear() * 12;
	dateObj.setMonth(dateObj.getMonth() + num);
	var diff = dateObj.getMonth() + dateObj.getFullYear() * 12 - currentMonth;

	// If don't get the right number, set date to
	// last day of previous month
	if (diff != num) {
		dateObj.setDate(0);
	}
	return dateObj;
}
