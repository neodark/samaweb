//this controller retrieves data from the sectionFactory through the REST API and associates it with the $scope
//The $scope is ultimately bound to the section view
app.controller('sectionController',['$scope', 'sectionFactory', 'authState', 'authFactory', function ($scope, sectionFactory, authState, authFactory) {

   $scope.authState = authState;

   $scope.sections;
   $scope.section;
   $scope.section_id;
   $scope.section_list_url;
   $scope.coursedate_month_name = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
   "Août", "Septembre", "Octobre", "Novembre", "Décembre"];

   $scope.new_course_address_january = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_january = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_january = "";
   $scope.new_course_topic_january = "Sujet du cours";
   $scope.new_course_address_february = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_february = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_february = "";
   $scope.new_course_topic_february = "Sujet du cours";
   $scope.new_course_address_march = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_march = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_march = "";
   $scope.new_course_topic_march = "Sujet du cours";
   $scope.new_course_address_march = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_address_april = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_april = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_april = "";
   $scope.new_course_topic_april = "Sujet du cours";
   $scope.new_course_address_may = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_may = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_may = "";
   $scope.new_course_topic_may = "Sujet du cours";
   $scope.new_course_address_june = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_june = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_june = "";
   $scope.new_course_topic_june = "Sujet du cours";
   $scope.new_course_address_july = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_july = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_july = "";
   $scope.new_course_topic_july = "Sujet du cours";
   $scope.new_course_address_august = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_august = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_august = "";
   $scope.new_course_topic_august = "Sujet du cours";
   $scope.new_course_address_september = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_september = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_september = "";
   $scope.new_course_topic_september = "Sujet du cours";
   $scope.new_course_address_october = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_october = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_october = "";
   $scope.new_course_topic_october = "Sujet du cours";
   $scope.new_course_address_november = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_november = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_november = "";
   $scope.new_course_topic_november = "Sujet du cours";
   $scope.new_course_address_december = "Martigny - Rue de Rossettan - sous la salle de gymnastique";
   $scope.new_course_time_december = "Les cours ont lieu de 19h30 à 21h30";
   $scope.new_course_dates_december = "";
   $scope.new_course_topic_december = "Sujet du cours";

   var currentTime = new Date();
   var year = currentTime.getFullYear();

   $scope.year = year;

   $scope.initSection = function(section_list_url)
   {
       $scope.section_list_url = section_list_url;
       getSectionData($scope.section_list_url);
   }

   $scope.initSingleSection = function(section_list_url, section_id)
   {
       $scope.section_list_url = section_list_url;
       $scope.section_id = section_id;
       getSingleSectionData(section_id, $scope.section_list_url);
   }

   function getSectionData(section_list_url)
   {
       sectionFactory.getSectionsInformation(section_list_url)
           .success(function (sectionsData) {
               $scope.sections = sectionsData;
               $scope.section = sectionsData[0];
               if(sectionsData[0] != undefined)
               {
                    $scope.section_id = sectionsData[0].id;
               }
           })
           .error(function (error) {
               $scope.status = 'Unable to load sections data: ' + error.message;
           });
   }

   function getSingleSectionData(section_id, section_list_url)
   {
       sectionFactory.getSectionInformation(section_id, section_list_url)
           .success(function (sectionData) {
               $scope.section = sectionData;

               //set address, time, dates, topic in section edition ui
               for(var i = 0; i < sectionData.section_program.length; i++)
               {
                    if(sectionData.section_program[i].identifier == 0)
                    {
                        $scope.new_course_address_january    = sectionData.section_program[i].location;
                        $scope.new_course_time_january       = sectionData.section_program[i].time;
                        $scope.new_course_dates_january      = sectionData.section_program[i].dates;
                        $scope.new_course_topic_january      = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 1)
                    {
                        $scope.new_course_address_february   = sectionData.section_program[i].location;
                        $scope.new_course_time_february      = sectionData.section_program[i].time;
                        $scope.new_course_dates_february     = sectionData.section_program[i].dates;
                        $scope.new_course_topic_february     = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 2)
                    {
                        $scope.new_course_address_march      = sectionData.section_program[i].location;
                        $scope.new_course_time_march         = sectionData.section_program[i].time;
                        $scope.new_course_dates_march        = sectionData.section_program[i].dates;
                        $scope.new_course_topic_march        = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 3)
                    {
                        $scope.new_course_address_april      = sectionData.section_program[i].location;
                        $scope.new_course_time_april         = sectionData.section_program[i].time;
                        $scope.new_course_dates_april        = sectionData.section_program[i].dates;
                        $scope.new_course_topic_april       = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 4)
                    {
                        $scope.new_course_address_may        = sectionData.section_program[i].location;
                        $scope.new_course_time_may           = sectionData.section_program[i].time;
                        $scope.new_course_dates_may          = sectionData.section_program[i].dates;
                        $scope.new_course_topic_may          = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 5)
                    {
                        $scope.new_course_address_june       = sectionData.section_program[i].location;
                        $scope.new_course_time_june          = sectionData.section_program[i].time;
                        $scope.new_course_dates_june         = sectionData.section_program[i].dates;
                        $scope.new_course_topic_june         = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 6)
                    {
                        $scope.new_course_address_july       = sectionData.section_program[i].location;
                        $scope.new_course_time_july          = sectionData.section_program[i].time;
                        $scope.new_course_dates_july         = sectionData.section_program[i].dates;
                        $scope.new_course_topic_july         = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 7)
                    {
                        $scope.new_course_address_august     = sectionData.section_program[i].location;
                        $scope.new_course_time_august        = sectionData.section_program[i].time;
                        $scope.new_course_dates_august       = sectionData.section_program[i].dates;
                        $scope.new_course_topic_august       = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 8)
                    {
                        $scope.new_course_address_september  = sectionData.section_program[i].location;
                        $scope.new_course_time_september     = sectionData.section_program[i].time;
                        $scope.new_course_dates_september    = sectionData.section_program[i].dates;
                        $scope.new_course_topic_september    = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 9)
                    {
                        $scope.new_course_address_october    = sectionData.section_program[i].location;
                        $scope.new_course_time_october       = sectionData.section_program[i].time;
                        $scope.new_course_dates_october      = sectionData.section_program[i].dates;
                        $scope.new_course_topic_october      = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 10)
                    {
                        $scope.new_course_address_november   = sectionData.section_program[i].location;
                        $scope.new_course_time_november      = sectionData.section_program[i].time;
                        $scope.new_course_dates_november     = sectionData.section_program[i].dates;
                        $scope.new_course_topic_november     = sectionData.section_program[i].topic;
                    }
                    else if(sectionData.section_program[i].identifier == 11)
                    {
                        $scope.new_course_address_december   = sectionData.section_program[i].location;
                        $scope.new_course_time_december      = sectionData.section_program[i].time;
                        $scope.new_course_dates_december     = sectionData.section_program[i].dates;
                        $scope.new_course_topic_december     = sectionData.section_program[i].topic;
                    }

               }

           })
           .error(function (error) {
               $scope.status = 'Unable to load section data: ' + error.message;
           });
   }

   $scope.save_program = function(section_dates, section_time, section_address, section_topic, action)
   {
        var new_section_data = {};
        var section_program_all = [];

        for(var i = 0; i < $scope.coursedate_month_name.length; i++)
        {
            //replace dates dd/mm/yyyy by dd-mm-yyyy
            var find = '/';
            var re = new RegExp(find, 'g');
            var section_dates_list = section_dates[i].replace(re, '-');

            var section_program = {};
            //create json data to upload
            section_program["identifier"] = i;
            section_program["month"] = $scope.coursedate_month_name[i];
            section_program["location"] = section_address[i];
            section_program["dates"] = section_dates_list;
            section_program["time"] = section_time[i];
            section_program["topic"] = section_topic[i];

            section_program_all.push(section_program);
        }

        new_section_data["section_program"] = section_program_all;

        if(action == 'save')
        {
            sectionFactory.addSection(new_section_data)
               .success(function (sectionsData) {
                   $('#modalsuccess').modal('show')
               })
               .error(function (error) {
                   $scope.status = 'Unable to load sections data: ' + error.message;
                   $('#modalfailure').modal('show')
               });
        }
        else if(action == 'update')
        {
            sectionFactory.updateSection($scope.section_id, new_section_data)
               .success(function (sectionsData) {
                   $('#modalsuccess').modal('show')
               })
               .error(function (error) {
                   $scope.status = 'Unable to load sections data: ' + error.message;
                   $('#modalfailure').modal('show')
               });
        }
   }

   $scope.download_pdf_program_section = function(section_id)
   {

         var the_body = [];

         var headers = [{ text: 'Mois', style: 'tableHeader' }, { text: 'Dates', style: 'tableHeader'}, { text: 'Heures', style: 'tableHeader' }, { text: 'Lieu', style: 'tableHeader' }, { text: 'Cours', style: 'tableHeader' }];
         the_body.push(headers);

         for(var i = 0; i < $scope.section.section_program.length; i++)
         {
            var single_cours_month = [];
            single_cours_month.push($scope.section.section_program[i].month);
            single_cours_month.push($scope.section.section_program[i].dates);
            single_cours_month.push($scope.section.section_program[i].time);
            single_cours_month.push($scope.section.section_program[i].location);
            single_cours_month.push($scope.section.section_program[i].topic);
            the_body.push(single_cours_month);
         }

         var docDefinition = {

            // by default we use portrait, you can change it to landscape if you wish
            pageOrientation: 'landscape',

            content: [
              { text: 'Samaritains de Martigny', fontSize: 17, bold: true, margin: [0, 20, 0, 8] },
              { text: 'Programme annuel ' + $scope.year, fontSize: 14, bold: true, margin: [0, 20, 0, 8] },
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
        var name_download = "Programme_Annuel_Samaritains_Martigny_" + $scope.year + ".pdf";
        pdfMake.createPdf(docDefinition).download(name_download);

   }

}]);
