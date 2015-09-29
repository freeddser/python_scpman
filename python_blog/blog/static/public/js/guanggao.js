var roll_pic_width = 950;
var roll_pic_height = 200;
var roll_text_height = 0; 
var roll_bgcolor = '#EFEFEF'; 
var roll_flash = '/static/views/users/images/roll_pic_new.swf';
var roll_pic_ary = new Array(Array(0),Array(0),Array(0),
Array(roll_pic_width,roll_pic_height,roll_text_height,roll_bgcolor,roll_flash));

roll_pic_ary[0].push("/static/views/users/images/banner2.jpg");
roll_pic_ary[1].push(escape("#"));
roll_pic_ary[2].push("�ٳ�������");
roll_pic_ary[0].push("/static/views/users/images/banner3.jpg");
roll_pic_ary[1].push(escape("#"));
roll_pic_ary[2].push("΢��banner");
roll_pic_ary[0].push("/static/views/users/images/banner4.jpg");
roll_pic_ary[1].push(escape("#"));
roll_pic_ary[2].push("�ֻ�Ӫҵ��");
roll_pic_ary[0].push("/static/views/users/images/banner5.jpg");
roll_pic_ary[1].push(escape("#"));
roll_pic_ary[2].push("��������ٶȵ���");
roll_pic_ary[0].push("/static/views/users/images/banner6.jpg");
roll_pic_ary[1].push(escape("#"));
roll_pic_ary[2].push("�����ֻ�");

roll_pic_ary[0].push("/static/views/users/images/banner7.jpg");
roll_pic_ary[1].push(escape("#"));
roll_pic_ary[2].push("���Ŀ�");

roll_pic_ary[0].push("/static/views/users/images/banner8.jpg");
roll_pic_ary[1].push(escape("#"));
roll_pic_ary[2].push("�ּ�ͥ ��ɵļ�");
roll_pic_ary[0].push("images/b8.jpg");
roll_pic_ary[1].push(escape("#"));
roll_pic_ary[2].push("ȫ��3G��������");

function roll_pic_flash(roll_pic_ary) {
 var w   = roll_pic_ary[3][0];
 var h   = roll_pic_ary[3][1];
 var text_h  = roll_pic_ary[3][2];
 var bgcolor  = roll_pic_ary[3][3];
 var roll_swf = roll_pic_ary[3][4];
 var swf_height = h + text_h;
 var pics  = roll_pic_ary[0].join("|");
 var links  = roll_pic_ary[1].join("|");
 var texts  = roll_pic_ary[2].join("|");
 return '<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0" width="'+ w +'" height="'+ swf_height +'"><param name="default_url" value="http://www.hbw.cn/"><param name="allowScriptAccess" value="sameDomain"><param name="movie" value="' + roll_swf + '"><param name="quality" value="high"><param name="bgcolor" value="'+bgcolor+'"><param name="menu" value="false"><param name="wmode" value="transparent"><param name="improved_by" value="http://vod.hai169.com/"><param name=wmode value="opaque"><param name="FlashVars" value="pics='+pics+'&links='+links+'&texts='+texts+'&borderwidth='+w+'&borderheight='+h+'&textheight='+text_h+'"><embed src="' + roll_swf + '" wmode="opaque" FlashVars="pics='+pics+'&links='+links+'&texts='+texts+'&borderwidth='+w+'&borderheight='+h+'&textheight='+text_h+'" menu="false" bgcolor="'+bgcolor+'" quality="high" width="'+ w +'" height="'+ h +'" allowScriptAccess="sameDomain" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" /></object>';

}
document.write(roll_pic_flash(roll_pic_ary));
