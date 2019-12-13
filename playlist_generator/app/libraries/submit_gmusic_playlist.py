from gmusicapi import Musicmanager

def submitPlaylistToGMusic(request):

    auth_code = request.GET.get('gmusicauthcode')

    mm = Musicmanager()
    # after running api.perform_oauth() once:
    if not mm.login(auth_code):
        return 'Failed to login'

    return 'Logged in successfully'