//This factory retrieves data from the REST API and associates it with the $scope
app.factory('authFactory', ['$http', function($http) {

    var urlBase = '';
    var authFactory = {};

    authFactory.login = function (username, password)
    {
        function add_auth_header(data, headersGetter){
            var headers = headersGetter();
            headers['Authorization'] = ('Basic ' + btoa(username +
                                        ':' + password));
        }

        var data_tosend = {};
        data_tosend["username"] = Base64.encode(username);
        data_tosend["password"] = Base64.encode(password);

        return $http({
          //headers: {'Content-Type': 'application/json'},
          url: '/api/auth/',
          method: "POST",
          data: data_tosend,
          //transformRequest: add_auth_header,
        })
    };

    authFactory.logout = function ()
    {
        return $http({
          //headers: {'Content-Type': 'application/json'},
          url: '/api/auth/',
          method: "DELETE",
        })
    };

    return authFactory;
}]);
