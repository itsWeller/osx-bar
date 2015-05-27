#! /usr/bin/python
from mpd import MPDClient
from time import strftime
import os

title_bar = [' ' for _ in xrange(197)] # Magical number for Geektool window length

left    = []
center  = []
right   = []

def build_segment(segment, data):
    segment.extend(data)

def build_bar(left=left, center=center, right=right, title_bar=title_bar):
    mid_points = (len(title_bar)/2-len(center)/2, len(title_bar)/2+len(center)/2)

    title_bar[:len(left)] = left
    title_bar[mid_points[0]:mid_points[1]] = center
    title_bar[len(title_bar) - len(right):] = right

# Music Info
client = MPDClient()
client.connect("localhost",6600)
song_info = client.currentsong()

# Time
now = str(strftime("%I:%M"))

# Default Hostname (Yes I know I should get it programatically, but, lazy.
hostname = " chris@air.local"

# Battery left
battery = os.popen("pmset -g batt | grep -o '[0-9]*%'").read().strip()

build_segment(left, " chris@air.local")
build_segment(center, song_info['artist']+' // '+song_info['title'])
build_segment(right, battery + " | " + now + " ")

build_bar()

print ''.join(title_bar)
