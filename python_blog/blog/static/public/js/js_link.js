function link_del(id) {
    if (!confirm("确认要删除吗?")) {
        window.event.returnValue = false;
    }
    else{
        url="/admin/manager/url_link/delete/"+id+'/'
        document.getElementById('link_form').action = url;
        document.getElementById('link_form').method = 'GET';

    }
}


function link_xiugai(id) {

        url="/admin/manager/url_link/edit/"+id+'/'
        document.getElementById('link_form').action = url;
        document.getElementById('link_form').method = 'GET';

}