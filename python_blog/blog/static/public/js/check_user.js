/*
 *version:0.6
 *online;2013-06-30
 *author:scpman
 *online_site:http://scpman.com http://ddser.com
 *mail:freeddser@gmail.com
 */
function ck_email()
            {
              var temp = document.getElementById("email");
              //对电子邮件的验证
             var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
             if(!myreg.test(temp.value))
                  {
                       alert('提示\n\n请输入有效的E_mail！');
                       myreg.focus();
                        return false;
                   }
            }

function ck_user(s)
{
    var t = document.getElementById("user1");
    var re = /^[0-9a-z \u4e00-\u9fa5]+$/gi;
    if(!re.test(t.value))
    {
        alert('提示\n\n用户名只可以是中文，字母，下划线，和数字！');
        re.focus();
        return false;
    }

}