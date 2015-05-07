#!/usr/bin/env python
########################################################################
# \file fill_db.py                                                     #
#                                                                      #
# SCORE              / The goal is to populate samaweb database with   #
#                      information                                     #
#                                                                      #
# This program is free software; you can redistribute it and/or modify #
# it under the terms of the associated license. For more information   #
# about these matters, see the file named COPYING.                     #
#                                                                      #
# \date    May 2015                                                    #
# \author  Flavio Tarsetti (tarsetti dot flavio at gmail dot com)      #
#                          tarsetti.flavio@gmail.com                   #
#                                                                      #
# Copyright (c) 2015 - Flavio Tarsetti Software                        #
########################################################################

import os
from optparse import OptionParser
from time import localtime, strftime
import json
from pprint import pprint

#=========================================================
# GLOBAL VARS
#=========================================================

# Program information
Version = "1.0"
Project = "SAMAWEB"
program_description = """--------------------------------------------
**Fill the database with information**
Version : %s"""%Version+"""\nProject  : %s"""%Project+"""\n--------------------------------------------"""

# Program settings
path_json   = 'db_fill/course.json'
web_url     = 'http://localhost:5000/api/'
options     = {}

#=========================================================
# LOCAL FUNCTIONS DEFINITION
#=========================================================

def software_description():
    print program_description

    #Program specification
    print "\nBegin database population on :"
    os.system('hostname')
    print strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
    print "\n"

def parse_options():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.set_description("***Face Localizer***")

    parser.add_option("--json_file",dest="json_file", help = "json file with data",default="")
    parser.add_option("-v","--verbose",dest="verbosity", action="store_true", help="need more verbosity?", default=False)
    parser.add_option("-q","--no_verbose",dest="verbosity", action="store_false", help="need more verbosity?", default=False)

    try:
        (options,args) = parser.parse_args()
    except:
        parser.error("cmdline error")
        sys.exit(-1)

    #if len(args) < 1:
    #    parser.error("incorrect number of arguments")

    print "--------------------------------------------"
    print "  json file: %s"% options.json_file
    print "  verbosity: %s" % options.verbosity
    print "--------------------------------------------\n\n";

    return options

def loadData(path):
    data = {}
    print path
    with open(path) as data_file:
        print data_file
        data = json.load(data_file)
        print data

    if options.verbosity:
        pprint(data)

    return data

def postData(data, url):

    import urllib2,json

    print data
    postdata = data

    req = urllib2.Request(url)
    req.add_header('Content-Type','application/json')
    data = json.dumps(postdata)

    response = urllib2.urlopen(req,data)
    return response

def fill_db(data):
    for key in data:
        print key
        if key != "urlmap":
            print "\nPopulating %s..."%key
            if options.verbosity:
                pprint(data[key])
            pprint(data[key])
            #for one_data in (data[key]):
            #    response = postData(one_data, web_url)
            #    print response.geturl()
            #    print response.info()
            #    print response.getcode()
            #    print ".",
            #    if options.verbosity:
            #        pprint(one_data)

#=========================================================
# MAIN FUNCTION DEFINITION
#=========================================================

def main():
    global options
    software_description()
    options = parse_options()
    data = loadData(path_json)
    fill_db(data)

#=========================================================
# MAIN
#=========================================================

if __name__ == '__main__':
    main()
