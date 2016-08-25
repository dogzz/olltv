# coding: utf-8
# Author: Roman Miroshnychenko aka Roman V.M.
# E-mail: romanvm@yandex.ua
# Licence: GPL v.3: http://www.gnu.org/copyleft/gpl.html

import os
import cPickle as pickle
import hashlib
import base64
import re
from collections import namedtuple
import requests
from simpleplugin import Plugin

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'http://oll.tv/',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
    }
HEADERS_AUTH_POPUP = HEADERS.copy()
HEADERS_AUTH_POPUP['Accept'] = 'application/json, text/javascript, */*; q=0.01'
HEADERS_AUTH_POPUP['X-Requested-With'] = 'XMLHttpRequest'
HEADERS_LOGIN = HEADERS.copy()
HEADERS_LOGIN['Accept'] = '*/*'
HEADERS_LOGIN['X-Requested-With'] = 'XMLHttpRequest'
HEADERS_LOGIN.pop('Pragma')
HEADERS_HOME = HEADERS.copy()
HEADERS_HOME.pop('Pragma')
HEADERS_HOME['Cache-Control'] = 'max-age=0'
HEADERS_SUBS = HEADERS.copy()
HEADERS_SUBS.pop('Pragma')
HEADERS_SUBS.pop('Cache-Control')
HEADERS_CHANNELS = HEADERS.copy()
HEADERS_CHANNELS['Referer'] = 'http://oll.tv/account/subs'
HEADERS_CHANNELS.pop('Pragma')
HEADERS_CHANNELS.pop('Cache-Control')
LOGIN_URL = 'http://oll.tv/authAPI/login'
HOME_URL = 'http://oll.tv/'
AUTH_POPUP_URL = 'http://oll.tv/authAPI/AuthorizationPopup?backUrl=%2F&'
# CAPTCHA_URL = 'http://www.ex.ua/captcha?captcha_id={0}'

Captcha = namedtuple('Captcha', ['captcha_id', 'image'])

plugin = Plugin()
cookies_file = os.path.join(plugin.config_dir, '__cookies__.pcl')


class CookiesError(Exception):
    pass


class LoginError(Exception):
    pass


def _load_cookie_jar():
    if os.path.exists(cookies_file):
        with open(cookies_file, 'rb') as fo:
            try:
                return pickle.load(fo)
            except (pickle.PickleError, EOFError):
                pass
    raise CookiesError


def load_page(url, post_data=None, headers=HEADERS):
    """
    Load a webpage from ex.ua by given url
    """
    plugin.log('Loading page {0} with post_data {1}'.format(url, post_data))
    session = requests.Session()
    session.headers = headers.copy()
    try:
        session.cookies = _load_cookie_jar()
    except CookiesError:
        pass
    if post_data is not None:
        resp = session.post(url, data=post_data)
    else:
        resp = session.get(url)
    with open(cookies_file, 'wb') as fo:
        pickle.dump(session.cookies, fo)
    page = resp.text
    plugin.log('Page loaded:\n{0}'.format(page.encode('utf-8')))
    return page


def get_cookies():
    """
    Get cookies as dict
    """
    try:
        cookie_jar = _load_cookie_jar()
    except CookiesError:
        return {}
    else:
        return requests.utils.dict_from_cookiejar(cookie_jar)


def is_logged_in():
    """
    Check if cookies conatain a user ID
    """
    cookies = get_cookies()
    plugin.log("Is logged to Oll.tv")
    return 'sessionId' in cookies and (':' in cookies['sessionId'] or '%3A' in cookies['sessionId'])


def check_captcha():
    """
    Check if there is a captcha on a login page. Returns a namedtuple
    with 'captcha_id' and 'image' elements.
    """
    # web_page = load_page(LOGIN_URL)
    # captcha_match = re.search('<img src=\'/captcha\?captcha_id=(.+?)\'', web_page, re.UNICODE)
    # if captcha_match is not None:
    #     captcha_id = captcha_match.group(1)
    #     captcha = Captcha(captcha_id, CAPTCHA_URL.format(captcha_id))
    # else:
    #     captcha = Captcha('', '')
    # plugin.log('Captcha: {0}'.format(captcha))
    return Captcha('', '')


def login(username, password, captcha_id='', captcha_value=''):
    """
    Send loging data to ex.ua.
    Raises LoginError if login is not successful
    """
    login_data = {
        'email': username,
        'password': password,
        'remember': '0'
        }
    if captcha_id:
        login_data['captcha_id'] = captcha_id
        login_data['captcha_value'] = captcha_value
    load_page(HOME_URL)
    load_page(AUTH_POPUP_URL, post_data=None, headers=HEADERS_AUTH_POPUP)
    result_page = load_page(LOGIN_URL, login_data, HEADERS_LOGIN)
    if 'LOGIN_OK' not in result_page:
        raise LoginError
    else:
        load_page(HOME_URL, post_data=None, headers=HEADERS_HOME)



def encode(clear):
    key = hashlib.md5(str(True)).hexdigest()
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode(''.join(enc))


def decode(enc):
    key = hashlib.md5(str(True)).hexdigest()
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return ''.join(dec)
