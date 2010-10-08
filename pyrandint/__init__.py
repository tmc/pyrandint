import json
import urllib

def get_randint():
    return int(json.loads(urllib.urlopen('http://randint.com/api/').read())['rand']['int'])
