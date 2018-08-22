class Student:
    Studentlist=[]
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        Student.Studentlist.append(self)
    def display(self):
        print(self.name)
def read():
    f=open('Student.txt','r')
    for line in f:
        l=line.split()
        if l:
            Student(l[0],int(l[1]),int(l[2]))
        else:
            break
read()
while 1!=0:
    print("Enter Your choice")
    print("1. Add a student")
    print("2. print all Student info")
    print("3. Search Student by name")
    print("4. search Student by roll no.")
    print("5. update by roll no.")
    print("6. save to file")
    print("7.Exit")
    ch=int(input())
    if ch==1:
        print("Enter the name")
        name=input().strip()
        flag=False
        if len(name)<4:
            print("Invalid Input")
            flag=True
        for a in name:
            try:
                b=int(a)
                print("Invalid input")
                flag=True
                break
            except:
                continue
        if flag:
            continue
        print("Enter the roll")
        try:
            roll=int(input())
            if len(str(roll))<2:
                print("Invalid Input")
                continue
        except:
            print("Invalid Input")
            continue
        print("Enter the marks")
        try:
            marks=int(input())
        except:
            print("Invalid Input")
            continue
        d=Student(name,roll,marks)
    elif ch==2:
        for a in Student.Studentlist:
            print(a.name)
            print(a.roll)
            print(a.marks)
    elif ch==3:
        print("Enter the name")
        name=input().strip()
        flag=False
        if len(name)<4:
            print("Invalid Input")
            flag=True
        for a in name:
            try:
                b=int(a)
                print("Invalid input")
                flag=True
                break
            except:
                continue
        if flag:
            continue
        for a in Student.Studentlist:
            if a.name==name:
                print("Found",a.name)
                print("Rollno",a.roll)
                print("marks",a.marks)
                break
        else:
            print("Notfound")
    elif ch==4:
        print("Enter the Rollno")
        try:
            roll=int(input())
            if len(str(roll))<2:
                print("Invalid Input")
                continue
        except:
            print("Invalid Input")
            continue
        for a in Student.Studentlist:
            if a.roll==roll:
                print("Found",a.name)
                print("Rollno",a.roll)
                print("marks",a.marks)
                break
        else:
            print("Notfound")
    elif ch==5:
        print("Enter the Rollno")
        try:
            roll=int(input())
            if len(str(roll))<2:
                print("Invalid Input")
                continue
        except:
            print("Invalid Input")
            continue
        for a in Student.Studentlist:
            if a.roll==roll:
                print("Enter the new marks")
                try:
                    marks=int(input())
                except:
                    print("Invalid Input")
                    break
                a.marks=marks
                print("Name",a.name)
                print("Roll",a.roll)
                print("Marks",a.marks)
                break
        else:
            print("Notfound")
    elif ch==6:
        f=open('Student.txt','w+')
        for a in Student.Studentlist:
            string=a.name+" "+str(a.roll)+" "+str(a.marks)
            f.write(string+'\n')
        f.close()
    elif ch==7:
        break
    else:
        print("Invalid Input")
