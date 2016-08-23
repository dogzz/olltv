#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################
#
#
#
#
#
##########################################################################

import xbmcaddon, xbmc, xbmcgui, xbmcplugin
import os
import sys

addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')
addon_version = addon.getAddonInfo('version')
addon_path = xbmc.translatePath(addon.getAddonInfo('path')).decode('utf-8')
cookie_path = os.path.join(addon_path, 'resources', 'cookie')
language = addon.getLocalizedString

sys.path.append(os.path.join(addon_path, 'resources', 'lib'))
from utils import error, log_in

xbmc.log('[%s]: Start plugin! Version: %s' % (addon_name, addon_version))
# ##################################	  Start Splash	    ####################################### #
splash = xbmcgui.WindowXML('splash.xml', addon_path)
splash.show()

# ##################################	    First run		####################################### #
if addon.getSetting('firstrun') == '0' or addon.getSetting('firstrun') == '':
    addon.openSettings()
    addon.setSetting(id='firstrun', value='1')

# ##################################	 Remove cookies		####################################### #
if os.path.exists(cookie_path):
    os.remove(cookie_path)

if addon.getSetting('username').isdigit() and addon.getSetting('password').isdigit():
    # ##################################	   Home screen		####################################### #
    if log_in():
        import Background

        back = Background.Background('background.xml', addon_path, win=splash)
        back.doModal()
        del back
        splash.close()
    else:
        error(splash)
else:
    error(splash, language(30101))

# ##################################       Close addon      ####################################### #
del splash
xbmc.log('[%s]: Close plugin. Version: %s' % (addon_name, addon_version))
