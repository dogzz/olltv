# coding: utf-8
import sys
from bs4 import BeautifulSoup
from collections import namedtuple

web_page = """HTTP/1.1 200 OK
Server: nginx
Date: Thu, 25 Aug 2016 18:23:20 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Keep-Alive: timeout=7
Vary: Accept-Encoding
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Length: 27187

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">

        <title>Пакет Кругозор</title>
    <meta name="description" content="">
    <meta name="keywords" content="">
    <meta name="mrc__share_title" content="Мир становится еще интереснее с пакетом «Кругозор»" />
<meta name="mrc__share_description" content="и телеканалами Discovery, National Geographic, Animal Planet и Nat Geo Wild и др." />
<meta property="og:title" content="Мир становится еще интереснее с пакетом «Кругозор»" />
<meta property="og:description" content="и телеканалами Discovery, National Geographic, Animal Planet и Nat Geo Wild и др." />
<meta property="og:image" content="http://s8.ollcdn.net/i/82/42/cd/8242cd_krugozor.png" />
<meta property="og:url" content="http://oll.tv/pack/3141" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="OLL.TV" />
<meta itemprop="name" content="Мир становится еще интереснее с пакетом «Кругозор»" />
<meta itemprop="description" content="и телеканалами Discovery, National Geographic, Animal Planet и Nat Geo Wild и др." />
<meta itemprop="image" content="http://s8.ollcdn.net/i/82/42/cd/8242cd_krugozor.png" />
<link rel="image_src" href="http://s8.ollcdn.net/i/82/42/cd/8242cd_krugozor.png" />
        <meta name="viewport" content="width=1024">
    <meta name='yandex-verification' content='7b740f8e1072f968' />
    <meta name="google-site-verification" content="mvtlV9395JLGNNLzuaRrYpPswARBGAD4cdA2SYIXvfc" />
    <meta name='wmail-verification' content='d672fe3beddcc9d2' />
    <meta name="apple-itunes-app" content="app-id=586319502"/>
    <!-- styles -->
    <link href="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/css/style.css" rel="stylesheet">
        <!-- fav and touch icons -->
    <link rel="shortcut icon" type="image/vnd.microsoft.icon" href="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/i/favicon/favicon.ico">
    <link rel="apple-touch-icon" href="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/i/favicon/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="72x72" href="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/i/favicon/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="114x114" href="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/i/favicon/apple-touch-icon-114x114.png">

    <!-- socials -->
    <!-- VK -->
    <meta property="vk:app_id" content="2875767"/>
    <script type="text/javascript" src="http://vk.com/js/api/share.js?9" charset="windows-1251"></script>
    <!--    <script type="text/javascript" src="http://userapi.com/js/api/openapi.js?49"></script>-->

    <!-- Odnoklasniki -->
    <link href="http://stg.odnoklassniki.ru/share/odkl_share.css" rel="stylesheet">
    <script src="http://stg.odnoklassniki.ru/share/odkl_share.js" type="text/javascript"></script>
    <!-- end socials -->

    <meta name="google-site-verification" content="lm6S4nWh9fq842Xcw58C0Jl_LiE2maH_FJBT3P-Kb8c" />
    <script>dataLayer = [{"CategoryPage":"Пакет Кругозор","Authorization":"Yes","UserType":"Old","Loyalty":"small","uid":1762519}];</script>
<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-W6QTPL"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-W6QTPL');</script>
<!-- End Google Tag Manager -->

    <script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/js/ga_social_tracking.js"></script>

        <script language="JavaScript"><!--
        var N = 3;
        var ar_bn1= Math.floor(Math.random()*N+1);
        //-->
    </script>

    <!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function (d, w, c) {
        (w[c] = w[c] || []).push(function() {
            try {
                w.yaCounter17950666 = new Ya.Metrika({id:17950666, enableAll: true, webvisor:true});
            } catch(e) { }
        });

        var n = d.getElementsByTagName("script")[0],
                s = d.createElement("script"),
                f = function () { n.parentNode.insertBefore(s, n); };
        s.type = "text/javascript";
        s.async = true;
        s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//mc.yandex.ru/metrika/watch.js";

        if (w.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", f);
        } else { f(); }
    })(document, window, "yandex_metrika_callbacks");
    </script>
            <noscript><div><img src="//mc.yandex.ru/watch/17950666" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
    <!-- /Yandex.Metrika counter -->
    <script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/js/jquery.min.js"></script>
</head>

<body class="payment-page b-payment-page orange">


<div class="cont-old-browsers b-cont-old-browsers">
    <strong>Ваш браузер устарел.</strong> Сайт будет работать неправильно.<br />  Пожалуйста, скачайте и установите один из новых бесплатных браузеров:<br />
    <a href="https://www.google.com/chrome?hl=ru">Google Chrome</a>,
    <a href="http://ru.opera.com/download/">Opera</a>,
    <a href="http://www.mozilla.org/ru/firefox/new/">Mozilla Firefox</a>,
    <a href="http://windows.microsoft.com/ru-RU/internet-explorer/downloads/ie">Internet Explorer,</a>
    <a href="http://www.apple.com/ru/safari/">Safari</a>.
    <span class="close"></span>
</div>
<header class="alt-header">
    <div class="cont-logo"><a href="/"><img src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/i/pre-logo.png" alt="Твое. Персональное. Интерактивное" /></a></div>
    <div class="cont-top-menu">
        <div class="main-head">
            <div class="head">
                                    Пакет &laquo;Кругозор&raquo;
                            </div>
        </div>

        <p class="head-discount-info">
                            При подключении <br>
                на 12 месяцев - <a href="/payment/3141#year">скидка <strong>16</strong>%</a>
                    </p>
                    <a href="/payment/3141#month" class="buy-subscribe">Купить за 29 грн/мес</a>

                    <a href="/go" class="fa-close b-fa-close"></a>

        <script type="text/javascript">
            window._olltv = window._olltv || {};
            window._olltv.user = window._olltv.user || {};
            window._olltv.user.isLogged = true;
        </script>
    </div>
</header>

<section class="cont-main">
    <div class="cont-payment">
        <section class="cont-tariff-kino">
            <h1>Телеканалы</h1>
            <ul class="tv-chan b-channels-list">
                                <li class="news">
                    <div>
                                                    <a href="/iptv/discovery"><img src="http://s3.ollcdn.net/i/93/3d/28/933d28_discovery.jpg" alt="" /></a>
                                                <div class="head">Discovery</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/animalplanet"><img src="http://s9.ollcdn.net/i/22/cc/78/22cc78_animal-planet.jpg" alt="" /></a>
                                                <div class="head">Animal Planet</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/nationalgeographic"><img src="http://s8.ollcdn.net/i/50/6c/4d/506c4d_national-geographic.jpg" alt="" /></a>
                                                <div class="head">National Geographic</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/natgeowild"><img src="http://s0.ollcdn.net/i/7c/70/00/7c7000_nat-geo.jpg" alt="" /></a>
                                                <div class="head">Nat Geo Wild</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/history"><img src="http://s0.ollcdn.net/i/89/2d/7c/892d7c_history.jpg" alt="" /></a>
                                                <div class="head">History</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/viasatexplorer"><img src="http://s4.ollcdn.net/i/34/68/33/346833_viasatexplorer.jpg" alt="" /></a>
                                                <div class="head">Viasat Explore</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/viasathistory"><img src="http://s7.ollcdn.net/i/89/f4/cc/89f4cc_viasathistory.jpg" alt="" /></a>
                                                <div class="head">Viasat History</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/viasatnature"><img src="http://s1.ollcdn.net/i/6a/8d/b1/6a8db1_viasatnature.jpg" alt="" /></a>
                                                <div class="head">Viasat Nature</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/viasathistorynaturehd"><img src="http://s6.ollcdn.net/i/11/d7/c9/11d7c9_162x89-viasat-history-nature.png" alt="" /></a>
                                                <div class="head">Viasat History/Nature HD</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/travelchannel"><img src="http://s5.ollcdn.net/i/56/55/23/565523_162x89-travel.png" alt="" /></a>
                                                <div class="head">Travel Channel</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/englishclubtv"><img src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/i/posters/englishclubtv.jpg" alt="" /></a>
                                                <div class="head">English Club TV</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/englishclubtvhd"><img src="http://s9.ollcdn.net/i/94/53/09/945309_english-club-hd.jpg" alt="" /></a>
                                                <div class="head">English Club TV HD</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/olltv_bbcearth"><img src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/i/posters/olltv_bbcearth.jpg" alt="" /></a>
                                                <div class="head">OLL.TV BBC Земля</div>
                    </div>
                </li>
                                <li class="news">
                    <div>
                                                    <a href="/iptv/olltv_harmony"><img src="http://s5.ollcdn.net/i/4c/de/3a/4cde3a_161x89-garmonia.jpg" alt="" /></a>
                                                <div class="head">OLL.TV Гармония классики</div>
                    </div>
                </li>
                                            </ul>
        </section>
                <section class="cont-tariff-kino clearfix">
            <h1>Управление телевидением</h1>
            <div class="half">
                <ul class="tv-manage">
                    <li class="pause">ТВ-пауза до 10 минут</li>
                    <li class="rec">ТВ-запись на 7 дней <i>не для всех телеканалов</i></li>
                </ul>
            </div>
            <div class="half">
                <ul class="tv-manage">
                    <li class="prog-tv">ТВ-программа</li>
                    <li class="control">Родительский контроль</li>
                </ul>
            </div>
            <div class="half">
                <ul class="tv-manage">
                    <li class="prog-theme">Телепрограммы по темам</li>
                    <li class="sound">Звуковые дорожки</li>
                </ul>
            </div>
        </section>
        <section class="cont-tariff-kino clearfix">
            <div class="half">
                <h1>Дополнительно</h1>
                <ul class="tv-addon">
                                        <li class="radio">Радио эфирное и онлайн</li>
                                    </ul>
            </div>
            <div class="half">
                <h1>Просмотр</h1>
                <div class="devices">
                    <ul class="con-list">
                        <li><a href="/pre-order"><em class="icCon-stb"></em><span>OLL.TV BOX</span></a></li>
                        <li><a href="/device/smarttv"><em class="icCon-tv"></em><span>Smart TV</span></a></li>
                        <li><a href="/device/tablet"><em class="icCon-tab"></em><span>Планшет</span></a></li>
                        <li><a href="/device/smartphone"><em class="icCon-phone"></em><span>Смартфон</span></a></li>
                        <li><em class="icCon-pc"></em><span>ПК</span></li>
                    </ul>
                </div>
                <i>Вы можете использовать одновременно до<br /> 3-х устройств без дополнительной платы.</i>
            </div>
            <div class="half">
                <h1>Подключение</h1>
                                    <a href="/payment/3141#month" class="buy-subscribe">Купить за 29 грн/мес</a>
                                <i>
                    При подключении на 3 месяца экономия 5%, на 12 месяцев - 16%.<br /><br />
                    Услуга доступна на территории Украины.<br />Цена указана с НДС.
                </i>
            </div>
                    </section>
    </div>
</section>

<div class="PopupOverlay dn"></div>
<form method="POST" action="/redirect/301?url=/" id="AuthFormInput" class="form-horizontal dn">
    <div class="popup-form-section">
        <p>Телефон или email</p>
        <input type="text" class="b-form-input b-email" placeholder="" name="AuthForm[email]" id="AuthForm_email"/>
        <em></em>
    </div>
    <div class="popup-form-section">
        <p>Пароль</p>
        <input type="password" class="b-form-input b-password b-edit-password" placeholder="Не менее 6 символов" name="AuthForm[password]" id="AuthForm_password"/>
        <em></em>
    </div>
    <div class="popup-form-section">
        <input type="submit" value="Войти" class="btn-yellow b-submit"/>
    </div>
    <div class="label-bl">
        <label class="label_check" for="sample-check">
            <input name="sample-check-1" id="sample-check" value="" type="checkbox" class="b-form-input b-remember" />
            Запомнить
        </label>
        <a href="#" class="callPopup" data-content="b-restore-password-popup" title="Забыл пароль">Забыли пароль?</a>
    </div>
</form>
<div class="Popup dn b-phone-request-popup">
    <div class="Popup-body">
        <div class="popup-error-bl dn"><span class="b-error-txt"></span></div>
        <a class="closePopup ic_close b-close-popup" href="#"></a>
        <h1>Ввод мобильного телефона</h1>
        <p>Для безопасной оплаты необходимо ввести номер мобильного телефона</p>
        <div class="clearfix height20"></div>
        <form method="post" class="b-popup-widget-form">
            <div class="input-txt">
                <input type="text" class="b-input-phone" placeholder="Телефон"/>
            </div>
            <div class="clearfix height20"></div>
            <input value="Продолжить" class="btn-blue b-phone-request-submit" type="button"/>
            <div class="clearfix height10"></div>
        </form>
    </div>
</div>

<!-- -->
<div class="Popup dn b-phone-request-confirm-popup">
    <div class="Popup-body">
        <div class="popup-error-bl dn"><span class="b-error-txt"></span></div>
        <a class="closePopup ic_close b-close-popup" href="#"></a>
        <h1>Ввод мобильного телефона</h1>
        <div class="clearfix"></div>
        <form class="b-popup-widget-form">
            <div class="input-txt">
                <input type="text" class="b-show-phone" placeholder="" disabled/>
                <em></em>
                <a href="#" class="b-change-phone">Указать другой номер телефона</a>
            </div>
            <div class="clearfix height15"></div>
            <div class="input-txt">
                <input type="password" class="b-input-code" placeholder="Введите пароль из SMS"/>
                <em></em>
                <a href="#" class="b-resend-sms">Отправить SMS повторно</a>
                <span class="txt-bot b-resend-sms-success-text" style="display: none">SMS отправлена</span>
            </div>
            <div class="clearfix height15"></div>

            <input value="Продолжить" class="btn-blue b-phone-request-confirm-popup" type="button"/>
        </form>
    </div>
</div>
<!-- -->
<div class="Popup dn b-email-request-popup">
    <div class="Popup-body">
        <div class="popup-error-bl dn"><span class="b-error-txt"></span></div>
        <a class="closePopup ic_close b-close-popup" href="#"></a>
        <h1>Квитанция об оплате</h1>
        <p>Для получения квитанции об оплате введите, пожалуйста, ваш email</p>
        <div class="clearfix height20"></div>
        <form method="post">
            <div class="input-txt">
                <input type="text" class="b-input-email" placeholder="Email"/>
            </div>
            <div class="clearfix height20"></div>
            <input value="Продолжить" class="btn-blue b-email-request-submit" type="button"/>
            <div class="clearfix height10"></div>
        </form>
    </div>
</div>
<!-- -->
<div class="Popup dn b-registration-popup">
    <div class="Popup-body">
        <div class="popup-error-bl dn"><span class="b-error-txt"></span></div>


        <!--     скрывать в попапе 2 шага       -->
        <a class="closePopup ic_close b-close-popup" href="#"></a>
                    <h1>Регистрация<a href="#" class="callPopup" data-content="b-new-auth-form">Войти</a></h1>
            <div class="clearfix"></div>

        <form class="b-popup-widget-form">
            <div class="popup-form-section">
                <p>Ваш мобильный телефон <span class="form-required-star">*</span></p>

                <p><input type="text" class="b-input-phone" placeholder="" value="+380"/></p>
            </div>
            <div class="popup-form-section">
                <p>Ваш e-mail</p>

                <p><input type="text" class="b-input-email" placeholder=""
                          value=""/></p>
            </div>
            <div class="popup-form-section label-bl ">
                <label class="label_check r_on" for="receive_news">
                    <input name="receive_news" id="receive_news" value="" checked="true" type="checkbox" class="b-send-news">
                    Получать новости и предложения
                </label>
            </div>


            <div class="popup-form-section">
                <p><input value="Продолжить" class="btn-yellow b-registration-submit" type="submit"/></p>
            </div>
            <article>Нажимая кнопку «Продолжить» вы принимаете <br/><a href="/terms" target="_blank">условия
                    соглашения</a></article>
        </form>
    </div>
            <div class="Popup-footer">
            <h3>Зарегистрироваться через</h3>

            <div class="icSocRound-bl">
                <a href="/auth/vkontakte" title="" class="icVkRound"></a>
                <a href="/auth/facebook" title="" class="icFbRound"></a>
                <a href="/auth/twitter" title="" class="icTwRound"></a>
                <a href="/auth/odnoklassniki" title=""
                   class="icOkRound"></a>
                <a href="/auth/google" title="" class="icGoRound"></a>
            </div>
        </div>
        <!--     /скрывать в попапе 2 шага       -->


</div>
<!-- -->

<!-- -->
<div class="Popup dn b-registration-confirm">
    <div class="Popup-body">
        <div class="popup-error-bl dn"><span class="b-error-txt"></span></div>
        <a class="closePopup ic_close b-close-popup" href="#"></a>

        <h1>Регистрация</h1>

        <div class="clearfix"></div>
        <form class="b-popup-widget-form">
            <div class="popup-form-section">
                <input type="text" class="b-show-phone" placeholder="" disabled/>
                <em></em>
                <a href="#" class="b-change-phone">Указать другой номер телефона</a>
            </div>
            <div class="popup-form-section">
                <input type="text" class="b-input-code" placeholder="Введите пароль из SMS"/>
                <em></em>
                <a href="#" class="b-resend-sms">Отправить SMS повторно</a>
                <span class="txt-bot b-resend-sms-success-text" style="display: none">SMS отправлена</span>
            </div>
            <div class="popup-form-section">
                <input value="Продолжить" class="btn-yellow b-registration-confirm-submit" type="submit"/>
            </div>
        </form>
    </div>
</div>
<!-- -->

<!-- -->
<div class="Popup dn b-registration-success">
    <div class="Popup-body">
        <div class="popup-error-bl dn"><span class="b-error-txt"></span></div>
        <a class="closePopup ic_close b-close-popup" href="#"></a>

        <h1 style="font-size: 31px;">Спасибо за регистрацию!</h1>

        <div class="clearfix"></div>
        <div class="popup-form-section">
            <p style="font-size: 15px;">Пароль из SMS - ваш пароль для входа на сайт.<br/>Для изменения пароля войдите
                <a href="/account">в Личный кабинет</a></p>
        </div>

        <div class="popup-form-section">
            <input value="Продолжить" class="btn-yellow b-close-popup" type="submit">
        </div>
    </div>
</div>
<!-- -->
<!-- script -->
<script type="text/javascript" src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/js/jquery.min.js"></script>
<script type="text/javascript" src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/js/crypto.js"></script>
<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/js/jquery-ui.min.js"></script>
<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/js/sly.js"></script>
<script type="text/javascript" src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/js/jquery.bxslider.js"></script>
<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/js/jq.placeholder.min.js"></script>
<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/js/jq.validate.1-9-0.min.js"></script>
<script type="text/javascript" src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/js/main.js"></script>

<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/promo-olltv/js/jquery.cookie.js"></script>
<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/js/jq.jscrollpane.min.js"></script>
<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/js/chek-radio.js"></script>
<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/js/bootstrap.min.2012-09-27.js"></script>

<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/js/app.min.js"></script>

<script src="http://i.ollcdn.net/628a53838ae96ec44f35736fb84e3d0481acb2b8/app/index.min.js"></script>

<script src="http://vkontakte.ru/js/api/openapi.js" type="text/javascript"></script>

<script type="text/javascript">
    window._olltv = window._olltv || {};
    _olltv.isPromo = true;
</script>

<script type="text/javascript" src="http://w.sharethis.com/button/buttons.js"></script>
<script type="text/javascript">stLight.options({publisher: "c170cc04-7830-4dd2-bf0e-535b87ce782a", doNotHash: true, doNotCopy: false, hashAddressBar: false});</script>
<script>
    window.senderCallback = function() {
        SenderWidget.init({
            companyId: "i69139852202"
        });
    }
</script>
<script>
    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        js = d.createElement(s);
        js.id = id;
        js.src = "https://widget.sender.mobi/build/init.js";
        fjs.parentNode.insertBefore(js, fjs, 'sender-widget');
    })(document, 'script');
</script>
</body>
</html>


"""
ChannelItem = namedtuple('ChannelItem', ['title', 'thumb', 'path', 'media_path'])
def _parse_channel_items(web_page):
    """
    Parse the list of media
    """
    # html.parser is faster but does not work properly on Python < 2.7.3
    if sys.version_info[1] >= 7 and sys.version_info[2] >= 3:
        soup = BeautifulSoup(web_page, 'html.parser')
    else:
        soup = BeautifulSoup(web_page, 'html5lib')
    content_table = soup.find('ul', class_='tv-chan b-channels-list')
    content_cells = content_table.find_all('li', class_='news')
    listing = []
    for content_cell in content_cells:
        try:
            link_tag = content_cell.find('a')
            if link_tag is not None:
                title = content_cell.find('div', class_='head').text
                image_tag = content_cell.find('img')
                if image_tag is not None:
                    thumb = image_tag['src']
                else:
                    thumb = ''
                listing.append(ChannelItem(title, thumb, link_tag['href'], ""))
        except TypeError:
            pass
    return listing
_parse_channel_items(web_page)