"""A Module for Grading just call finalapp() and Start the app"""
def app():
    def voidfunc():
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    def Grader(i):
        """Collect Percentage in Floats and Return Percentage"""
        if ((i>=80.0)&(i<=100.0)):
            return "A"
        elif ((i>=70.0)&(i<80.0)):
            return "B+"
        elif ((i>=60.0)&(i<70.0)):
            return "B"
        elif ((i>=50.0)&(i<60.0)):
            return "C+"
        elif ((i>=45.0)&(i<50.0)):
            return "C"
        elif ((i>=40.0)&(i<45.0)):
            return "D"
        elif ((i>=39.0)&(i<40.0)):
            return "D-"
        elif ((i<39.0)&(i>=0.0)):
            return "F"
        else:
            return "Invalid Percentage"
    voidfunc()
    print("\t\t A Grading System")
    voidfunc()
    no_sub=int(input("\t Enter Number of Subjects"))
    print("\t Enter Number of Subjects:",no_sub)
    after_sub=no_sub
    voidfunc()
    marks=[]
    total_marks=0.0
    
    while no_sub>0:
        ma=float(input("\t Enter Marks of Subject: "))
        print("\t Enter Marks of Subject:",ma)
        if ma>100:
            print("Invalid marks please Try Again and Enter marks between 0 and 100")
        elif ((ma>=0.0)&(ma<=100.0)):
            marks.append(ma)
            total_marks+=ma
            no_sub-=1
        else:
            print("Invalid Input !!!!!!")
    voidfunc()
    print("Total Marks Obtained in",after_sub,"Subjects is:",total_marks)
    percentage=(total_marks/(after_sub*100))*100
    print("Obtained Percentage By Student {:.2f} : ".format(percentage))
    voidfunc()
    grade_return=Grader(percentage)
    print("\t Grade Of Student is:",grade_return)
    voidfunc()


def finalapp():
    ch=True
    while ch:
        inp=input("Do You Want To Continue Yes or No ( Y/N ): ")
        print("Do You Want To Continue Yes or No ( Y/N ): ",inp)
        inp=inp.lower()
        if ((inp=="yes") | (inp=="y")) :
            app()
      
        elif ((inp=="no") | (inp=="n")):
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\t Thanks For Using The System.......")
            ch=False
       
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\t Invalid Input !!!!!")