import argparse
import os
import markdown

def change_ext(file, ext='.html'):
  # pre is the part of file name before extension and oldext is current extension
  pre, oldext = os.path.splitext(file)
  return pre + ext

def converter(file):
  #print("Is file:" + file)
  with open(file, 'r') as f:
    mdfile = f.read()
  
  htmlfile = markdown.markdown(mdfile)
  with open(change_ext(file), 'w') as f:
    f.write(htmlfile)

def converterdir(dir):
  for file in os.listdir(dir):
    if file.endswith(".md"):
      converter(file)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("file")
  args = parser.parse_args()

  if os.path.isfile(args.file):
    converter(args.file)
  elif os.path.isdir(args.file):
    converterdir(args.file)
  else:
    raise FileNotFoundError("There is no such file or directory.")