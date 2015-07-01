var app = angular.module('samawebApp', ['ui.router']);

app.config(function ($stateProvider, $urlRouterProvider){

    $urlRouterProvider
        .otherwise('/');

    $stateProvider
        .state('course', {
            url: '/',
            views: {
                'courseInfo': {
                    templateUrl: '/partials/courseInfo/',
                    //templateUrl: '/reports/partials/reportGeneralInfo.html',
                    controller: 'courseController',
                }
            }
        })
});
