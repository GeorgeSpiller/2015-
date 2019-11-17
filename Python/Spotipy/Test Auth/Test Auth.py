import spotipy

import sys
import spotipy.util as util

#URL: https://open.spotify.com/user/georgespiller14?si=obzOahqqTamieRcJxQx-8w
#URI: spotify:user:georgespiller14

# Set up aut token

username = georgespiller14
scope = ""
app_redirect_url = "https://google.com/"

SPOTIPY_CLIENT_ID='your-spotify-client-id'
SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
SPOTIPY_REDIRECT_URI='your-app-redirect-url'


token = util.prompt_for_user_token(username, scope)
