/**
 * Created with PyCharm.
 * User: Administrator
 * Date: 13-7-20
 * Time: 下午7:54
 * To change this template use File | Settings | File Templates.
 */

function atc_search(b)
{
    var atc_str=document.getElementById("search_atcs").value
    if (atc_str=='' || atc_str==null)
    {
        alert('请输入关键字');
        return false;
    }
    window.location.href="/article/search/?search_atcs="+atc_str;


}
