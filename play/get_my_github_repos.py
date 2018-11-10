import sys
import json
import pprint

import requests

import click

BASE_URL = 'https://api.github.com/users/wlmgithub/repos?per_page=100'

@click.command()
@click.option('--mine/--no-mine', default=True)
def main(mine):
  for n in range(1, 3):
    r = requests.get('{}&page={}'.format(BASE_URL, n))
    if r.status_code == 200:
      ret = r.json()
      for o in ret:
        if not mine:
          if o['fork']:
            print(o['name'])
        else:
          if not o['fork']:
            print(o['name'])

def main0():
  with open(XXX) as fh:
    js = json.load(fh)
    for i in js:
      print(i['name'])

if __name__ == '__main__':
#  XXX = sys.argv[1]
  main()
