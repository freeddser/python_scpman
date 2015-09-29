/*
 *version:0.6
 *online;2013-06-30
 *author:scpman
 *online_site:http://scpman.com http://ddser.com
 *mail:freeddser@gmail.com
 */

function is_mood_del(moodid) {
    if (!confirm("del?")) {
        window.event.returnValue = false;
    }
    else{
        url="/admin/manager/mood/delete/"+moodid+'/'
        document.getElementById('mood_form').action = url;
        document.getElementById('mood_form').method = 'POST';

    }
}







