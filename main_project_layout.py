#___MAIN FILE...*___
# The program can be used to retrive marks of either a paticular student or the list of toppers in a paticular subject.

import Subjects as S,function_defination as F,student_details as SD
F.User_Check()
S.Clear_Sub_Files()
S.Read_Sample_File()
while(True):
    print('''\nList of Operations...)
1) Display Result
2) Display Student(s) with max. marks 
3) Exit\n
Enter your choice : ''',end='')
    n1=int(input())
    
    if n1==1:
        SD.board_result()
    elif n1==2:
        while(True):
            print('''\nSelect Subject...
1) Physics
2) Chemistry
3) Mathematics
4) Biology
5) English Core
6) History
7) Political Science
8) Economics
9) Business Studies
10)Accountancy
11)Optional Subjects
12)Return to previous Menu
Enter your choice : ''',end='')
            n2=int(input())
            if n2==1:
                S.File_open("Physics")
            elif n2==2:
                S.File_open("Chemistry")       # write original =subject names as parameter
            elif n2==3:
                S.File_open("Mathematics")
            elif n2==5:
                S.File_open("English Core")
            elif n2==4:
                S.File_open("Biology")
            elif n2==6:
                S.File_open("History")       # write original =subject names as parameter
            elif n2==7:
                S.File_open("Political Science")
            elif n2==8:
                S.File_open("English Core")
            elif n2==9:
                S.File_open("Economics")
            elif n2==10:
                S.File_open("Chemistry")       # write original =subject names as parameter
            elif n2==12:
                    break                 #S.File_open("Maths")
            elif n2==11:
                while(True):
                    print('''\n1)Computer Science
2) Geography
3) Hind Music Vocal
4) Commercial Art
5) Physical Education
6) Hindi Core
7) Legal Studies
8) Psychology
9) Sociology
10)Biotechnology
11)Sculpture
12) Return to previous Menu
Enter your choice : ''',end='')
                    n3=int(input())
                    if n3==1:
                        S.File_open("Computer Science")
                    if n3==2:
                        S.File_open("Geography")
                    if n3==3:
                        S.File_open("Vocal Music")
                    if n3==4:
                        S.File_open("Commercial Art")
                    if n3==5:
                        S.File_open("Physical Education")
                    if n3==6:
                        S.File_open("Hindi")
                    if n3==8:
                        break
                    
            elif n2==11:
                break
            
    elif n1==3:
        break
