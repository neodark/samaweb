//Directive that returns an element which adds buttons on click which adds items
var app = angular.module('samawebApp');

//Directive to login on button click
app.directive("buttonsavecourse", function($compile)
{
	return function(scope, element, attrs)
    {
        //login button click
		element.bind("click", function()
        {
            scope.save_course(scope.course_type, scope.new_course_dates, scope.new_course_address, scope.new_course_maximum_participants);
		});
    }
});
