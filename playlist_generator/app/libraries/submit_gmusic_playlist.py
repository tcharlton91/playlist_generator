import oauth2client
import gmusicapi
import random

from django.http import HttpResponse

def perform_oauth_and_get_credentials(request):

    response = HttpResponse()

    mm = Musicmanager()

    try:
        auth_code = request.GET.get('gmusicauthcode')
        creds = mm.perform_oauth(auth_code)
        if not creds:
            response.write('Failed to perform oauth')

        # possibly need response to be StreamingHttpResponse 
        response.write(creds)
    except Exception as e:
        response.write(str(e))

    print('Performed oauth successfully')

    return response

# this should possibly be an internal function, where you login with the creds,
# and then get_playlist, or submit_songs etc
def login(request):

    response = HttpResponse()

    creds = request.GET.get('gmusicCreds')
    mm = Musicmanager(creds)

    try:
        if not mm.login():
            response.write('Failed to login')
    except Exception as e:
        response.write(str(e))

    response.write('Logged in successfully')

    return response

def import_playlist(request):

    print(request.GET.get('gmusicCreds'))
    print('-----')
    print(request.GET.get('playlist'))

class _OAuthClient(gmusicapi.clients.shared._Base):
    
    def perform_oauth(self, auth_code):
        # print(cls._session_class.oauth._asdict())
        flow = oauth2client.client.OAuth2WebServerFlow(**self._session_class.oauth._asdict())
        uri = flow.step1_get_authorize_url()
        print(uri)
        creds = flow.step2_exchange(auth_code)
        self.creds = creds
        return creds
        
    def _oauth_login(self):
        print(self.creds)
        if not self.session.login(self.creds):
            return False
        
        return True
            
class Musicmanager(_OAuthClient):
    _session_class = gmusicapi.session.Musicmanager
    def __init__(self, creds=None):
        self.creds = creds
        super(Musicmanager, self).__init__(self.__class__.__name__, True, True, True)
        
    def login(self):
        return( self._oauth_login() and self._perform_upauth() )
        
    def _perform_upauth(self):

        mac_address = "52:54:00:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        )

        try:
            self._make_call(gmusicapi.protocol.musicmanager.AuthenticateUploader,
                            mac_address,
                            'tc-music (gmusicapi-{0})'.format(gmusicapi.__version__))
            print('Successfully performed upauth')
        except gmusicapi.exceptions.CallFailure:
            self.session.logout()
            return False
        return True

    def logout(self):
        return super(Musicmanager, self).logout()