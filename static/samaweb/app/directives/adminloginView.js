//Directive that returns an element which adds buttons on click which adds items
var app = angular.module('samawebApp');

//Directive to login on button click
app.directive("buttonlogin", function($compile)
{
	return function(scope, element, attrs)
    {
        //login button click
		element.bind("click", function()
        {
            var email_input = document.getElementById("user_id");
            var password_input = document.getElementById("user_password");
            scope.login(email_input.value, password_input.value);
            //checkCredentials("neo", "pwd4sama")
		});
    }
});

//Directive to login on button click
app.directive("buttonlogout", function($compile)
{
	return function(scope, element, attrs)
    {
        //login button click
		element.bind("click", function()
        {
            scope.logout();
		});
    }
});
