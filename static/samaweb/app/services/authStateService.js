//This factory retrieves data from the REST API and associates it with the $scope
app.service('authState', function() {

    var urlBase = '';
    var authState = {};

    authState.user = undefined;

    return authState;
});
