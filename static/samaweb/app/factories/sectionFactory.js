//This factory retrieves data from the REST API and associates it with the $scope
app.factory('sectionFactory', ['$http', function($http) {

    var urlBase = '';
    var sectionFactory = {};

    sectionFactory.getSectionsInformation = function (section_list_url) {
        return $http.get(section_list_url);
    };

    sectionFactory.getSectionInformation = function (section_id, section_list_url) {
        return $http.get(section_list_url + section_id);
    };

    sectionFactory.addSection = function (sectionData)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/section/',
          method: "POST",
          data: sectionData,
        })
    };

    sectionFactory.updateSection = function (section_id, sectionData)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/section/' + section_id,
          method: "PUT",
          data: sectionData,
        })
    };

    sectionFactory.deleteSection = function (sectionId)
    {
        return $http({
          headers: {'Content-Type': 'application/json'},
          url: '/api/section/' + sectionId,
          method: "DELETE",
        })
    };

    return sectionFactory;
}]);
