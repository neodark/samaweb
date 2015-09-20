//This controller retrieves data from the courseFactory through the REST API and associates it with the $scope
//The $scope is ultimately bound to the course view
app.controller('courseController',['$scope', 'courseFactory', function ($scope, courseFactory) {

   $scope.courses;
   $scope.course_type;
   $scope.course_list_url;

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
