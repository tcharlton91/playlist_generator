
if ( checkCookie('gmusicAuthCode') ) {
    $('.GMusicAuth').hide();
    $('.GMusicRefreshAuth').show();
}
else {
    $('.GMusicAuth').show();
    $('.GMusicRefreshAuth').hide();
}

function checkCookie($name)
{
    if (typeof $.cookie($name) === 'undefined') {
        return false;
    } else {
        return true;
    }
}
