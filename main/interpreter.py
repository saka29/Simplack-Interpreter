'''Simplack interpreter
By Saka.
Bad, messy, and terrible because I'm not that good
at Python. But it has a debug option!

Because Python does not support multiline inputs, run from command line
and put the name of the file to be run for example:

interpreter.py hello.txt

See https://esolangs.org/wiki/Simplack'''
import sys
file = open(sys.argv[1])
code = file.read()
code = code.splitlines()
stack = []
done = False
debug = False

point = 0
while done == False:
    l = code[point]
    line = l.split()
    ins = line[0]
    if debug == True:
        print("Instruction: ",l)
        print("Stack: ",stack)
    if l[0]=='#':
        point += 1
    elif ins == 'input':
        if line[1] == 'a':
            inp = input('>>')
            for x in inp:
                stack.append(ord(x))
        elif line[1] == 'i':
            inp = input('>>')
            stack.append(int(inp))
        else:
            print("ERROR ON LINE ",str(point))
            done = True
        point += 1
    elif ins == 'output':
        item = stack[int(line[1])]
        if line[2] == 'a':
            print(chr(item),end='')
        elif line[2] == 'i':
            print(item,end='')
        else:
            print("ERROR ON LINE ",str(point))
            done = True
        point += 1
    elif ins == 'push':
        stack.append(int(line[1]))
        point += 1
    elif ins == 'pop':
        stack.pop(int(line[1]))
        point += 1
    elif ins == 'increase':
        if line[2][0] == '$':
            add = stack[int(line[2][1:])]
        else:
            add = int(line[2])
        stack[int(line[1])] = stack[int(line[1])] + add
        point += 1
    elif ins == 'set':
        if line[2][0] == '$':
            val = stack[int(line[2][1:])]
        else:
            val = int(line[2])
        stack[int(line[1])] = val
        point += 1
    elif ins == 'if':
        if line[2][0] == '$':
            check = stack[int(line[2][1:])]
        else:
            check = int(line[2])
        if stack[int(line[1])] == check:
            point = int(line[4])
        else:
            point += 1
    elif ins == 'goto':
        point = int(line[1])
    elif ins == 'exit':
        done = True
    if l==code[-1] and ins != 'goto':
        done = True
