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
import kartina_api

addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')
addon_version = addon.getAddonInfo('version')
addon_path = xbmc.translatePath(addon.getAddonInfo('path')).decode('utf-8')
language = addon.getLocalizedString

global windowstack
windowstack = []

global ids
ids = []


# Function to show error message
def error(window=None, message=None):
    if not message:
        message = language(30102)
    dialog = xbmcgui.Dialog()
    dialog.ok(language(30100), message)
    if window:
        window.close()


# Function for log in KARTINA.TV or show error
def log_in():
    data = kartina_api.login()
    if data['result'] == 'ok':
        return True
    else:
        error(None, data['message'])
        return False
