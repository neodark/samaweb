//this controller retrieves data from the sectionFactory through the REST API and associates it with the $scope
//The $scope is ultimately bound to the section view
app.controller('sectionController',['$scope', 'sectionFactory', 'authState', 'authFactory', function ($scope, sectionFactory, authState, authFactory) {

   $scope.authState = authState;

   $scope.sections;
   $scope.section;
   $scope.section_id;
   $scope.section_list_url;
   $scope.single_section_dates;
   $scope.single_section_time;
   $scope.single_section_location;
   $scope.participant_to_update;
   $scope.participant_detail_url;
   $scope.coursedate_year = [];
   $scope.coursedate_month = [];
   $scope.coursedate_month_name = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
   "Août", "Septembre", "Octobre", "Novembre", "Décembre"];
   $scope.coursedate_day = [];
   $scope.coursedate_day_simple = [];
   $scope.coursedate_year_simple = [];
   $scope.gender_type = ["M.", "Mme."];
   $scope.gender_db_selection = ["M", "F"];
   $scope.current_section_type;
   $scope.gender = [];
   $scope.new_section_address = "Martigny - Rue de Rossetan - sous la salle de gymnastique";
   $scope.new_section_time = "Les cours ont lieu de 19h à 22h";
   $scope.new_section_dates = "";
   $scope.new_section_maximum_participants = 12;
   $scope.signup = {};
   $scope.signup_gender_selected;
   $scope.signup_coursedate_selected;
   $scope.signup_coursedate_month_selected;
   $scope.signup_bd_day_selected;
   $scope.signup_bd_year_selected;

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
        $scope.coursedate_year.push(item_dict);
        $scope.coursedate_year_simple.push(i);
   }

   for (var i = 1; i < 13; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = $scope.coursedate_month_name[i-1];
        $scope.coursedate_month.push(item_dict);
   }

   for (var i = 1; i < 32; i++)
   {
        var item_dict = {};
        item_dict["identifier"] = i;
        item_dict["name"] = i;
        $scope.coursedate_day.push(item_dict);
        $scope.coursedate_day_simple.push(i);
   }

   $scope.initSection = function(section_list_url)
   {
       $scope.section_list_url = section_list_url;
       getSectionData($scope.section_list_url);
   }

   $scope.initSingleSection = function(section_type, section_list_url, section_id)
   {
       $scope.section_list_url = section_list_url;
       getSingleSectionData(section_id, $scope.section_list_url);
   }

   function getSectionData(section_list_url)
   {
       sectionFactory.getSectionsInformation(section_list_url)
           .success(function (sectionsData) {
               $scope.sections = sectionsData;
               $scope.section = sectionsData[0];
               console.log($scope.sections);
               console.log($scope.section);
           })
           .error(function (error) {
               $scope.status = 'Unable to load sections data: ' + error.message;
           });
   }

   function getSingleSectionData(section_id, section_list_url)
   {
       sectionFactory.getSectionInformation(section_id, section_list_url)
           .success(function (sectionsData) {
               $scope.singleSection = sectionsData;

               //set dates in section edition ui
               $scope.new_section_dates = $scope.singlesection.section_program.dates;

               //set time in section edition ui
               $scope.new_section_time = $scope.singlesection.section_program.time;

               //set location in section edition ui
               $scope.new_section_address = $scope.singlesection.section_program.location;

               //set maximum participants in section edition ui
               $scope.new_section_maximum_participants = $scope.singlesection.max_inscription_counter;
           })
           .error(function (error) {
               $scope.status = 'Unable to load section data: ' + error.message;
           });
   }

   $scope.save_section = function(section_dates, section_time, section_address, maximum_participants)
   {
        var new_section_data = {};
        var section_program = {};

        //replace dates dd/mm/yyyy by dd-mm-yyyy
        var find = '/';
        var re = new RegExp(find, 'g');
        var section_dates_list = section_dates.replace(re, '-');

        //create json data to upload
        section_program["location"] = section_address;
        section_program["dates"] = section_dates_list;
        section_program["time"] = section_time;
        new_section_data["status"] = 'O';
        new_section_data["section_type"] = section_type;
        new_section_data["max_inscription_counter"] = maximum_participants;
        new_section_data["section_program"] = section_program;

        sectionFactory.addsection(new_section_data)
           .success(function (sectionsData) {
               //console.log(sectionsData);
               $('#modalsuccess').modal('show')
           })
           .error(function (error) {
               $scope.status = 'Unable to load sections data: ' + error.message;
               $('#modalfailure').modal('show')
           });
   }

   $scope.update_section = function(section_id, section_type, section_dates, section_time, section_address, maximum_participants, perform_action)
   {
        var update_section_data = {};
        var section_program = {};

        //replace dates dd/mm/yyyy by dd-mm-yyyy
        var find = '/';
        var re = new RegExp(find, 'g');
        var section_dates_list = section_dates.replace(re, '-');

        //create json data to upload
        section_program["location"] = section_address;
        section_program["dates"] = section_dates_list;
        section_program["time"] = section_time;
        //update_section_data["status"] = 'O';
        update_section_data["section_type"] = section_type;
        update_section_data["max_inscription_counter"] = maximum_participants;
        update_section_data["section_program"] = section_program;

        if(perform_action == 'archive')
        {
            update_section_data["status"] = 'C';
        }

        sectionFactory.updatesection(section_id, update_section_data)
           .success(function (sectionsData) {
               //console.log(sectionsData);
               $('#modalsuccess').modal('show')
           })
           .error(function (error) {
               $scope.status = 'Unable to load sections data: ' + error.message;
               $('#modalfailure').modal('show')
           });
   }

   $scope.download_pdf_program_section = function(section_id)
   {

         var the_body = [];

         var headers = [{ text: 'M./Mme.', style: 'tableHeader' }, { text: 'Nom', style: 'tableHeader'}, { text: 'Prénom', style: 'tableHeader' }, { text: 'Naissance', style: 'tableHeader' }, { text: 'Adresse', style: 'tableHeader' }, { text: 'NPA', style: 'tableHeader' }, { text: 'Ville', style: 'tableHeader' }, { text: 'Téléphone', style: 'tableHeader' }, { text: 'Email', style: 'tableHeader' }];
         the_body.push(headers);

         for(var i = 0; i < $scope.singlesection.participants.length; i++)
         {
            var single_participant = [];
            if($scope.singlesection.participants[i].gender == 'F')
            {
                single_participant.push("Mme.");
            }
            else
            {
                single_participant.push("M.");
            }
            single_participant.push($scope.singlesection.participants[i].last_name);
            single_participant.push($scope.singlesection.participants[i].first_name);
            single_participant.push($scope.singlesection.participants[i].birth_date.split("-")[2]+ "-" +
                                    $scope.singlesection.participants[i].birth_date.split("-")[1]+ "-" +
                                    $scope.singlesection.participants[i].birth_date.split("-")[0]);
            single_participant.push($scope.singlesection.participants[i].address);
            single_participant.push($scope.singlesection.participants[i].npa.toString());
            single_participant.push($scope.singlesection.participants[i].city);
            single_participant.push($scope.singlesection.participants[i].phone);
            single_participant.push($scope.singlesection.participants[i].email);
            the_body.push(single_participant);
         }

         var docDefinition = {

            // by default we use portrait, you can change it to landscape if you wish
            pageOrientation: 'landscape',

            content: [
              { text: 'Samaritains de Martigny', fontSize: 24, bold: true, margin: [0, 20, 0, 8] },
              { text: 'Informations sur le cours:', fontSize: 14, bold: true, margin: [0, 20, 0, 8] },
              { text: 'Type: ' + section_type, fontSize: 12, bold: false },
              { text: 'Dates: ' + $scope.singlesection.section_program['dates'], fontSize: 12, bold: false },
              { text: 'Heures: ' + $scope.singlesection.section_program['time'], fontSize: 12, bold: false },
              { text: 'Lieu: ' + $scope.singlesection.section_program['location'], fontSize: 12, bold: false },
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
        var name_download = "Cours_" + section_type + ".pdf";
        pdfMake.createPdf(docDefinition).download(name_download);

   }

}]);
