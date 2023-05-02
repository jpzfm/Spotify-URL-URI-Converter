import re
import os

inp = "{query}"

#  URLs to URIs
#  Converts track URL to URI.
if re.search("/track/", inp):
    processed = inp.split('track/')
    uri = "spotify:track:" + processed[-1][0:22]
    cmd = 'echo %s | tr -d "\n" | pbcopy' % uri
    os.system(cmd)

#  Converts artist URL to URI.
elif re.search("/artist/", inp):
    processed = inp.split('artist/')
    uri = "spotify:artist:"+processed[-1][0:22]
    cmd = 'echo %s | tr -d "\n" | pbcopy' % uri
    os.system(cmd)

#  Converts album URL to URI.
elif re.search("/album/", inp):
    processed = inp.split('album')
    uri = "spotify:album:"+processed[-1][0:22]
    cmd = 'echo %s | tr -d "\n" | pbcopy' % uri
    os.system(cmd)

#  Converts playlist URL to URI
elif re.search("/playlist/", inp):
    user = re.search('/user/(.*)/playlist/', inp).group(1)
    playlist = inp.split('playlist/')
    uri = "spotify:user:" + user + ":playlist:" + playlist[-1][0:22]
    cmd = 'echo %s | tr -d "\n" | pbcopy' % uri
    os.system(cmd)

#  URIs to URLs
#  Converts track URI to URL.
elif re.search(":track:", inp):
    processed = inp.split('track:')
    url = "https://open.spotify.com/track/" + processed[-1][0:22]
    cmd = 'echo %s | tr -d "\n" | pbcopy' % url
    os.system(cmd)

#  Converts artist URI to URL.
elif re.search(":artist:", inp):
    processed = inp.split('artist:')
    url = "https://open.spotify.com/artist/" + processed[-1][0:22]
    cmd = 'echo %s | tr -d "\n" | pbcopy' % url
    os.system(cmd)

#  Converts album URI to URL.
elif re.search(":album:", inp):
    processed = inp.split('album:')
    url = "https://open.spotify.com/album/" + processed[-1][0:22]
    cmd = 'echo %s | tr -d "\n" | pbcopy' % url
    os.system(cmd)

#  Converts playlist URI to URL.
elif re.search(":playlist:", inp):
    user = re.search(':user:(.*):playlist:', inp).group(1)
    playlist = inp.split('playlist:')
    url = "https://open.spotify.com/user/" + user + "/playlist/" + playlist[-1][0:22]
    cmd = 'echo %s | tr -d "\n" | pbcopy' % url
    os.system(cmd)

else:
    exit()
