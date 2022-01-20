def Subject(Scode):
    if Scode=='301':
        subject="English Core" #  
    elif Scode=='302':
        subject="Hindi Core"   #  
    elif Scode=='052':
        subject="Commercial Art"  #
    elif Scode=='042':
        subject="Physics"  # 
    elif Scode=='043':
        subject="Chemistry"  # 
    elif Scode=='044':
        subject="Biology"   #
    elif Scode=='029':
        subject="Geography"   #
    elif Scode=='027':
        subject="History"  #   
    elif Scode=='028':
        subject="Political Science"  # 
    elif Scode=='030':
        subject="Economics" #
    elif Scode=='034':
        subject="Hind Music Vocal"  #
    elif Scode=='037':
        subject="Psychology"   #
    elif Scode=='039':
        subject="Sociology"   #   
    elif Scode=='041':
        subject="Mathematics"  #  
    elif Scode=='045':
        subject="Biotechnology"  # 
    elif Scode=='048':
        subject="Physical Education" # 
    elif Scode=='051':
        subject="Sculpture"  #  
    elif Scode=='054':
        subject="Business Studies"  #   
    elif Scode=='055':
        subject="Accountancy"    #
    elif Scode=='083':
        subject="Computer Science"   #
    elif Scode=='074':
        subject="Legal Studies"
    return subject

def display_report_card(L):
    print("")
    print("-----------------------------------------------------------")
    print("\t\tREPORT CARD 'Session 2019-20'")
    print("-----------------------------------------------------------")
    print("Board Roll No. :",L[0])
    print("Student name   :",L[1])
    print("Class          : 12","\n")
    print("-----------------------------------------------------------")
    print(" Subject                Max. Marks    Marks Scored    Grade")  #char max.
    print("-----------------------------------------------------------")
    print(formats(L[2],25),formats("100",15),formats(L[3],12),L[4])
    print(formats(L[5],25),formats("100",15),formats(L[6],12),L[7])
    print(formats(L[8],25),formats("100",15),formats(L[9],12),L[10])
    print(formats(L[11],25),formats("100",15),formats(L[12],12),L[13])
    print(formats(L[14],25),formats("100",15),formats(L[15],12),L[16])
    print("____________________________________________________________")
    print("Percentage : ",L[17],"%",sep='')
    print()
    
def formats(word,char):   #no. of spaces
    if len(word)==char:
        pass
    else:
        while(len(word)!=char):
            word=word+" "
        return word

def percentage(marks_percentage):
    total=0
    for i in marks_percentage:
        total+=int(i)
    percent=total/5
    return percent


def User_Check():
    UC=0
    UserName='Team'
    PassWord='isro123'
    print("Please enter following details to proceed:-")
    while(UC==0):
        U_name=input("Enter user name : ")
        if U_name==UserName:
            pswd=input("Enter password : ")
            if pswd==PassWord:
                print('\t-----------------------------------------')
                print("\t | Welcome To Report Management System | ")
                print('\t-----------------------------------------')
                UC=1
                break
            else:
                print("Invalid Password")
        else:
            print("Invalid user name")

def sorts(L):
    n=len(L)
    for i in range(n):
        for j in range(n-i-1):
            if L[j][1]<L[j+1][1]:
                L[j+1][1],L[j][1]=L[j][1],L[j+1][1]
                L[j+1][0],L[j][0]=L[j][0],L[j+1][0]
    return L
