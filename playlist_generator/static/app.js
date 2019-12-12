
if ( checkCookie('gmusicAuthCode') ) {
    $('.GMusicAuth').hide();
    $('.GMusicRefreshAuth').show();
}
else {
    $('.GMusicAuth').show();
    $('.GMusicRefreshAuth').hide();
}
