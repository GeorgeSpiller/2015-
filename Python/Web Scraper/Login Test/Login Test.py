import requests

def login():
    with requests.Session() as c:
        url = "http://testing-ground.scraping.pro/login"
        Username = "admin"
        Password = "12345"
        c.get(url)#Visit the site first, so that its cookie is loaded into the browser
        #This is important as the cookie contains the csrf token, which is used
        #to verify that the user is not cross sitescripting, and that they are loging
        #in from their page, so we generate this by visiting the site first and then
        #extracting the token from the browsercookie where it is stored as 'csrftoken'
        page = c.get(url)
        print(page)#Dont think we actualy visit the url resulting in no cookie being saved. ???? page returns <Response [200]>

        #print(c.cookies)
        #csrftoken = c.cookies['csrftoken']

        login_data = dict(csrfmiddlewaretoken=csrftoken, username=Username, password=Password, next='/')
        #the format of the post is token, usrname, passwrd, next
        #next is the url of where that page will take you to next, if the login is sucessful,
        #in this case '/' means the root of the page
        c.post(url, data=login_data, headers="Referer : http://testing-ground.scraping.pro/login")
        #we add a header as some login pages go not accept post requests with empty headers
        page = c.get('http://testing-ground.scraping.pro/login?mode=welcome')
        print (page.content)

print("starting...")

login()

print("...finished")
