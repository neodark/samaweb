//Directive that returns an element which adds buttons on click which adds items
var app = angular.module('samawebApp');

//Directive to save/update course on button click
app.directive("buttonsaveupdateprogram", function($compile)
{
	return function(scope, element, attrs)
    {
        //login button click
		element.bind("click", function()
        {
            var action = attrs.id.split("btn_section_program_")[1];

            course_dates = [];
            course_dates.push(scope.new_course_dates_january);
            course_dates.push(scope.new_course_dates_february);
            course_dates.push(scope.new_course_dates_march);
            course_dates.push(scope.new_course_dates_april);
            course_dates.push(scope.new_course_dates_may);
            course_dates.push(scope.new_course_dates_june);
            course_dates.push(scope.new_course_dates_july);
            course_dates.push(scope.new_course_dates_august);
            course_dates.push(scope.new_course_dates_september);
            course_dates.push(scope.new_course_dates_october);
            course_dates.push(scope.new_course_dates_november);
            course_dates.push(scope.new_course_dates_december);

            course_time = [];
            course_time.push(scope.new_course_time_january);
            course_time.push(scope.new_course_time_february);
            course_time.push(scope.new_course_time_march);
            course_time.push(scope.new_course_time_april);
            course_time.push(scope.new_course_time_may);
            course_time.push(scope.new_course_time_june);
            course_time.push(scope.new_course_time_july);
            course_time.push(scope.new_course_time_august);
            course_time.push(scope.new_course_time_september);
            course_time.push(scope.new_course_time_october);
            course_time.push(scope.new_course_time_november);
            course_time.push(scope.new_course_time_december);

            course_address = [];
            course_address.push(scope.new_course_address_january);
            course_address.push(scope.new_course_address_february);
            course_address.push(scope.new_course_address_march);
            course_address.push(scope.new_course_address_april);
            course_address.push(scope.new_course_address_may);
            course_address.push(scope.new_course_address_june);
            course_address.push(scope.new_course_address_july);
            course_address.push(scope.new_course_address_august);
            course_address.push(scope.new_course_address_september);
            course_address.push(scope.new_course_address_october);
            course_address.push(scope.new_course_address_november);
            course_address.push(scope.new_course_address_december);

            course_topic = [];
            course_topic.push(scope.new_course_topic_january);
            course_topic.push(scope.new_course_topic_february);
            course_topic.push(scope.new_course_topic_march);
            course_topic.push(scope.new_course_topic_april);
            course_topic.push(scope.new_course_topic_may);
            course_topic.push(scope.new_course_topic_june);
            course_topic.push(scope.new_course_topic_july);
            course_topic.push(scope.new_course_topic_august);
            course_topic.push(scope.new_course_topic_september);
            course_topic.push(scope.new_course_topic_october);
            course_topic.push(scope.new_course_topic_november);
            course_topic.push(scope.new_course_topic_december);

            scope.save_program(course_dates, course_time, course_address, course_topic, action);
		});
    }
});

//Directive to delete participant on button click
app.directive("buttondownloadprogram", function($compile)
{
	return function(scope, element, attrs)
    {
        //login button click
		element.bind("click", function()
        {
            scope.download_pdf_program_section(scope.course_id, scope.course_type);
		});
    }
});
