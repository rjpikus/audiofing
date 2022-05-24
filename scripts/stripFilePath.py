#L = open("print2.txt", "w").read().splitlines()
#for line in L:
 #   line.removeprefix('audio-fingerprint-identifying-python')

a_file = open("print2.txt", "r")

s = ""
for line in a_file:
  sline = line.strip()
  stripped_line = sline.split("audio-fingerprint-identifying-python\\",1)[1] 
  substring = ".py"
  if substring in stripped_line:
    s += stripped_line + " "

a_file.close()
print(s)

