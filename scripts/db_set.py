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
import sys
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
    print "--------------------------------------------\n";

    return options

def loadData(path):
    data = {}
    with open(path) as data_file:
        data = json.load(data_file)

    if options.verbosity:
        pprint(data)

    return data

def postData(data, url):

    import urllib2,json

    if options.verbosity:
        print "POST data: %s"%data

    postdata = data

    req = urllib2.Request(url)
    req.add_header('Content-Type','application/json')
    data = json.dumps(postdata)

    response = urllib2.urlopen(req,data)
    return response

def getData(url):

    import urllib2,json

    if options.verbosity:
        print "GET data: %s"%data

    req = urllib2.Request(url)
    req.add_header('Content-Type','application/json')

    response = urllib2.urlopen(req)
    if options.verbosity:
        print response.geturl()
        print response.info()
        print response.getcode()
        pprint(json.loads(response.read()))
    return response

def deleteData(url):

    import urllib2,json

    if options.verbosity:
        print "DELETE data: %s"%data

    req = urllib2.Request(url)
    req.add_header('Content-Type','application/json')
    req.get_method = lambda: 'DELETE' # creates the delete method

    response = urllib2.urlopen(req)
    print ".",
    sys.stdout.flush()

    if options.verbosity:
        print response.geturl()
        print response.info()
        print response.getcode()
        pprint(json.loads(response.read()))
    return response

def fill_db(data):
    global web_url
    for key in data:
        if key != "urlmap":
            print "\nPopulating %s..."%key
            if options.verbosity:
                pprint(data[key])
            for one_data in (data[key]):
                url_end = data["urlmap"][key]
                url_endpoint = web_url+url_end
                response = postData(one_data, url_endpoint)
                print ".",
                sys.stdout.flush()
                if options.verbosity:
                    print url_endpoint
                    print response.geturl()
                    print response.info()
                    print response.getcode()
                    pprint(one_data)
    print "\nFinished data population\n"

def retrieve_db(data):
    global web_url
    for key in data:
        if key != "urlmap":
            print "\nRetrieving %s..."%key
            if options.verbosity:
                pprint(data[key])
            url_end = data["urlmap"][key]
            url_endpoint = web_url+url_end
            getData(url_endpoint)
            print ".",
            sys.stdout.flush()
            if options.verbosity:
                print url_endpoint
                print response.geturl()
                print response.info()
                print response.getcode()
                pprint(one_data)
    print "\nFinished retrieving all data\n"

def delete_db(data):
    global web_url
    for key in data:
        if key != "urlmap":
            print "\nDeleting %s..."%key
            if options.verbosity:
                pprint(data[key])
            url_end = data["urlmap"][key]
            url_endpoint = web_url+url_end
            response = getData(url_endpoint)
            json_response = json.loads(response.read())
            for one_data in json_response:
                url_endpoint_id = url_endpoint + unicode(one_data["id"])
                deleteData(url_endpoint_id)
                if options.verbosity:
                    print "delete data"
                    pprint(one_data)
                    pprint(one_data["id"])
            if options.verbosity:
                print url_endpoint
                print response.geturl()
                print response.info()
                print response.getcode()
                pprint(one_data)
    print "\nFinished deleting all data\n"

#=========================================================
# EXPERIMENTS LAUNCHED
#=========================================================
def end():
    print "End of program\n";
    print strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())

#=========================================================
# MAIN FUNCTION DEFINITION
#=========================================================
def main():
    global options
    software_description()
    options = parse_options()
    data = loadData(options.json_file)
    fill_db(data)
    retrieve_db(data)
    delete_db(data)
    end()

#=========================================================
# MAIN
#=========================================================
if __name__ == '__main__':
    main()
