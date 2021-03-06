//Directive that returns an element which adds buttons on click which adds items
var app = angular.module('samawebApp');

//Directive to save course on button click
app.directive("buttonsavecourse", function($compile)
{
	return function(scope, element, attrs)
    {
        //login button click
		element.bind("click", function()
        {
            scope.save_course(scope.course_type, scope.new_course_dates, scope.new_course_time, scope.new_course_address, scope.new_course_maximum_participants, scope.course_price);
		});
    }
});

//Directive to update course on button click
app.directive("buttonupdatecourse", function($compile)
{
	return function(scope, element, attrs)
    {
        //button click
		element.bind("click", function()
        {
            var action = attrs.id.split("btn_course_")[1];
            scope.update_course(scope.singleCourse.id, scope.course_type, scope.new_course_dates, scope.new_course_time, scope.new_course_address, scope.new_course_maximum_participants, scope.course_price, action);
		});
    }
});

//Directive to delete participant on button click
app.directive("buttondeleteparticipant", function($compile)
{
	return function(scope, element, attrs)
    {
        //login button click
		element.bind("click", function()
        {
            var action = attrs.id.split("btn_participant_")[1];
            scope.delete_participant(scope.course_id, scope.course_type, scope.participant_to_update.id, action);
		});
    }
});

//Directive to delete participant on button click
app.directive("buttondownloadparticipants", function($compile)
{
	return function(scope, element, attrs)
    {
        //login button click
		element.bind("click", function()
        {
            scope.download_pdf_participants(scope.course_id, scope.course_type);
		});
    }
});
