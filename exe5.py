"""print("managment system")
a=int(input("1 for give and 2 for output"))
if a==1:
    b=input("1 for mohon 2 for rohan 3 for shyam")
    # take(k)
else:
    b=input("1 for mohon 2 for rohan 3 for shyam")
    output(b)
"""
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("1 for exercise and 2 for food"))
        if c==1:
            value=input("type here\n")
            with open("mohan_exe.txt","a") as op:
                op.write(str([str(gettime())])+" : "+value+ "\n")
            print("written success")
        elif c==2:
            value = input("type here\n")
            with open("mohan_food.txt","a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("written success")
    elif k==2:
        c = int(input("1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("rohan_exe.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("written success")
        elif c == 2:
            value = input("type here\n")
            with open("rohan_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("written success")
    elif k==3:
        c = int(input("1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("shyam_exe.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("written success")
        elif c == 2:
            value = input("type here\n")
            with open("shyam_food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("written success")
        else:
            print("please enter valid value")
def retrieve(k):
    if k==1:
        c=int(input("1 for exercise and 2 for food:"))
        if (c==1):
            with open("mohan_exe.txt") as op:
                for i in op:
                    print(i,end="")
        elif (c==2):
            with open("mohan_food.txt") as op:
                for i in op:
                    print(i,end="")
    elif (k==2):
        c=int(input("1 for exercise and 2 for food"))
        if (c==1):
            with open("rohan_exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c==2):
            with open("rohan_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==3:
        c=int(input("1 for exercise and 2 for food"))
        if (c==1):
            with open("shyam_exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c==2):
            with open("shyam_food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print(" enter valid number")

print("managment system")
a=int(input("1 for lock and 2 for retrieve"))
if a==1:
    b=int(input("1 for mohon and 2 for rohan and 3 for shyam"))
    take(b)
else:
    b=int(input("1 for mohon and 2 for rohan and 3 for shyam"))
    retrieve(b)





