with open("dz1.txt", "w+") as files:
   files.write('но у меня не получается')
   files.seek(0)
   dz1 = files.read()
with open("dz2.txt", "t") as s:
   dz = s.read()
with open('dz3.txt', 'h') as k:
   k.write(dz1 + "," + dz2)
