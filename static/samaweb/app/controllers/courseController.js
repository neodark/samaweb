//This controller retrieves data from the courseFactory through the REST API and associates it with the $scope
//The $scope is ultimately bound to the course view
app.controller('courseController',['$scope', 'courseFactory', function ($scope, courseFactory) {

   $scope.courses;
   $scope.course_type;
   $scope.course_list_url;
   $scope.birthdate_year = [];
   $scope.birthdate_month = [];
   $scope.birthdate_month_name = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
   "Août", "Septembre", "Octobre", "Novembre", "Décembre"];
   $scope.birthdate_day = [];

   var currentTime = new Date();
   var year = currentTime.getFullYear();

   for (var i = year-70; i < year; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = i;
        $scope.birthdate_year.push(item_dict);
   }

   for (var i = 1; i < 13; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = $scope.birthdate_month_name[i-1];
        $scope.birthdate_month.push(item_dict);
   }

   for (var i = 1; i < 32; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = i;
        $scope.birthdate_day.push(item_dict);
   }

   $scope.submitted = false;
   $scope.signupForm = function() {
     if ($scope.signup_form.$valid) {
       // Submit as normal
       console.log("submit as normal");
       console.log($scope.signup_form);
     } else {
       console.log("submit error");
       console.log($scope.signup_form);
       $scope.signup_form.submitted = true;
     }
   }


   $scope.init = function(course_type, course_list_url)
   {
       $scope.course_type     = course_type;
       $scope.course_list_url = course_list_url;
       getCourseData($scope.course_type, $scope.course_list_url);
       console.log($scope);
   }
 
   function getCourseData(course_type, course_list_url)
   {
       courseFactory.getCoursesInformation(course_type, course_list_url)
           .success(function (coursesData) {
               $scope.courses = coursesData;
           })
           .error(function (error) {
               $scope.status = 'Unable to load courses data: ' + error.message;
           });
   }
}]);
