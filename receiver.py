import os
message = ""
ready = False

while True:
  while os.path.exists("/tmp/DRD"):
    pass
  if os.path.exists("/tmp/DSR"):
    if os.path.exists("/tmp/data"):
      message = message + "1"
    else:
      message = message + "0"
    ready = open("/tmp/DRD", 'w')
  if message != "":
    print(message)
    
