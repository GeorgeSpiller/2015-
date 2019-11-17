from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from urllib.request import *
import http.cookiejar
#import cookielib
import mechanize
from lxml import html
import requests



def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    print(e)

def Login():
    usrname = input("enter username:")
    passwrd = input("enter Password:")
    login_url = "https://www.instagram.com/accounts/login/"


    payload = {
        "username": "<USER NAME>",
        "password": "<PASSWORD>",
        "csrf_token": "<CSRF_TOKEN>"
    }
    session_requests = requests.session()
    
    result = session_requests.get(login_url)
    tree = html.fromstring(result.text)
    print(list(set(tree.xpath("//input[@name='csrf_token']/@value"))))
    authenticity_token = list(set(tree.xpath("//input[@name='csrf_token']/@value")))[0]

    result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
    )

    
"""
    br = mechanize.Browser()
    #br.set_all_readonly(False)    # allow everything to be written to
    br.set_handle_robots(False)   # ignore robots
    #br.set_handle_refresh(False)  # can sometimes hang without this

    response = br.open(url)

    #br.form = list(br.forms())[0]  # use when form is unnamed

    for form in br.forms():
        print ("Form name:", form.name)
        print (form)
        
    print(br.form)
    
    for control in br.form.controls:
        print (control)
        print ("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))

    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open("https://www.instagram.com/accounts/login/")#Url that contains signin form
    br.select_form(nr=0)
    br['username'] = usrname	#see what is the name of txt input in form
    br['password'] = passwrd
    result = br.submit().read()
    f=file('s.html', 'w')
    f.write(result)
    f.close()
    """
    
"""
<input class="_2hvTZ pexuQ zyHYP" id="f28c1636e7997f4"
aria-label="Phone number, username, or email"
aria-required="true" autocapitalize="off"
autocorrect="off" maxlength="75" name="username"
type="text" value="Test Data"
wtx-context="AF4A0A12-DE34-4FA2-A79F-BDE21A635D3A">

    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("https://www.instagram.com/accounts/login/?source=auth_switcher")

    username = input("Username: ")
    pssword = input("Password: ")
    
    br.select_form(nr=0)
    br.form['username'] = username
    br.form['password'] = password
    br.submit()
    print (br.response().read())
    


"""





"""
    url = 'https://www.bbc.co.uk/'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        tag = html.h3

        for h3 in html.select('h3'):
            print(h3.string)
"""

print("Starting....")

"""
 - log into instergram
 - get top hashes
"""

Login()


print("...Finished.")




















    
