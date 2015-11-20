//This controller retrieves data from the courseFactory through the REST API and associates it with the $scope
//The $scope is ultimately bound to the course view
//app.controller('courseController',['$scope', 'courseFactory', 'authFactory', function ($scope, courseFactory, authFactory) {
app.controller('authController',['$scope', 'authState', 'authFactory', function ($scope, authState, authFactory) {

   $scope.authState = authState;

   $scope.initAuth = function()
   {
   }

   $scope.login = function(username, password)
   {
       authFactory.login(username, password)
           .success(function (loginData) {
               $scope.status = 'Successfully logged in user: ' + loginData;
               authState.user = loginData.username;
           })
           .error(function (error) {
               $scope.status = 'Unable to login user: ' + error.message;
           });
   }

   $scope.logout = function()
   {
       authFactory.logout()
           .success(function (loginData) {
               $scope.status = 'Successfully logged out user: ' + loginData + authState.user;
               authState.user = undefined;
           })
           .error(function (error) {
               $scope.status = 'Unable to logout user: ' + error.message;
           });
   }

}]);
