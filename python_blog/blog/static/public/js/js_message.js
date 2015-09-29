/**
 * Created with PyCharm.
 * User: Administrator
 * Date: 13-7-28
 * Time: 下午2:01
 * To change this template use File | Settings | File Templates.
 */
function mes_del(id) {
    if (!confirm("确认要删除吗?")) {
        window.event.returnValue = false;
    }
    else{
        url="/admin/manager/message/delete/"+id+'/'
        document.getElementById('mes_form').action = url;
        document.getElementById('mes_form').method = 'POST';

    }
}

function mes_del_old(id) {
    if (!confirm("确认要删除吗?")) {
        window.event.returnValue = false;
    }
    else{
        url="/admin/manager/message/delete_old/"+id+'/'
        document.getElementById('mes_form').action = url;
        document.getElementById('mes_form').method = 'POST';

    }
}



function mes_read(id) {
//    alert(id);

    url="/admin/manager/message/new/"+id+'/'
    document.getElementById('mes_form').action = url;
    document.getElementById('mes_form').method = 'POST';

}