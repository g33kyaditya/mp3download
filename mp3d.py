#!/usr/bin/python
import urllib2
import sys
import re
import subprocess

song_name = []
for st in sys.argv:
    song_name.append(st)

song_name = song_name[1:]
query = '+'.join(song_name)
search_query = 'https://www.youtube.com/results?search_query=' + query

response = urllib2.urlopen(search_query)
html = response.read()

locator = re.search('href="\/watch\?v=.{11}"', html)
locator = locator.group()
last_url = locator[6:-1]

video_url = 'https://www.youtube.com' + last_url

subprocess.call(['youtube-dl', '--extract-audio', '--audio-format', 'mp3',
                 '--output', '%(title)s.%(ext)s', video_url])

