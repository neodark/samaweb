//This factory retrieves data from the REST API and associates it with the $scope
app.factory('courseFactory', ['$http', function($http) {

    var urlBase = '';
    var courseFactory = {};

    courseFactory.getCoursesInformation = function (course_type, course_list_url) {
        return $http.get(course_list_url + '?coursetype=' + course_type + '&coursestatus=Open');
    };

    courseFactory.getCourseInformation = function (course_id, course_list_url) {
        return $http.get(course_list_url + course_id);
    };

    courseFactory.addCourse = function (courseData)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/course/',
          method: "POST",
          data: courseData,
        })
    };

    courseFactory.updateCourse = function (course_id, courseData)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/course/' + course_id,
          method: "PUT",
          data: courseData,
        })
    };

    courseFactory.registerParticipant = function (participantData)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/participant/',
          method: "POST",
          data: participantData,
        })
    };

    courseFactory.updateParticipant = function (participantData, participantId)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/participant/' + participantId,
          method: "PUT",
          data: participantData,
        })
    };

    courseFactory.deleteParticipant = function (participantId)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/participant/' + participantId,
          method: "DELETE",
        })
    };


    courseFactory.getParticipantInformation = function (participant_detail_url) {
        return $http.get(participant_detail_url);
    };


    return courseFactory;
}]);
