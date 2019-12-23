import sys

def exe(filename):
  content = open(filename, 'r+').read()
  remove(content)

def remove(content):
  valib_bf = '[]+-<>,.'
  bf = ''
  for char in content:
    if char in valid_bf:
      bf += char
    else:
      continue
  print(bf)

def main():
  if len(sys.argv) >= 2:
    exe(sys.argv[1])
  else:
    print('Usage:', sys.argv[0], 'filename')
    
if __name__ == '__main__':
  main()
