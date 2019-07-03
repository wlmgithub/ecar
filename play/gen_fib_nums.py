import sys
import click

NUM = 10

def gen_fib():
  a, b = 1, 1
  while True:
    yield a
    a, b = b, a+b

@click.command()
@click.option('--num', default=NUM, help='Given number')
def main(num):
  i = 1
  for n in gen_fib():
    print(i, n)
    i += 1
    if i > int(num):
      break

if __name__ == '__main__':
  sys.exit(main())
