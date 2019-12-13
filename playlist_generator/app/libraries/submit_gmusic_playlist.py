from gmusicapi import Musicmanager

def submitPlaylistToGMusic(request):

    auth_code = request.GET.get('gmusicauthcode')

    mm = Musicmanager()
    
    try:
        if not mm.login(auth_code):
            return 'Failed to login'
    except Exception as e:
        return e

    return 'Logged in successfully'