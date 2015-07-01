//This controller retrieves data from the courseFactory through the REST API and associates it with the $scope
//The $scope is ultimately bound to the course view
app.controller('courseController',['$scope', 'courseFactory', function ($scope, courseFactory) {

   $scope.courses;
   $scope.course_type;
   $scope.course_list_url;
   $scope.url_prefix;
   $scope.static_url;

   $scope.init = function(course_type, course_list_url, url_prefix, static_url)
   {
       $scope.course_type     = course_type;
       $scope.course_list_url = course_list_url;
       $scope.url_prefix = url_prefix;
       $scope.static_url = static_url;
       getCourseData($scope.course_type, $scope.course_list_url);
   }
 
   function getCourseData(course_type, course_list_url)
   {
       courseFactory.getCoursesInformation(course_type, course_list_url)
           .success(function (coursesData) {
               $scope.courses = coursesData;
               $scope.courses.url_prefix = $scope.url_prefix;
           })
           .error(function (error) {
               $scope.status = 'Unable to load courses data: ' + error.message;
           });
   }
}]);
