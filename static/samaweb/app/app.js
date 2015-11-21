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
                },
                'courseInfoAdmin': {
                    templateUrl: '/partials/courseInfoAdmin/',
                    //templateUrl: '/reports/partials/reportGeneralInfo.html',
                    controller: 'courseController',
                },
                'courseRegistration': {
                    templateUrl: '/partials/courseRegistration/',
                    //templateUrl: '/reports/partials/reportGeneralInfo.html',
                    controller: 'courseController',
                }
            }
        })
});
