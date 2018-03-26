//this controller retrieves data from the courseFactory through the REST API and associates it with the $scope
//The $scope is ultimately bound to the course view
app.controller('courseController',['$scope', 'courseFactory', 'authState', 'authFactory', function ($scope, courseFactory, authState, authFactory) {

   $scope.authState = authState;

   $scope.courses;
   $scope.course_type;
   $scope.course_id;
   $scope.course_list_url;
   $scope.single_course_dates;
   $scope.single_course_time;
   $scope.single_course_location;
   $scope.participant_to_update;
   $scope.participant_detail_url;
   $scope.birthdate_year = [];
   $scope.birthdate_month = [];
   $scope.birthdate_month_name = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
   "Août", "Septembre", "Octobre", "Novembre", "Décembre"];
   $scope.birthdate_day = [];
   $scope.birthdate_day_simple = [];
   $scope.birthdate_year_simple = [];
   $scope.gender_type = ["M.", "Mme."];
   $scope.gender_db_selection = ["M", "F"];
   $scope.current_course_type;
   $scope.gender = [];
   $scope.new_course_address = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time = "Les cours ont lieu de 19h à 22h";
   $scope.new_course_dates = "";
   $scope.new_course_maximum_participants = 12;
   $scope.signup = {};
   $scope.signup_gender_selected;
   $scope.signup_birthdate_selected;
   $scope.signup_birthdate_month_selected;
   $scope.signup_bd_day_selected;
   $scope.signup_bd_year_selected;
   $scope.myform;

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
        $scope.birthdate_year_simple.push(i);
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
        $scope.birthdate_day_simple.push(i);
   }

   //$scope.submitted = false;
   $scope.signupForm = function(selected_action)
   {
       if ($scope.signup_form.$valid)
       {
           // Submit as normal
           //console.log("submit as normal");

           var data_participant = {};
           data_participant["status"] = 'S';
           data_participant["first_name"] = $scope.signup_form.firstname.$modelValue;
           data_participant["last_name"] = $scope.signup_form.lastname.$modelValue;
           data_participant["address"] = $scope.signup_form.address.$modelValue;
           data_participant["npa"] = $scope.signup_form.npa.$modelValue;
           data_participant["city"] = $scope.signup_form.city.$modelValue;
           data_participant["phone"] = $scope.signup_form.phone.$modelValue;
           data_participant["email"] = $scope.signup_form.email.$modelValue;

           $scope.current_course_type = location.search.split('coursetype=')[1].split('&')[0];
           if(selected_action == 'add_participant')
           {
               data_participant["course"] = location.search.split('courseid=')[1];
               data_participant["gender"] = $scope.gender_db_selection[$scope.signup_form.gender_type_select.$modelValue];
               data_participant["birth_date"] = $scope.signup_form.year_select.$modelValue + "-" +
                                                $scope.signup_form.month_select.$modelValue + "-" +
                                                $scope.signup_form.day_select.$modelValue;

                courseFactory.registerParticipant(data_participant)
                .success(function (coursesData) {
                    //console.log(coursesData);
                    $('#modalparticipantsuccess').modal('show')
                })
                .error(function (error) {
                    $scope.status = 'Unable to load courses data: ' + error.message;
                    $('#modalparticipantfailure').modal('show')
                });
           }
           else if(selected_action == 'edit_participant')
           {
                data_participant["course"] = location.search.split('courseid=')[1].split('&participantid')[0];
                var gender_index = $scope.gender_type.indexOf($scope.signup_form.gender_type_select.$modelValue);
                data_participant["gender"] = $scope.gender_db_selection[gender_index];

                var birthdate_day = $scope.signup_form.day_select.$modelValue;
                var birthdate_month = $scope.birthdate_month_name.indexOf($scope.signup_form.month_select.$modelValue) + 1;
                var birthdate_year = $scope.signup_form.year_select.$modelValue;

                data_participant["gender"] = $scope.gender_db_selection[gender_index];

                data_participant["birth_date"] = birthdate_year + "-" +
                                                 birthdate_month + "-" +
                                                 birthdate_day;

                courseFactory.updateParticipant(data_participant, $scope.participant_to_update.id)
                .success(function (coursesData) {
                    //console.log(coursesData);
                    $('#modalparticipantsuccess').modal('show')
                })
                .error(function (error) {
                    $scope.status = 'Unable to load courses data: ' + error.message;
                    $('#modalparticipantfailure').modal('show')
                });
           }
       }
       else
       {
           //console.log("submit error");
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
           if(! $scope.signup_form.year_select.$valid || ! $scope.signup_form.month_select.$valid || ! $scope.signup_form.day_select.$valid)
           {
               bootbox.alert("Merci d'indiquer votre date de naissance", function()
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


   $scope.initCourse = function(course_type, course_list_url)
   {
       $scope.course_type     = course_type;
       $scope.course_list_url = course_list_url;
       getCourseData($scope.course_type, $scope.course_list_url);
   }

   $scope.initSingleCourse = function(course_type, course_list_url, course_id)
   {
       $scope.course_type     = course_type;
       $scope.course_list_url = course_list_url;
       getSingleCourseData(course_id, $scope.course_list_url);
   }

   $scope.initCourseRegistration = function(course_type, course_dates, course_time, course_location, course_list_url)
   {
       $scope.course_type     = course_type;
       $scope.course_list_url = course_list_url;
       $scope.single_course_dates = course_dates;
       $scope.single_course_time = course_time;
       $scope.single_course_location = course_location;
   }

   $scope.initParticipantEdition = function(course_type, course_dates, course_time, course_location, course_list_url, participant_detail_url, participant_id)
   {
       $scope.course_type     = course_type;
       $scope.course_list_url = course_list_url;
       $scope.single_course_dates = course_dates;
       $scope.single_course_time = course_time;
       $scope.single_course_location = course_location;
       $scope.participant_detail_url = participant_detail_url;
       getSingleParticipantData($scope.participant_detail_url);
   }

   function getSingleParticipantData(participant_detail_url)
   {
       courseFactory.getParticipantInformation(participant_detail_url)
           .success(function (participantData) {
               $scope.participant_to_update = participantData;
               if(participantData.gender == 'F')
               {
                    $scope.signup_gender_selected = $scope.gender_type[1];
               }
               else
               {
                    $scope.signup_gender_selected = $scope.gender_type[0];
               }
               $scope.signup_birthdate_selected = participantData.birth_date;
               $scope.signup_birthdate_month_selected = $scope.birthdate_month_name[parseInt(participantData.birth_date.split("-")[1]-1)];
               $scope.signup_bd_day_selected = parseInt(participantData.birth_date.split("-")[2]) ;
               $scope.signup_bd_year_selected = parseInt(participantData.birth_date.split("-")[0]) ;
               $scope.signup.firstname = participantData.first_name;
               $scope.signup.lastname = participantData.last_name;
               $scope.signup.address = participantData.address;
               $scope.signup.npa = participantData.npa;
               $scope.signup.city = participantData.city;
               $scope.signup.phone = participantData.phone;
               $scope.signup.email = participantData.email;

               $scope.course_id = participantData.course;
           })
           .error(function (error) {
               $scope.status = 'Unable to load participant data: ' + error.message;
           });
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

   function getSingleCourseData(course_id, course_list_url)
   {
       courseFactory.getCourseInformation(course_id, course_list_url)
           .success(function (coursesData) {
               $scope.singleCourse = coursesData;

               //set dates in course edition ui
               $scope.new_course_dates = $scope.singleCourse.additional_information.dates;

               var splitted_dates = $scope.new_course_dates.split(" ");

               $(".datepicker_course").datepicker({
                   format: "dd/mm/yyyy",
                   language: "fr-CH",
                   multidate: true,
                   multidateSeparator: " "
               });

               var all_dates = [];
               for(var i=0; i<splitted_dates.length; i++)
               {
                    var single_date_split = splitted_dates[i].split("-");
                    var singledate = new Date(single_date_split[1] + "/" + single_date_split[0] + "/" + single_date_split[2]);
                    all_dates.push(singledate);

               }

               $(".datepicker_course").datepicker("setDates", all_dates);
               $(".datepicker_course").datepicker('update');
               $scope.new_course_dates = $scope.singleCourse.additional_information.dates;

               //set time in course edition ui
               $scope.new_course_time = $scope.singleCourse.additional_information.time;

               //set location in course edition ui
               $scope.new_course_address = $scope.singleCourse.additional_information.location;

               //set maximum participants in course edition ui
               $scope.new_course_maximum_participants = $scope.singleCourse.max_inscription_counter;


           })
           .error(function (error) {
               $scope.status = 'Unable to load course data: ' + error.message;
           });
   }

   $scope.save_course = function(course_type, course_dates, course_time, course_address, maximum_participants)
   {
        var new_course_data = {};
        var additional_information = {};

        //replace dates dd/mm/yyyy by dd-mm-yyyy
        var find = '/';
        var re = new RegExp(find, 'g');
        var course_dates_list = course_dates.replace(re, '-');

        //create json data to upload
        additional_information["location"] = course_address;
        additional_information["dates"] = course_dates_list;
        additional_information["time"] = course_time;
        new_course_data["status"] = 'O';
        new_course_data["course_type"] = course_type;
        new_course_data["max_inscription_counter"] = maximum_participants;
        new_course_data["additional_information"] = additional_information;

        courseFactory.addCourse(new_course_data)
           .success(function (coursesData) {
               //console.log(coursesData);
               $('#modalsuccess').modal('show')
           })
           .error(function (error) {
               $scope.status = 'Unable to load courses data: ' + error.message;
               $('#modalfailure').modal('show')
           });
   }

   $scope.update_course = function(course_id, course_type, course_dates, course_time, course_address, maximum_participants, perform_action)
   {
        var update_course_data = {};
        var additional_information = {};

        //replace dates dd/mm/yyyy by dd-mm-yyyy
        var find = '/';
        var re = new RegExp(find, 'g');
        var course_dates_list = course_dates.replace(re, '-');

        //create json data to upload
        additional_information["location"] = course_address;
        additional_information["dates"] = course_dates_list;
        additional_information["time"] = course_time;
        //update_course_data["status"] = 'O';
        update_course_data["course_type"] = course_type;
        update_course_data["max_inscription_counter"] = maximum_participants;
        update_course_data["additional_information"] = additional_information;

        if(perform_action == 'archive')
        {
            update_course_data["status"] = 'C';
        }

        courseFactory.updateCourse(course_id, update_course_data)
           .success(function (coursesData) {
               //console.log(coursesData);
               $('#modalsuccess').modal('show')
           })
           .error(function (error) {
               $scope.status = 'Unable to load courses data: ' + error.message;
               $('#modalfailure').modal('show')
           });
   }

   $scope.delete_participant = function(course_id, course_type, participant_id, perform_action)
   {

        courseFactory.deleteParticipant(participant_id)
           .success(function (participantData) {
               //console.log(coursesData);
               $('#modalsuccess').modal('show')
           })
           .error(function (error) {
               $scope.status = 'Unable to load courses data: ' + error.message;
               $('#modalfailure').modal('show')
           });
   }

   $scope.download_pdf_participants = function(course_id, course_type)
   {

         var the_body = [];

         var headers = [{ text: 'M./Mme.', style: 'tableHeader' }, { text: 'Nom', style: 'tableHeader'}, { text: 'Prénom', style: 'tableHeader' }, { text: 'Naissance', style: 'tableHeader' }, { text: 'Adresse', style: 'tableHeader' }, { text: 'NPA', style: 'tableHeader' }, { text: 'Ville', style: 'tableHeader' }, { text: 'Téléphone', style: 'tableHeader' }, { text: 'Email', style: 'tableHeader' }];
         the_body.push(headers);

         for(var i = 0; i < $scope.singleCourse.participants.length; i++)
         {
            var single_participant = [];
            if($scope.singleCourse.participants[i].gender == 'F')
            {
                single_participant.push("Mme.");
            }
            else
            {
                single_participant.push("M.");
            }
            single_participant.push($scope.singleCourse.participants[i].last_name);
            single_participant.push($scope.singleCourse.participants[i].first_name);
            single_participant.push($scope.singleCourse.participants[i].birth_date.split("-")[2]+ "-" +
                                    $scope.singleCourse.participants[i].birth_date.split("-")[1]+ "-" +
                                    $scope.singleCourse.participants[i].birth_date.split("-")[0]);
            single_participant.push($scope.singleCourse.participants[i].address);
            single_participant.push($scope.singleCourse.participants[i].npa.toString());
            single_participant.push($scope.singleCourse.participants[i].city);
            single_participant.push($scope.singleCourse.participants[i].phone);
            single_participant.push($scope.singleCourse.participants[i].email);
            the_body.push(single_participant);
         }

         var docDefinition = {

            // by default we use portrait, you can change it to landscape if you wish
            pageOrientation: 'landscape',

            content: [
              { text: 'Samaritains de Martigny', fontSize: 24, bold: true, margin: [0, 20, 0, 8] },
              { text: 'Informations sur le cours:', fontSize: 14, bold: true, margin: [0, 20, 0, 8] },
              { text: 'Type: ' + course_type, fontSize: 12, bold: false },
              { text: 'Dates: ' + $scope.singleCourse.additional_information['dates'], fontSize: 12, bold: false },
              { text: 'Heures: ' + $scope.singleCourse.additional_information['time'], fontSize: 12, bold: false },
              { text: 'Lieu: ' + $scope.singleCourse.additional_information['location'], fontSize: 12, bold: false },
              { text: 'Participants:', fontSize: 14, bold: true, margin: [0, 20, 0, 8] },
              {
                      style: 'tableBody',
                      table: {
                              headerRows: 1,
                              body: the_body                      },
                      layout: 'lightHorizontalLines'
              },


            ],

            styles: {
                tableBody: {
                    margin: [0, 5, 0, 15]
                },
                tableHeader: {
                    bold: true,
                    fontSize: 13,
                    color: 'black'
                }
            },
        defaultStyle: {
            // alignment: 'justify'
        }

         };

        // download the PDF (temporarily Chrome-only)a
        var name_download = "Cours_" + course_type + ".pdf";
        pdfMake.createPdf(docDefinition).download(name_download);

   }


   //$scope.login = function(username, password)
   //{
   //    authFactory.login(username, password)
   //        .success(function (loginData) {
   //            $scope.status = 'Successfully logged in user: ' + loginData;
   //            $scope.user = loginData.username;
   //        })
   //        .error(function (error) {
   //            $scope.status = 'Unable to login user: ' + error.message;
   //        });
   //}

   //$scope.logout = function()
   //{
   //    authFactory.logout()
   //        .success(function (loginData) {
   //            $scope.status = 'Successfully logged out user: ' + loginData;
   //            $scope.user = undefined;
   //        })
   //        .error(function (error) {
   //            $scope.status = 'Unable to logout user: ' + error.message;
   //        });
   //}

}]);
