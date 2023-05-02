import re
import os

inp = "{query}"

def convert_url_to_uri(inp, key):
    processed = inp.split(f'/{key}/')
    return f"spotify:{key}:" + processed[-1].split('?')[0]

def convert_uri_to_url(inp, key):
    processed = inp.split(key)
    return f"https://open.spotify.com/{key}/" + processed[-1]

patterns = {
    'track': (re.compile("/track/"), re.compile(":track:")),
    'artist': (re.compile("/artist/"), re.compile(":artist:")),
    'album': (re.compile("/album/"), re.compile(":album:")),
    'playlist': (re.compile("/playlist/"), re.compile(":playlist:"))
}

for key, (url_pattern, uri_pattern) in patterns.items():

    if url_pattern.search(inp):
        if key == "playlist":
            user_match = re.search('/user/(.*)/playlist/', inp)
            user = user_match.group(1) if user_match else None
            uri = "spotify:user:" + user + ":playlist:" + inp.split(f'/playlist/')[-1].split('?')[0] if user else "spotify:playlist:" + inp.split(f'/playlist/')[-1].split('?')[0]
        else:
            uri = convert_url_to_uri(inp, key)
        cmd = f'echo {uri} | tr -d "\n" | pbcopy'
        os.system(cmd)
        break
        
    elif uri_pattern.search(inp):
        if key == "playlist":
            user_match = re.search(':user:(.*):playlist:', inp)
            user = user_match.group(1) if user_match else None
            url = "https://open.spotify.com/user/" + user + "/playlist/" + inp.split('playlist:')[-1] if user else "https://open.spotify.com/playlist/" + inp.split('playlist:')[-1]
        else:
            url = convert_uri_to_url(inp, key)
        cmd = f'echo {url} | tr -d "\n" | pbcopy'
        os.system(cmd)
        break
        
else:
    exit()
