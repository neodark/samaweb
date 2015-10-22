//This controller retrieves data from the courseFactory through the REST API and associates it with the $scope
//The $scope is ultimately bound to the course view
app.controller('courseController',['$scope', 'courseFactory', function ($scope, courseFactory) {

   $scope.courses;
   $scope.course_type;
   $scope.course_list_url;
   $scope.birthdate_year = [];
   $scope.birthdate_month = [];
   $scope.birthdate_month_name = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
   "Août", "Septembre", "Octobre", "Novembre", "Décembre"];
   $scope.birthdate_day = [];
   $scope.gender_type = ["M.", "Mme."];
   $scope.gender = [];

   var currentTime = new Date();
   var year = currentTime.getFullYear();

   for (var i = 0; i < $scope.gender_type.length; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = $scope.gender_type[i];
        $scope.gender.push(item_dict);
   }

   for (var i = year-70; i < year; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = i;
        $scope.birthdate_year.push(item_dict);
   }

   for (var i = 1; i < 13; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = $scope.birthdate_month_name[i-1];
        $scope.birthdate_month.push(item_dict);
   }

   for (var i = 1; i < 32; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = i;
        $scope.birthdate_day.push(item_dict);
   }

   //$scope.submitted = false;
   $scope.signupForm = function()
   {
       if ($scope.signup_form.$valid)
       {
           // Submit as normal
           console.log("submit as normal");
           console.log($scope.signup_form);

           var data_participant = {};
           data_participant["sex"] = $scope.signup_form.gender_type_select.$modelValue;
           data_participant["first_name"] = $scope.signup_form.firstname.$modelValue;
           data_participant["last_name"] = $scope.signup_form.lastname.$modelValue;
           data_participant["birth_date"] = '2015-01-25';
           data_participant["address"] = $scope.signup_form.address.$modelValue;
           data_participant["npa"] = $scope.signup_form.npa.$modelValue;
           data_participant["city"] = $scope.signup_form.city.$modelValue;
           data_participant["phone"] = $scope.signup_form.phone.$modelValue;
           data_participant["email"] = $scope.signup_form.email.$modelValue;
           data_participant["course"] = 1;
           data_participant["last_course_date"] = '2015-02-11';

           courseFactory.registerParticipant(data_participant);
       }
       else
       {
           console.log("submit error");
           console.log($scope.signup_form);
           console.log($scope.signup_form.lastname.$valid);
           if(! $scope.signup_form.gender_type_select.$valid)
           {
               bootbox.alert("Merci d'indiquer M. ou Mme. dans le menu au dessus de votre prénom", function()
               {
               });
           }
           if(! $scope.signup_form.firstname.$valid)
           {
               bootbox.alert("Votre prénom n'est pas valide", function()
               {
               });
           }
           if(! $scope.signup_form.lastname.$valid)
           {
               bootbox.alert("Votre nom n'est pas valide", function()
               {
               });
           }
           if(! $scope.signup_form.address.$valid)
           {
               bootbox.alert("Merci d'indiquer votre adresse", function()
               {
               });
           }
           if(! $scope.signup_form.npa.$valid)
           {
               bootbox.alert("Merci d'indiquer le numéro postale de votre ville de résidence(exemple: 1920)", function()
               {
               });
           }
           if(! $scope.signup_form.city.$valid)
           {
               bootbox.alert("Merci d'indiquer votre ville de résidence", function()
               {
               });
           }
           if(! $scope.signup_form.phone.$valid)
           {
               bootbox.alert("Merci d'indiquer votre numéro de téléphone", function()
               {
               });
           }
           if(! $scope.signup_form.email.$valid)
           {
               bootbox.alert("Merci d'indiquer votre adresse email", function()
               {
               });
           }

     //$scope.signup_form.submitted = true;
     }
   }


   $scope.init = function(course_type, course_list_url)
   {
       $scope.course_type     = course_type;
       $scope.course_list_url = course_list_url;
       getCourseData($scope.course_type, $scope.course_list_url);
       console.log($scope);
   }
 
   function getCourseData(course_type, course_list_url)
   {
       courseFactory.getCoursesInformation(course_type, course_list_url)
           .success(function (coursesData) {
               $scope.courses = coursesData;
           })
           .error(function (error) {
               $scope.status = 'Unable to load courses data: ' + error.message;
           });
   }
}]);
