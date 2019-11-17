from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

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

def get_weather():
    """
    Downloads the page where the weather and returns
    """
    url = 'https://weather.com/en-GB/weather/today/l/53.20,-0.36?par=google'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        """
        get the original div that contains the weather as a string phrase:
        [<div class="today_nowcard-phrase">Cloudy</div>]
        then split() twice to extract phrase (eg. 'Cloudy')
        """
        weather_today = str(html.find_all(class_='today_nowcard-phrase')).split(">")[1].split("<")[0]

        
        file = open('weather.txt', 'a')
        file.write (weather_today)
        file.close()
        
print("Starting....")

get_weather()

print("...Finished.")











