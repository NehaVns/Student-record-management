import function_defination as F           
def board_result():
    read_file=open("Sample_Data.txt","r")
    data=' '
    board_RollNo=input("Enter the Board roll no. : ")
    while data:
        data=read_file.readline()
        l=data.split()
        if len(l)>=21:
            if l[0].isdigit() and l[0]==board_RollNo:
                L,marks_percentage=[],[]
                Roll_No=l[0]
                L.append(Roll_No)
                Name=''
                for i in range(1,len(l)):
                    if l[i].isdigit():
                        L.append(Name)
                        break
                    else:
                        Name=Name+l[i]+" "
                for j in range(i,i+13,3):
                    Scode=l[j]
                    Marks=l[j+1]
                    Grade=l[j+2]
                    subject=F.Subject(Scode)
                    marks_details=[subject,Marks,Grade]
                    L.extend(marks_details)
                    marks_percentage.append(Marks)
                percentage=F.percentage(marks_percentage)
                L.append(percentage)
                F.display_report_card(L)
                break
    else:
        print("Invalid Roll No.")
        
        
