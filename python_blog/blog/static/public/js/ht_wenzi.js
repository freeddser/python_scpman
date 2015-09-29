/*
 *version:0.6
 *online;2013-06-30
 *author:scpman
 *online_site:http://scpman.com http://ddser.com
 *mail:freeddser@gmail.com
 */

text = new Array('对','一','个','城','市','的','留','恋',',','<br>','其','实','只','是','留','恋','那','里','的','人','和','事',',','<br>','更','多','的',',','是','沉','淀','在','这','个','城','市','里','自','己','最','好','的','年','华','.',' ',' ',' ',' ','-','-','B','y','  ','S','c','p','m','a','n');
i   = 0;
str = "";

function wz_print(){
    str += text[i];
    wenzi.innerHTML = str;
    i++;

    if (i<text.length){

        setTimeout("wz_print()",400);
    }
}
