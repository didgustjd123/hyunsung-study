def push(n):
    lst.append(n)

def size():
    return len(lst)

def empty():
    if len(lst)==0:
        return 1
    else:
        return 0

def pop():
    try:
        print(lst.pop())
    except:
        print(-1)

def top():
    try:
        print(lst[-1])
    except:
        print(-1)

N=int(input())
lst=[]
for _ in range(N):
    cmd=input().split()
    if cmd[0]=='push':
        push(int(cmd[1]))

    elif cmd[0]=='size':
        print(size())

    elif cmd[0]=='empty':
        print(empty())

    elif cmd[0]=='pop':
        pop()

    elif cmd[0]=='top':
        top()

T=int(input())
for i in range(T):
    vps=[]
    cn=0
    parent=input()
    for j in range(len(parent)):
        if parent[j]=="(":
            vps.append(parent[j])
        else:
            if len(vps)>=1:
                vps.pop()
            else:
                cn+=1
    if len(vps)==0 and cn==0:
        print('yes')
    else:
        print('no')

def push(x):
    ls.append(x)

def pop():
    try:
        ls.pop(0)
    except:
        print(-1)

def size():
    return len(ls)

def empty():
    if len(ls)==0:
        return 1
    else:
        return 0

def front():
    try:
        print(ls[0])
    except:
        print(-1)

def back():
    try:
        print(ls[-1])
    except:
        print(-1)

ls=[]
cn=int(input())
for i in range(cn):
    t=input().split()
    if t[0]=="push":
        push(int(t[1]))
    elif t[0]=="pop":
        pop()
    elif t[0]=="size":
        print(size())
    elif t[0]=="empty":
        print(empty())
    elif t[0]=="front":
        front()
    elif t[0]=="back":
        back()
