/*
 *version:0.6
 *online;2013-06-30
 *author:scpman
 *online_site:http://scpman.com http://ddser.com
 *mail:freeddser@gmail.com
 */

function atc_edit_js(b)
{
    var atcid=b;
    url="/admin/manager/article/edit/"+atcid+'/'
    document.getElementById('man_atc_form').action = url;
    document.getElementById('man_atc_form').method = 'GET';

}


function add_newclass(){
    str = "<form action='/admin/manager/article/class/add/' method='POST' /><td>"

    str+= "<input type='text' name='new_class_name' value='新分类名字'/></td>"
    str+="<td colspan='3' align='center'><input type='submit' name='add' value='add'>"
    str+="</td></tr></form>"
    addclass.innerHTML = str;

}


function del_atcchk_js() {

    if (!confirm("确认要删除吗?")) {
        window.event.returnValue = false;
    }
    else{
        var value="";
        for (var i=0;i<atc_chk.length;i++ ){
            if(atc_chk[i].checked){
                value=value+atc_chk[i].value + ",";
            }

        }
        url="/admin/manager/article/delete/"
        document.getElementById('man_atc_form').action = url;
        document.getElementById('man_atc_form').method = 'POST';
    }

}

function delfirm(){
    if (!confirm("确认要删除吗?")) {
        window.event.returnValue = false;
    }
}



function link_del(b)
{
    var atc_str=document.getElementById("search_atcs").value
    if (atc_str=='' || atc_str==null)
    {
        alert('请输入关键字');
        return false;
    }
    window.location.href="/article/search/?search_atcs="+atc_str;


}


