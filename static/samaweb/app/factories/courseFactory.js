//This factory retrieves data from the REST API and associates it with the $scope
app.factory('courseFactory', ['$http', function($http) {

    var urlBase = '';
    var courseFactory = {};

    courseFactory.getCoursesInformation = function (course_type, course_list_url) {
        return $http.get(course_list_url + '?coursetype=' + course_type);
    };

    courseFactory.registerParticipant = function (participantData)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/participants/',
          method: "POST",
          data: participantData,
        })
    };

    return courseFactory;
}]);
