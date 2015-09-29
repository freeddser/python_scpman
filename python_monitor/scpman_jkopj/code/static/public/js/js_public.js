/*
 *version:0.6
 *online;2013-06-30
 *author:scpman
 *online_site:http://scpman.com http://ddser.com
 *mail:freeddser@gmail.com
 */


function ck_ip(id)
{
    str =  document.getElementById(id).value;
    str = str.match(/(\d+)\.(\d+)\.(\d+)\.(\d+)/g);
    if (str == null){
        alert("你输入的IP地址无效");
        return false;
    }else if (RegExp.$1>255 || RegExp.$2>255 || RegExp.$3>255 || RegExp.$4>255){
        alert("你输入的IP地址无效");
        return false;
    }else{
//        alert("你输入的IP地址有效");
        return true;
    }
}


function checkbox_xiu_2(id)
{
    var chk = document.getElementById(id);
    if(chk.checked){

    document.getElementById('portnum').style.display = "block";

    }else{
    document.getElementById('portnum').style.display = "none";
    }

}

function check_num(id)
{
    var idReg=/^[1-9][0-9]*$/; // 数字
    var num=document.getElementById(id).value;
    if (!idReg.test(num)){
        alert('非法输入，端口只能是数字');
    }
}


/*主机记录处理部分*/


function host_edit(id) {
    var id=id;
    url="/admin/manager/hostmonitor/edit/"+id+"/"
    document.getElementById('hsform').action = url;
    document.getElementById('hsform').method = 'GET';
}



function host_disable(id) {
    if (!confirm("确认要禁用?")) {
        window.event.returnValue = false;
    }
    else{
        var id=id;
        url="/admin/manager/hostmonitor/disabled/"+id+"/"
        document.getElementById('hsform').action = url;
        document.getElementById('hsform').method = 'GET';

    }
}
