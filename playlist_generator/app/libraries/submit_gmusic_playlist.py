from gmusicapi import Musicmanager
import oauth2client

def submitPlaylistToGMusic(request):

    auth_code = request.GET.get('gmusicauthcode')

    mm = Musicmanager()
    
    try:
        if not mm.login(auth_code):
            return 'Failed to login'
    except Exception as e:
        return e

    return 'Logged in successfully'
    
class _OAuthClient(gmusicapi.clients.shared._Base):
    @classmethod
    def perform_oauth(cls, auth_code):
        # print(cls._session_class.oauth._asdict())
        flow = oauth2client.client.OAuth2WebServerFlow(**cls._session_class.oauth._asdict())
        uri = flow.step1_get_authorize_url()
        creds = flow.step2_exchange(auth_code)
        cls.creds = creds
        return creds
        
    def _oauth_login(self):
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
        try:
            self._make_call(gmusicapi.protocol.musicmanager.AuthenticateUploader,
                            '00:11:22:33:44:55',
                            'tc-music (gmusicapi-{0})'.format(gmusicapi.__version__))
        except CallFailure:
            self.session.logout()
            return False
        return True

    def logout(self):
        return super(Musicmanager, self).logout()