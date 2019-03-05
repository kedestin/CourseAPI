#!/usr/bin/python3
# Required version 3.6 or higher

import requests
import json
import inspect
from pathlib import Path


BASE_URL = "https://siscs.uit.tufts.edu/"

"""SIS course search api endpoints
"""
endpoints = {
    "getCareer":     ("psc/csprod/EMPLOYEE/HRMS/s/WEBLIB_CLS_SRCH.ISCRIPT1."
                      "FieldFormula.IScript_getCareers"),
    "getSubjects":   ("psc/csprod/EMPLOYEE/HRMS/s/WEBLIB_CLS_SRCH.ISCRIPT1."
                      "FieldFormula.IScript_getSubjects"),
    "getAttributes": ("psc/csprod/EMPLOYEE/HRMS/s/WEBLIB_CLS_SRCH.ISCRIPT1."
                      "FieldFormula.IScript_getAttributes"),
    "getCourseNumbers":  ("psc/csprod/EMPLOYEE/HRMS/s/WEBLIB_CLS_SRCH.ISCRIPT1."
                      "FieldFormula.IScript_getCourseNumbers"),
    "getTerms":      ("psc/csprod/EMPLOYEE/HRMS/s/WEBLIB_CLS_SRCH.ISCRIPT1."
                      "FieldFormula.IScript_getTerms"),
    "performSearch": ("psc/csprod/EMPLOYEE/HRMS/s/WEBLIB_CLS_SRCH.ISCRIPT1."
                      "FieldFormula.IScript_getSearchresultsAll3")

}


def cookiefy(cookie):
    """Returns a string representation of a cookie dictionary

    Arguments:
        cookie {dict} -- dictionary of cookies and values

    Returns:
        str -- stringified cookie
    """
    return "; ".join([str(x)+"="+str(y) for x, y in cookie.items()])


def fetchPSTOKEN():
    """Retrives a PS_TOKEN from the web

    Returns:
        str -- PS_TOKEN
    """
    # This page's response tells the browser to set the PS_TOKEN cookie
    url = ("https://sis.uit.tufts.edu/psp/paprod/EMPLOYEE/EMPL/h/"
           "?tab=PAPP_GUEST")

    session = requests.Session()
    session.get(url)
    return session.cookies.get_dict()["PS_TOKEN"]


def getPSTOKEN(mode=""):
    """Returns a PS_wTOKEN (required for requests)
       The returned PS_TOKEN is cached in a local file

    Keyword Arguments:
        mode {str} -- if set to bypassCache, PS_TOKEN will be fetched from the 
                      web (default: {""})

    Returns:
        string -- PS_TOKEN
    """

    cacheTOK = Path("./.tufts_courses_cookie_PS_TOKEN")
    PS_TOKEN = None

    if cacheTOK.is_file() and not mode == "bypassCache":
        PS_TOKEN = cacheTOK.read_text()
    else:
        PS_TOKEN = fetchPSTOKEN()
        cacheTOK.write_text(PS_TOKEN)

    return PS_TOKEN


"""
    Cookie (Required for requests to succeed):
        PS_TOKEN   (guess: Probably an access token. These are assigned when 
                           a user first connects to SIS. They seem to get 
                           invalidated after some period of time)
        ExpirePage (guess: I'm not really sure. It doesn't seem to matter what 
                           the value is, so long as it's prefixed with 
                           "https://sis.uit.tufts.edu/psp/paprod/".
                           The value itself doesn't even need to be a valid
                           url)
"""
cookie = {
    "PS_TOKEN": getPSTOKEN(),
    "ExpirePage": "https://sis.uit.tufts.edu/psp/paprod/"
}


"""Request headers
"""
headers = {
    'Cookie': cookiefy(cookie),
    'cache-control': "no-cache",
}


def courseEndpoint(func):
    """Decorator that wraps each endpoint with the request logic
    """

    def sendRequest(*args, **kwargs):
        # Use param dictionary as query string
        querystring = func(*args, **kwargs)
        # Get url from endpoint dicitonary
        url = BASE_URL + endpoints[func.__name__]

        try:
            return requests.get(url, headers=headers, params=querystring).json()

        except json.decoder.JSONDecodeError:  # If request is malformed,
                                              # an html page is returned

            # Retry request with a new token from the web
            cookie["PS_TOKEN"] = getPSTOKEN("bypassCache")
            headers["Cookie"]  = cookiefy(cookie)

            return requests.get(url, headers=headers, params=querystring).json()
    return sendRequest


@courseEndpoint
def getCareer():
    """Gets all terms for all schools - (JSON representation of dropdown menu)

    Returns:
        JSON -- List of objects for each school, each containing term lists
    """
    return locals()  # querystring for request, not the actual function return


@courseEndpoint
def getSubjects(term, career):
    """Gets list of course subjects

    Arguments:
        term   {int} -- id corresponding to a term
        career {str} -- identifier for a school or program

    Returns:
        JSON -- List of course subjects objects
    """
    return locals()  # querystring for request, not the actual function return


@courseEndpoint
def getAttributes(term, career):
    """Gets nested lists of course attributes

    Arguments:
        term   {int} -- id corresponding to a term
        career {str} -- identifier for a school or program

    Returns:
        JSON -- Nested list of course attributes (think accordion dropdown
                menu)
    """
    return locals()  # querystring for request, not the actual function return


@courseEndpoint
def getCourseNumbers(term, career, subject):
    """Gets list of course numbers for given subject

    Arguments:
        term    {int} -- id corresponding to a term
        career  {str} -- identifier for a school or program
        subject {str} -- identifier for a course subject

    Returns:
        JSON -- List of course number objects
    """
    return locals()  # querystring for request, not the actual function return


@courseEndpoint
def getTerms(career):
    """Returns a list of terms for a given school or program

    Arguments:
        career {str} -- identifier for a school or program

    Returns:
        JSON -- List of terms
    """
    return locals()  # querystring for request, not the actual function return


@courseEndpoint
def performSearch(term, career="", subject="", crs_number="", attribute="",
                  keyword="", instructor="", searchby="crs_number"):
    """Performs a search given provided criteria

    Arguments:
        term       {int} -- id corresponding to a term

    Keyword Arguments:
        career     {str} -- identifier for a school or program (default: {""})
        subject    {str} -- identifier for a course subject (default: {""})
        crs_number {int} -- course number (default: {""})
        attribute  {str} -- course attribute (default: {""})
        keyword    {str} -- additional keyword (default: {""})
        instructor {str} -- course instructor (default: {""})
        searchby   {str} -- [honestly I have no idea] (default: {"crs_number"})

    Returns:
        JSON -- Returns a list of courses matching the criteria, along with
                relevant information
    """
    return locals()  # querystring for request, not the actual function return
