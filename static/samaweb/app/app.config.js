var app = angular.module('samawebApp');

app.config(function configureStartEndSymbol($interpolateProvider) {
            $interpolateProvider.startSymbol('{$').endSymbol('$}');
        }
);
