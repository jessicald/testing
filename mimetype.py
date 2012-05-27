#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from urlparse import urlparse
import urllib
import BeautifulSoup
import httplib
from random import choice

TestURLs = [
        'https://en.wikipedia.org/wiki/Vim_%28text_editor%29',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/World_map_pol_2005_v02.svg/800px-World_map_pol_2005_v02.svg.png',
        'http://shutupslaves.com:80/',
        'https://ko.wikipedia.org/wiki/?',
        'http://d.bldm.us/gallery/photos/a3300/Ｗｏｎ’ｔ　ｙｏｕ　ｂｅｃｏｍｅ　ａ　ｍａｇｉｃａｌ　ｄｏｇ？.jpg'
        'https://ko.wikipedia.org/wiki/&',
        'http://tinyurl.com/161',
        'http://i.imgur.com/R6D5v.gif',
        'https://twitter.com/#!/SteamGamers/status/185648047324282880'
        'https://twitter.com/?query=true&false=true#!/SteamGamers/status/185648047324282880?query=false'
]
HTMLTypes = ['text/html','application/xhtml+xml' ]
RedirectCodes = [ 301, 302, 303 ]
UserAgents = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]
UserAgent = choice(UserAgents)
MaxRedirects = 10

def ConstructTitle(Title, HostnameOrig, HostnameFinal=''):
    if HostnameFinal == '':
        summary = 'Title: %s | %s' % (HostnameOrig, Title)
    else:
        summary = 'Title: %s | %s | %s' % (HostnameOrig, Title, HostnameFinal)
    #summary = '\x02%s \x034 |\x03\x02 %s\x02\x034 |\x03\x02 %s\x02' % (HostnameOrig, Title, HostnameFinal)
    #self.irc.send(message.source, summary)
    print summary.encode('utf-8')

def PrepareURLContent(ParsedURL):
    url_content = '/'
    if ParsedURL.path != '':
        url_content = urllib.quote(ParsedURL.path, '/%')
    if ParsedURL.query != '':
        url_content = url_content + '?' + ParsedURL.query
    if ParsedURL.fragment != '':
        url_content = url_content + '#' + ParsedURL.fragment
    return url_content

for URL in TestURLs:
    print 'Test URL is: ' + URL
    """ AJAX HTML Snapshot URL parsing"""
    hashbang_index = URL.find('#!')
    if hashbang_index != -1:
        URL_base = URL[:hashbang_index]
        URL_fragment = urllib.quote(URL[hashbang_index+2:], '')
        URL = URL_base + '?_escaped_fragment_=' + URL_fragment


    parsed_url = parsed_url_orig = urlparse(URL)
    #Hostname = HostnameOrig = parsed_url.hostname
    URLContent = PrepareURLContent(parsed_url)

    print 'Path and Query to send: ' + URLContent

    """TODO: breadcrumb trail for loop detection"""
    for Try in xrange(0,MaxRedirects):
        Opener = httplib.HTTPConnection(parsed_url.hostname, parsed_url.port)
        Opener.request('HEAD', URLContent, '', {'User-Agent': UserAgent})
        Headers = Opener.getresponse()
        Opener.close()
        print 'Try ' + str(Try+1) + ', code ' + str(Headers.status)
        if Headers.status == 200:
            break
        elif Headers.status in RedirectCodes:
            parsed_url = urlparse(Headers.getheader('Location'))
            URLContent = PrepareURLContent(parsed_url)
    else:
        ConstructTitle('Max redirects reached, cannot retrive title.', parsed_url.hostname)
        continue

    ContentType = Headers.getheader('Content-Type').split(';')[0]
    print 'MIME Content-Type is: ' + ContentType
    if ContentType in HTMLTypes:
        Opener.request('GET', URLContent, '', {'User-Agent': UserAgent})
        Title = BeautifulSoup.BeautifulStoneSoup((BeautifulSoup.BeautifulSoup(Opener.getresponse()).title.string).replace('\n', '').strip(), convertEntities="html").contents[0]
        Opener.close()
        if parsed_url_orig.hostname != parsed_url.hostname:
            ConstructTitle(Title, parsed_url_orig.hostname, parsed_url.hostname)
        else:
            ConstructTitle(Title, parsed_url.hostname)
    else:
        Title = 'Type: ' + ContentType + ', Size: ' + Headers.getheader('Content-Length') + ' bytes'
        ConstructTitle(Title, parsed_url.hostname)

    print

