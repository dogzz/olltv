# coding: utf-8

import ast
import re
import sys
import xml.etree.ElementTree as et
from collections import namedtuple

from bs4 import BeautifulSoup
from simpleplugin import Plugin
import xbmc
import webclient

SITE = 'http://oll.tv'

# Extensions for supported media files
MEDIA_EXTENSIONS = 'avi|mkv|ts|m2ts|mp4|m4v|flv|vob|mpg|mpeg|mov|wmv|mp3|aac|ogg|wav|dts|ac3|flac|m4a|wma'
VIDEO_DETAILS = {
    'year': ur'(?:[Гг]од|[Рр]ік).*?: *?(\d{4})',
    'genre': ur'[Жж]анр.*?:(.*)',
    'director': ur'[Рр]ежисс?[её]р.*?:(.*)',
    'plot': ur'(?:Описание|О фильме|Сюжет|О чем|О сериале).*?:\n?(.*)',
    'cast': ur'(?:[ВвУу] ролях|[Аа]кт[ео]р[ыи]).*?:(.*)',
    'rating': ur'IMD[Bb].*?: *?(\d\.\d)',
}

MediaCategory = namedtuple('MediaCategory', ['name', 'path', 'items'])
TvChannelPack = namedtuple('TvChannelPack', ['path', 'name', 'items'])
MediaList = namedtuple('MediaList', ['media', 'prev_page', 'next_page', 'original_id'])
MediaItem = namedtuple('MediaItem', ['title', 'thumb', 'path'])
ChannelItem = namedtuple('ChannelItem', ['title', 'thumb', 'path', 'referer', 'media_path'])
MediaDetails = namedtuple('MediaDetails', ['title', 'thumb', 'files', 'mp4', 'info'])
MediaFile = namedtuple('MediaFile', ['filename', 'path', 'mirrors'])
ExUaPage = namedtuple('ExUaPage', ['type', 'content'])

plugin = Plugin()
poster_quality = '400' if plugin.hq_posters else '200'


def get_categories(path):
    """
    Get video categories
    """
    pass


def get_channel_packs(path):
    return parse_channel_packs(webclient.load_page(SITE + path, post_data=None, headers=webclient.HEADERS_SUBS))


def get_channel_list(path, page=0, items=25):
    """
    Get the list of media articles
    """
    url = SITE + path
    web_page = webclient.load_page(url, post_data=None, headers=webclient.HEADERS_CHANNELS)
    return _parse_channel_items(web_page, url)


def get_channel_strem(path, referer):
    url = SITE + path
    headers = webclient.HEADERS_CHANNELS.copy()
    headers['Referer'] = referer
    web_page = webclient.load_page(url, post_data=None, headers=headers)
    stream_url = _get_stream_url(web_page, url)
    return stream_url


def get_media_list(path, page=0, items=25):
    """
    Get the list of media articles
    """
    pass


def detect_page_type(path):
    """
    Detect the type of an ex.ua page
    """
    pass


# ===============

def parse_channel_packs(web_page):
    """
    Parse media categories list
    """
    # parse = re.findall('<b>(.*?)</b></a><p><a href=\'(.*?)\' class=info>(.*?)</a>', web_page)
    parse = re.findall('class=.b-purchase.*?<a href=[\'"](.*?)[\'"].*?<span>(.*?)</span>.*?subscr-yet-active[\'"]>(.*?)</span>', web_page, re.DOTALL)
    # soup = BeautifulSoup(web_page, 'html5lib')
    # media_tags = soup.find_all('tr', class_='b-purchase')
    listing = []
    for item in parse:
        listing.append(TvChannelPack(item[0], item[1], item[2]))
    plugin.log('Channels: {0}'.format(str(listing)))
    return listing


def _parse_channel_items(web_page, url):
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
                listing.append(ChannelItem(title, thumb, link_tag['href'], url, ""))
        except TypeError:
            pass
    return listing


def _get_stream_url(web_page, referer):
    parse = re.search('videoUrl:[\'"](.*?)[\'"]', web_page, re.DOTALL)
    stream_url = ""
    if parse is not None:
        url = parse.group(1)
        plugin.log("Get Stream Url: {0}".format(url))
        if url:
            headers = webclient.HEADERS_CHANNELS.copy()
            headers['Referer'] = referer
            web_page = webclient.load_page(url, post_data=None, headers=headers)
            parse = re.search('[\'"]url[\'"]:[\'"](.*?m3.*?)[\'"]', web_page, re.DOTALL)
            if parse is not None:
                stream_url = parse.group(1).replace('\/', '/') + '?key='
                plugin.log("Get Stream Url: {0}".format(stream_url))
    return stream_url


class VideoPlayer(xbmc.Player):
    def __init__(self, *args, **kwargs):
        xbmc.Player.__init__(self)
        self.size = None
        self.counter = 0
        self.stopped = False
        self.popstack = kwargs.get("popstack", True)

    def onPlayBackEnded(self):
        if self.size:
            self.counter += 1
            if self.counter <= self.size:
                self.stopped = False
                xbmc.sleep(1500)
                if not self.isPlaying():
                    self.stopped = True
            else:
                self.stopped = True
        else:
            self.stopped = True

    def onPlayBackStopped(self):
        self.stopped = True

    def onPlayBackStarted(self):
        self.stopped = False

    def play_item(self, stream_url, listitem, subtitle=None, popstack=True):
        if subtitle:
            try:
                listitem.setSubtitles([subtitle])
            except Exception as e:
                xbmc.log('[%s]: NOT KODI. SUBTITLE EXCEPTION: %s' % ('Oll.tv', e))
            xbmc.log('SUBTITILE - %s' % subtitle)
        xbmc.executebuiltin("Dialog.Close(all, true)")
        self.play(stream_url, listitem)

    def play_playlist(self, playlist, size, popstack=True):
        self.size = size
        xbmc.executebuiltin("Dialog.Close(all, true)")
        self.play(playlist)

    def WaitForVideoEnd(self):
        while not self.stopped:
            xbmc.sleep(200)
        self.stopped = False

