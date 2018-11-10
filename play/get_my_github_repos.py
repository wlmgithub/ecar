import sys
import json
import pprint

import requests

BASE_URL = 'https://api.github.com/users/wlmgithub/repos?per_page=100'


def main():
  for n in range(1, 3):
    r = requests.get('{}&page={}'.format(BASE_URL, n))
    if r.status_code == 200:
      ret = r.json()
      for o in ret:
        print(o['name'])

def main0():
  with open(XXX) as fh:
    js = json.load(fh)
    for i in js:
      print(i['name'])

if __name__ == '__main__':
#  XXX = sys.argv[1]
  main()
