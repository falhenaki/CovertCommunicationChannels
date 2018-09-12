import os

bits = input("Enter the bits to be sent: ")

bits = list(bits)

read = True
for x in bits:
  try:
    os.remove("/tmp/DSR")
  except:
    pass
  try:
    os.remove("/tmp/DRD")
  except:
    pass
  if x == "0":
    try:
      os.remove("/tmp/data")
    except:
      pass
  if x == "1":
    try:
      file = open("/tmp/data", 'r')
    except IOError:
      file = open("/tmp/data", 'w')
  dsrfile = open("/tmp/DSR", 'w')
  read = False
  while not os.path.exists("/tmp/DRD"):
    pass
print("Transmission complete")
