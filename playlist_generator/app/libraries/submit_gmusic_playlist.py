import oauth2client
import gmusicapi
import random

def submitPlaylistToGMusic(request):

    auth_code = request.GET.get('gmusicauthcode')

    mm = Musicmanager()
    
    try:
        if not mm.perform_oauth(auth_code) and mm.login():
            return 'Failed to login'
    except Exception as e:
        return e

    return 'Logged in successfully'
    
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
    def __init__(self):
        self.creds = None
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