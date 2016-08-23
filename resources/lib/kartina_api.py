#!/usr/bin/python
# -*- coding: utf-8 -*-
#############################################################################
#
#
#
#
#
#############################################################################

import xbmc, xbmcgui, xbmcaddon, xbmcvfs
import os
import platform
import requests
import simplejson
import base64

try:
    import requests.packages.urllib3 as urllib3

    urllib3.disable_warnings()
except ImportError as e:
    pass

addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')
addon_version = addon.getAddonInfo('version')
addon_path = xbmc.translatePath(addon.getAddonInfo('path')).decode('utf-8')
language = addon.getLocalizedString
cookie_path = os.path.join(addon_path, 'resources', 'cookie')
platform_version = xbmc.getInfoLabel('System.BuildVersion').split(" ")[0]
if int(platform_version.split(".")[0]) >= 14:
    name = 'Kodi'
else:
    name = 'XBMC'
try:
    UA = '%s/%s-%s' % (name, platform_version, platform.platform(aliased=0, terse=0)[:40])
except:
    data = os.uname()
    UA = '%s/%s-%s-%s-%s' % (name, platform_version, data[0], data[2], data[-1])
    UA = UA[:50]

API_URL = 'https://iptv.kartina.tv/api/json'


# Function to login in KARTINA TV
def login():
    usr = addon.getSetting('username')
    pwd = addon.getSetting('password')
    if usr.isdigit() and pwd.isdigit():
        data = GET('login?login=%s&pass=%s' % (usr, pwd))
        if 'ok' in data.keys():
            if not 'error' in data['ok'].keys():
                sid = data['ok']['sid']
                sid_name = data['ok']['sid_name']
                xbmc.log("%s\n%s" % (sid, sid_name))
                return {'result': 'error', 'message': 'Something went wrong with cookie!'}
            else:
                return {'result': 'error', 'message': data['ok']['error']['message']}
        else:
            return {'result': 'error', 'message': data['error']}
    else:
        return {'result': 'error', 'message': language(30101)}


# Function to GET data from API page
def GET(url, old_url=None, postparams=None):
    target = "%s/%s" % (API_URL, url)
    xbmc.log('[%s]: Target - %s' % (addon_name, target))

    if os.path.exists(cookie_path):
        f = open(cookie_path)
        cookie = simplejson.loads(base64.b64decode(f.read()))
    else:
        cookie = None

    if cookie and not old_url:
        request = requests.get(target, cookies=cookie, headers={'User-Agent': UA}, timeout=7)
        xbmc.log('[%s]: request - %s' % (addon_name, request))
        answer = request.text
        xbmc.log('[%s]: http - %s' % (addon_name, answer.encode('utf-8')))
    else:
        if not url.startswith('login?login='):
            usr = addon.getSetting('username')
            pwd = addon.getSetting('password')
            GET('login?login=%s&pass=%s' % (usr, pwd), old_url=url)
        else:
            session = requests.session()
            request = session.get(target, headers={'User-Agent': UA}, timeout=7)
            answer = request.text
            xbmc.log('[%s]: answer - %s' % (addon_name, answer))
            # if answer.startswith('{"result":"ok"'):
            #     cookies = requests.utils.dict_from_cookiejar(session.cookies)
            #     # xbmc.log('[%s]: NEW COOKIE - %s' % (addon_name, cookies))
            #     a.cookie_to_db(base64.b64encode(str(cookies).replace("'", '"')))
            #     if old_url:
            #         # xbmc.log('[%s]: GET elif usr and pwd, old_url - %s' % (addon_name, old_url))
            #         GET(old_url)
            #     else:
            #         # xbmc.log('[%s]: return GET elif usr and pwd, http - %s' % (addon_name, http.encode('utf-8')))
            #         return http.encode('utf-8')
            # else:
            #     return None

    try:
        answer = simplejson.loads(answer.encode('utf-8'))
    except Exception as e:
        xbmc.log('[%s] Error converting JSON to array!\n%s' % (addon_name, e))
        return {'error': 'Error converting JSON to array!'}

    xbmc.log('[%s]: JSON Answer - %s' % (addon_name, answer))

    return {'ok': answer}
