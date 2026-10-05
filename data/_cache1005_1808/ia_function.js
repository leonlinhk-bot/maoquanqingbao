$(function () {
    initial();
    left_menu()
});

function left_menu() {
    menu = false;
    if (location_href.match('digital_onboarding/')) {
        initDigitalBoardingMenu();
        menu = true;
    }
    if (location_href.match('fulfillment_ratio/')) {
        initFulfillmentMenu();
        menu = true;
    }
    if (location_href.match('home_insurance/')) {
        home_insurance_menu();
        menu = true;
    }
    if (location_href.match('medical_insurance/')) {
        initLeftMenu(1);
        menu = true;
    }
    if (location_href.match('participating_policy/')) {
        participating_policy_menu();
        menu = true;
    }
    if (location_href.match('premium_financing/')) {
        premium_financing_menu();
        menu = true;
    }
    if (location_href.match('qualifying_deferred_annuity_policy/')) {
        initQDAPMenu();
        menu = true;
    }
    if (location_href.match('reinsurance_specialty/')) {
        initRSMenu();
        menu = true;
    }
    if (location_href.match('travel_insurance/')) {
        travel_insurance_menu();
        menu = true;
    }
    if (location_href.match('critical_illness_insurance/')) {
        critical_illness_insurance_menu();
        menu = true;
    }
    if (menu == true){
    initMenu();
    }
}

function initial() {
    if (location_href.match('/management_trainee_scheme')) {
        $("#submit").click(function () {
            aboutUs();
        });
    }
    if (location_href.match('/portal_for_insurers/brief/')) {
        $("#submit").click(function () {
            portal_for_insurers();
        });
    }
    if (location_href.match('/portal_for_insurers/lisa/')) {
        $("#submit").click(function () {
            Levy();
        });
    }
    if (location_href.match('register_of_authorized_insurers.html')) {
        register_of_authorized_insurers();
    }
    if (location_href.match('enforcement/faq/faqs_14.html/')) {
        faqs_14();
    }
    if (location_href.match('infocenter/forms/Catastrophe_claims_data.html')) {
        catastrophe_claims();
    }
    if (location_href.match("/press_releases.html")) {
        info_press_releases();
    }
    if (location_href.match("/alert_list.html")) {
        info_alert_list();
    }
    if (location_href.match("/publications_publicity_materials.html")) {
        publications_publicity_materials();
    }
    if (location_href.match("/management_trainee_scheme/index.html")) {
        window.location = "../index.html";
    }
    if (location_href.match("qualifying_deferred_annuity_policy/qdap_tool.html")) {
        $('body').addClass('qdap_section');
    }
    if (location_href.match("qualifying_deferred_annuity_policy/qdap_all.html")) {
        $('body').addClass('qdap_section');
        getQDAP(null);
    }
    if (location_href.match("qualifying_deferred_annuity_policy/qdap_selection_tool.html")) {
        $('body').addClass('qdap_section qdap_index');
    }
    if (location_href.match("search.php")) {
        search();
    }
    if (location_href.match("subscribe.php")) {
        subscribe();
    }
    $('#keyword').keypress(function (e) {
        code = e.keyCode ? e.keyCode : e.which; // in case of browser compatibility
        if (code == 13) {

            e.preventDefault();

            $('#frmSearch').find('input[name=pq\\[\\]]').remove();
            $('#frmSearch').submit();
            return false;
            // do something
            /* also can use return false; instead. */
        }
    });

}

$(window).load(function () { speeches_articles(); });

function speeches_articles() {
    var select_year = getUrlParameter("year");
    if (select_year)
        show(select_year);


    $("#speeches_articles_year").change(function () {
        var status = this.value;
        document.location.href = "speeches_articles.html?year=" + this.value;
    });
}

function show(type) {
    var hide_table = true;
    $('#speeches_articles').each(function () {
        if (!$(this).is(":visible")) {
            $(this).show();
        }
        //$('.event_table > tbody  > tr').each(function(index, item) {
        $(this).find('tbody  > tr').each(function (index, item) {
            var sh = false;
            if (index >= 0) {

                $("td", this).each(function (j) {
                    //console.log($(this).text().indexOf(type));

                    if ($(this).text().indexOf(type) >= 0) {
                        sh = true;
                    }

                    return false;
                });
                if (sh) {
                    $(this).show();
                    hide_table = false;
                } else {
                    $(this).hide();
                }
            }
        });
    });
    if (hide_table) {
        //$('#Response_table').hide();
        $('#speeches_articles').after('<center>沒有搜尋結果</center>');

    }

    if (!$('#speeches_articles_year').find("option:contains('" + type + "')").length) {
        $('#speeches_articles_year').val(0);
    } else {
        $('#speeches_articles_year').val(type);
    }
}

function aboutUs() {
    var temp = $('#Why').val();
    if (temp == 1) {
        $('#form1').prop('action', 'why_insurance_authority.html');
        return true;
    }
    if (temp == 2) {
        $('#form1').prop('action', 'management_trainee_scheme.html');
        return true;
    }
    if (temp == 3) {
        $('#form1').prop('action', 'scheme_structure.html');
        return true;
    }
    if (temp == 4) {
        $('#form1').prop('action', 'career_progression.html');
        return true;
    }
    if (temp == 5) {
        $('#form1').prop('action', 'recruitment_process.html');
        return true;
    }
    if (temp == 6) {
        $('#form1').prop('action', 'q_a.html');
        return true;
    }
    return false;
}

function faqs_14() {
    $('.breadcrumb').html('');
    setTimeout(change_breadcrumb, 100);
};

function change_breadcrumb() {
    if (location_href.match('/en')) {
        $('.breadcrumb').html('<a href="../../index.html" class="home">Home</a> <span> > </span> Enforcement > FAQs  > Enforcement');
    } else if (location_href.match('/tc')) {
        $('.breadcrumb').html('<div class="breadcrumb"><a href="../../index.html" class="home">主頁</a> <span> > </span> 法規執行  > 常見問題  > 法規執行</div>');
    } else if (location_href.match('/sc')) {
        $('.breadcrumb').html('<div class="breadcrumb"><a href="../../index.html" class="home">主页</a> <span> > </span> 法规执行  > 常见问题  > 法规执行</div>');
    }
}

function catastrophe_claims() {
    $('.breadcrumb').html('');
    setTimeout(change_breadcrumb2, 100);
};

function change_breadcrumb2(){
    if (location_href.match('/en')) {
        $('.breadcrumb').html('<a href="../../index.html" class="home">Home</a> <span> > </span><a href="../insurance_authority_to_start_regulating_insurance_companies_tomorrow.html">Information Center</a> <span> > </span> <a href="intermediaries.html">Public Forms</a> > <a href="regulatory_returns.html">Regulatory Returns – Insurers</a>  > Catastrophe Claims Data Collection Requirement');
    } else if (location_href.match('/tc')) {
        $('.breadcrumb').html('<div class="breadcrumb"><a href="../../index.html" class="home">主頁</a> <span> > </span><a href="../insurance_authority_to_start_regulating_insurance_companies_tomorrow.html">資源中心</a> <span> > </span> <a href="intermediaries.html">公用表格</a>  > <a href="regulatory_returns.html">保險公司監管申報表</a>  > 巨災索償數據收集規定</div>');
    } else if (location_href.match('/sc')) {
        $('.breadcrumb').html('<div class="breadcrumb"><a href="../../index.html" class="home">主页</a> <span> > </span><a href="../insurance_authority_to_start_regulating_insurance_companies_tomorrow.html">资源中心</a> <span> > </span> <a href="intermediaries.html">公用表格</a>  > <a href="regulatory_returns.html">保险公司监管申报表</a>  > 巨灾索偿数据收集规定</div>');
    }
}
function info_press_releases() {

    $("#year").change(function () {
        var status = this.value;
        document.location.href = "press_releases.html?year=" + this.value;
    });

}

function info_alert_list() {

    $("#year").change(function () {
        var status = this.value;
        document.location.href = "alert_list.html?year=" + this.value;
    });

}

function publications_publicity_materials() {
    var id = getUrlParameter("id");
    if (id != null) {
        if (id == 7)
            $('#collapseSeven').addClass('in');
        if (id == 6)
            $('#collapseSix').addClass('in');
        if (id == 5)
            $('#collapseFive').addClass('in');
        if (id == 4)
            $('#collapseFour').addClass('in')
        if (id == 3)
            $('#collapseTV').addClass('in');
        if (id == 2)
            $('#collapseThree').addClass('in');
        if (id == 1)
            $('#collapseOne').addClass('in');
    }
};

function portal_for_insurers() {

    var temp = $('#overview').val();
    if (temp == 1) {
        $('#form1').prop('action', 'overview.html');
        return true;
    }
    if (temp == 2) {
        $('#form1').prop('action', 'brief_members.html');
        return true;
    }
    if (temp == 3) {
        $('#form1').prop('action', 'news.html');
        return true;
    } if (temp == 4) {
        $('#form1').prop('action', 'events.html');
        return true;
    }
    if (temp == 5) {
        $('#form1').prop('action', 'resources.html');
        return true;
    }
    return false;
}

function Levy() {
    var temp = $('#lisa').val();
    $('#form1').prop('target', '_self');
    if (temp == 1) {
        $('#form1').prop('action', 'important_notes_before_you_proceed.html');
        return true;
    }
    if (temp == 2) {
        $('#form1').prop('target', '_blank');
        $('#form1').prop('action', 'return_submission.html');
        return true;
    }
    if (temp == 3) {
        $('#form1').prop('action', 'download_area.html');
        return true;
    } if (temp == 4) {
        $('#form1').prop('action', 'enquiry.html');
        return true;
    }
    if (temp == 5) {
        $('#form1').prop('action', 'faq.html');
        return true;
    }
    if (temp == 6) {
        $('#form1').prop('action', 'notes_on_collection_of_levy_on_insurance_premium.html');
        return true;
    }
    if (temp == 7) {
        $('#form1').prop('action', 'system_maintenance_schedule.html');
        return true;
    }
    return false;
}
function register_of_authorized_insurers() {
    $.getJSON("register_of_insurers_updateDate.json", function (data) {
        var items = [];
        $.each(data, function (key, val) {
            items.push(val);
        });

        if (location_href.match('/en')) {
            var filename = items[2].toString().split("-");
            $('#download').attr("href", 'register_of_insurers_as_at_' + padding1(filename[2], 2) + padding1(filename[1], 2) + filename[0] + '.xlsx');
            document.getElementById("last_update_date").innerHTML = 'as at ' + items[0];
        }
        if (location_href.match('/tc') || location_href.match('/sc')) {
            var filename = items[2].toString().split("-");
            $('#download').attr("href", 'register_of_insurers_as_at_' + padding1(filename[2], 2) + padding1(filename[1], 2) + filename[0] + '.xlsx');
            document.getElementById("last_update_date").innerHTML = '截至' + items[1];
        }

    });
}
function padding1(num, length) {
    for (var len = (num + "").length; len < length; len = num.length) {
        num = "0" + num;
    }
    return num;
}

var last_revision_date = '<?= date("Y/m/d"); ?>';

function search() {

    $('.printBtn').off().on('click', 'a', function () {
        window.print();
        return false;
    });

    $('.topBtn').off().on('click', 'a', function () {
        window.location.hash = ''; window.location.hash = 'top';
        return false;
    });




    //initSearch();
    $('#btnSearch').click(function () {
        $('#frmSearch').find('input[name=pq\\[\\]]').remove();
        $('#frmSearch').submit();
        return false;
    });
    $('#btnSearchWithinResult').click(function () {
        $('#frmSearch').submit();
        return false;
    });

    function loadFilter(ul) {
        ul.find('>li').each(function () {
            var item = $(this).find('>span');
            var name = item.data('name'),
                val = item.data('value'),
                selected = item.hasClass('selected'),
                count = item.data('count');
            var sublist = $(this).find('>ul');
            $(this).empty();

            text = val;


            if (typeof count === 'undefined') {
                console.log(count);
            } else {
                text += ' (' + count + ')';

            }

            if (selected) {

                var fieldName = $(this).parent().parent().find('.sl_tit').text();
                if (!fieldName)
                    fieldName = $(this).parent().data('subject');

                $('#fqList').append($('<span class="fqListItem"></span>').text(fieldName + ":" + text).append($('<a href="#" class="btnRemoveFilter">&#x2718;</a>').data({
                    name: name,
                    value: val
                })));

                //$(this).append(text).append($('<a href="#" class="btnRemoveFilter">&#x2718;</a>').data({name:name,value:val}));
                $(this).append(text);
            } else {
                $(this).append($('<a href="#" class="filterItem"></a>').data({
                    name: name,
                    value: val
                }).text(text));
            }

            $(this).append(sublist);

            sublist.each(function () {
                loadFilter($(this));
            });

        });
    }


    loadFilter($('.filterItems'));


    $('.filtertree ul>li').each(function () {
        if ($(this).find('ul>li').length > 0) {
            $(this).prepend('<a href="#" class="ctrl"><span class="collapse">-</span><span class="expand">+</span></a>');
        } else {
            $(this).prepend('<a href="#" class="ctrl"><span>&bull;</span></a>');
        }
    });
    $('.filtertree ul li.collapsed>.ctrl').click(function () {
        $(this).parent().toggleClass('collapsed');
        return false;
    });


    //Jacky 20171214
    $('.filterItems:eq(1)>li').each(function (index) {

        if (index >= 6) {
            $(this).hide();
        }
        if (index == 6) {
            $('.filterItems:eq(1)').append('<li style="list-style-type:none"><a href="#" class="showYearItem" >More</a></li>');
        }
    });
    $('.showYearItem').click(function () {
        $('.filterItems:eq(1)>li').each(function (index) {
            $(this).show();
        });
        $(this).parent().hide();
        return false;
    });

    $('.filterItems,#fqList').on('click', 'a', function () {

        var pq = $('#frmSearch').find('input[name=pq\\[\\]]:first');
        $('#keyword').val(pq.val());
        pq.remove();

        var name = $(this).data('name');

        var val = '';
        if (!$(this).hasClass('btnRemoveFilter'))
            val = $(this).data('value');
        $('#frmSearch').find('input[name=' + name + ']').val(val);
        $('#frmSearch').submit();
        return false;
    });

    $('.btnChPage').click(function () {
        var pq = $('#frmSearch').find('input[name=pq\\[\\]]:first');
        $('#keyword').val(pq.val());
        pq.remove();
        $('#frmSearch').find('input[name=sort]').val($(this).siblings('select[name=sort]').val());
        $('#frmSearch').submit();
        return false;
    });

    $('.sd_path>ul').each(function () {
        var menuId = $(this).data('menu-id');
        var menuItem = menuItems[menuId];
        while (menuItem != null) {
            var title = menuItem[0],
                parent = menuItem[6];
            //$(this).prepend($('<li></li>').append($('<a href="#"></a>').text(title)));
            $(this).prepend($('<li></li>').html(title));

            menuId = parent;
            menuItem = menuItems[menuId];
        }
        //$(this).prepend('<li class="fst-child"><a href="#">Home</a></li>');
        $(this).prepend('<li class="fst-child">Home</li>');


    });
    var currentUrl = 'https://' + location.host + location.pathname;
    $('#frmSearch').attr('action', currentUrl);
    $('.search_page a').each(function () {
        if ($(this).attr('href').indexOf(currentUrl) != 0) {
            $(this).attr('href', currentUrl + $(this).attr('href'));
        }
    });




}

function show_year() {
    $('.filterItems:eq(0)>li').each(function (index) {
        $(this).show();
    });
}


/* // 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
    if (location_href.match('/how_to_choose.html')) {
        if (location_href.match('/en')) {
            player = new YT.Player('player', {
                width: '100%',
                videoId: '7oowhygsPug',
                playerVars: { 'autoplay': 1, 'playsinline': 1, 'loop': 1, 'rel': 0 },
                events: {
                    'onReady': onPlayerReady,
                    'onStateChange': onPlayerStateChange
                }
            });
        } else if (location_href.match('/tc') || location_href.match('/sc')) {
            player = new YT.Player('player', {
                width: '100%',
                videoId: 'siacsJL_eAA',
                playerVars: { 'autoplay': 1, 'playsinline': 1, 'loop': 1, 'rel': 0 },
                events: {
                    'onReady': onPlayerReady,
                    'onStateChange': onPlayerStateChange
                }
            });
        }
    }
    else if (location_href.match('/index.html')) {
        if (location_href.match('/en')) {
            player = new YT.Player('player', {
                width: '100%',
                videoId: 'e-UkI8FD_34',
                playerVars: { 'autoplay': 1, 'playsinline': 1, 'loop': 1, 'rel': 0 },
                events: {
                    'onReady': onPlayerReady,
                    'onStateChange': onPlayerStateChange
                }
            });
        } else if (location_href.match('/tc') || location_href.match('/sc')) {
            player = new YT.Player('player', {
                width: '100%',
                videoId: 'siacsJL_eAA',
                playerVars: { 'autoplay': 1, 'playsinline': 1, 'loop': 1, 'rel': 0 },
                events: {
                    'onReady': onPlayerReady,
                    'onStateChange': onPlayerStateChange
                }
            });
        }
    }
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    event.target.mute();
    event.target.playVideo();
}

function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.ENDED) {
        event.target.playVideo();
    }
}
 */

var xmlHttp;

function createXHR() {

    if (window.XMLHttpRequest) {

        xmlHttp = new XMLHttpRequest();
    } else if (window.ActiveXObject) {

        xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");

    }

    if (!xmlHttp) {

        alert("your browser does not support XML HTTP");
    }



}


/*function sendRequest(guideline_id,version,action,lang){
 
createXHR();

xmlHttp.onreadystatechange = catchResult;

var url = "guidelineAjax.php?timeStamp="+new Date().getTime()+'&guideline_id='+guideline_id+'&version='+version+'&action='+action+'&lang='+lang;

xmlHttp.open('GET',url,true);
xmlHttp.send(null);	
 
 
 
 
 
 
}
function catchResult(){
 
if(xmlHttp.readyState == 4){
  
if(xmlHttp.status == 200){

  var table = xmlHttp.responseText;
  var targetDiv = document.querySelector('div#previousversion');
  targetDiv.innerHTML = "";
  targetDiv.insertAdjacentHTML('beforeend',table);
  initPopUpWin();


        	
  
  
  
}
 
 
 
 
 
}
}*/





/* function subitemDisplay(button){
 
console.log(button);
var subItemDiv = button.nextElementSibling;
if(subItemDiv.classList.contains("active")){
  
  button.innerHTML = "Show subitem";
  subItemDiv.classList.remove("active");
  
  
  
  
  
}else {
  
  button.innerHTML = "Hide subitem";
  
  subItemDiv.classList.add("active");
  
  
}

 
 
 
 
 
 
 
 
 
}*/

function initPopUpWin() {
    // Get the modal
    var modal = document.getElementById("myModal");
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("bg_popup_close")[0];
    // Get popup image id


    if (modal !== null) {
        modal.style.display = "block";
    }


    // When the user clicks on <span> (x), close the modal


    if (modal !== null && span !== null) {
        span.onclick = function () {
            modal.style.display = "none";
        }


        span.onkeypress = function (e) {
            var key = e.keyCode; //|| e.charCode;

            if (key == 32 || key == 13) {
                modal.style.display = "none";
            }
        }


        /*$(document).on('keydown', '#input', function(e) {
          var key = event.keyCode || event.charCode;

          if( key == 8 || key == 46 ) {
            if(window.getSelection().anchorNode.parentNode.tagName ==='SPAN'){
              window.getSelection().anchorNode.parentNode.remove();
            }
            alert("backspace detected!");
            return false;
          }
        });*/

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    }
}

$("#topic").change(function () {
    search_topic();
});

function search_topic() {
    if (location_href.match('en/')) {
        lang = 'en';
    } else if (location_href.match('tc/')) {
        lang = 'tc';
    } else if (location_href.match('sc/')) {
        lang = 'sc';
    }

    if (location_href.match('preview/')) {
        action = 'preview';
    } else {
        action = 'pub';
    }
    createXHR();
    xmlHttp.onreadystatechange = catchResult;
    var url = 'ajax.php?timeStamp=' + new Date().getTime() + '&lang=' + lang;
    var keyword = document.getElementById('keyword').value;
    var topic = document.getElementById('topic').value;

    url += '&keyword=' + keyword + '&topic_id=' + topic + '&action=' + action;
    console.log(url);
    xmlHttp.open('GET', url, true);
    xmlHttp.send(null);
}

function catchResult() {
    if (xmlHttp.readyState == 4) {
        if (xmlHttp.status == 200) {
            var table = xmlHttp.responseText;
            var targetDiv = document.getElementById('guideline-div');
            targetDiv.innerHTML = "";
            targetDiv.insertAdjacentHTML('beforeend', table);
        }
    }
}

$("#search_guideline").click(function () {
    document.getElementById('search_form').submit();
});


isSubmitted = false;

function reloadCaptcha() {
    jQuery('#siimage').prop('src', './securimage_show.php?sid=' + Math.random());
}

function isCaptchaCorrect() {
    $.post("../share/check_code.php", {
        "captcha_code": $('#captcha_code').val()
    }, function (msg) {
        if (location_href.match("en/")) {
            if (msg == "no") {
                alert('Please enter the correct verification code');
                reloadCaptcha();
            } else if (msg == "ok") {
                $('#subscribe_form')[0].submit();
            }
        } else if (location_href.match("sc/")) {
            if (msg == "no") {
                alert('请输入正确验证码');
                reloadCaptcha();
            } else if (msg == "ok") {
                $('#subscribe_form')[0].submit();
            }
        } else if (location_href.match("tc/")) {
            if (msg == "no") {
                alert('請輸入正確驗證碼');
                reloadCaptcha();
            } else if (msg == "ok") {
                $('#subscribe_form')[0].submit();
            }
        }
    });


    /*
    $.post(
        "../php/captcha/checkCaptcha.php",
        {captcha_code:$('[name=code]').val()},
        function(data, textStatus, jqXHR){
            if(data=='true'){
                $('#subscribe_form')[0].submit();
            }else{
                alert('Please enter the correct verification number');
                isSubmitted = false;
            }
        }
    );
    */
}

function checkValidate() {
    isSubmitted = true;
    var isSubmitted = validate();
    if (isSubmitted) {
        isCaptchaCorrect();
    } else {
        isSubmitted = false;
    }
    return false;
}

function emailIsValid(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}

function validate() {

    var valid = false;

    var email = $('#email').val().trim();
    if (location_href.match("en/")) {
        if (email == "") {
            alert("Please enter email address");
            return false;
        } else if (!emailIsValid(email)) {
            alert("Please enter the correct email address");
            return false;
        }

        //topics 
        if (!$("input[name='topics[]']:checked").length > 0) {
            alert("Please check the box above to proceed with your subscription");
            return false;
        }

        if ($('#captcha_code').val() == "") {
            alert("Please enter verification code");
            return false;
        }
    } else if (location_href.match("sc/")) {
        if (email == "") {
            alert("请输入电邮地址");
            return false;
        } else if (!emailIsValid(email)) {
            alert("请输入正确电邮地址");
            return false;
        }

        if (!$("input[name='topics[]']:checked").length > 0) {

            alert("请点选以上方格以继续进行订阅");
            return false;
        }

        if ($('#captcha_code').val() == "") {
            alert("请输入验证码");
            return false;
        }
    } else if (location_href.match("tc/")) {
        if (email == "") {
            alert("請輸入電郵地址");
            return false;
        } else if (!emailIsValid(email)) {
            alert("請輸入正確電郵地址");
            return false;
        }

        if (!$("input[name='topics[]']:checked").length > 0) {
            alert("請點選以上方格以繼續進行訂閱");
            return false;
        }

        if ($('#captcha_code').val() == "") {
            alert("請輸入驗證碼");
            return false;
        }

    }
    return true;
}
$(function () {

    $('[name="topics[]"]').click(function () {
        $('#topicsAll').prop('checked', false);
        $('#deselect').prop('checked', false);
    });

});

function deselectAll() {

    $('[name="topics[]"]').each(function () {
        $(this).prop('checked', false);
    });
    $('#topicsAll').prop('checked', false);
}

function selectAll(x) {
    $('[name="' + x + '[]"]').each(function () {
        if ($('[name="' + x + 'All"]').prop('checked')) {
            $(this).prop('checked', true);
        } else {
            var select = $(this);
            if (select.attr('id') != x + '0') {
                $(this).prop('checked', false);
            } else {
                $(this).prop('checked', false);
            }
        }
    });
}

function subscribe() {
    $('#topicsAll').click(function () {
        selectAll('topics');
    });

    const form = document.querySelector(".campaign_form");
    form.addEventListener("submit", event => {
        if (!checkValidate()) {
            event.preventDefault();
        }
        // do whatever you want instead of submitting
    });

     $(".captcha_play_button").click(function () {
        event.preventDefault();
    }); 

    $(".refresh").click(function () {
        blur();
    });

    $(".refresh_button").click(function () {
        if (typeof window.captcha_image_audioObj !== 'undefined')
            captcha_image_audioObj.refresh();
        document.getElementById('captcha_image').src = '/admin/preview/1/share/securimage/securimage_show.php?' + Math.random(); 
        this.blur();
        event.preventDefault();
    });
}

