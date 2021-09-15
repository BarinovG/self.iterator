import hashlib


def md_generator(file):
  with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
      yield hashlib.md5(line.encode())


def md5_create(file):
  generator = md_generator(file)
  for i in md_generator(file):
    print(i.digest())
