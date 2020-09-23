from os import strerror
from sys import stdin

try:
    s = open("text.txt", "rt", encoding="utf-8")
    ch = s.read(1)
    while ch != "":
        print(ch, end="")
        ch = s.read(1)
    s.close()
except IOError as e:
    print("Oooooh noooo: ", strerror(e.errno))

try:
    s = open("text.txt", "rt", encoding="utf-8")
    content = s.readlines(200)
    print(content)
    s.close()
except IOError as e:
    print("Oooooh noooo: ", strerror(e.errno))

try:
    for line in open("text.txt", "rt", encoding="utf-8"):
        print(line, end="")
except IOError as e:
    print("Oooooh noooo: ", strerror(e.errno))


try:
    fo = open("newfile.txt" ,mode="wt", encoding="utf-8")
    for i in range(10):
        n = i + 1
        s = "Line #" + str(n) + "\n"
        fo.write(s)
    fo.close()
except IOError as e:
    print("Oooooh noooo: ", strerror(e.errno))
