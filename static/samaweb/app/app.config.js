var app = angular.module('samawebApp');

app.config(function configureStartEndSymbol($interpolateProvider) {
            $interpolateProvider.startSymbol('{$').endSymbol('$}');
        }
);

app.config(function configHttp($httpProvider) {
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.withCredentials = true;
        }
);
