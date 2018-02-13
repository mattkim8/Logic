from satsolve import *

#The beginning of a solution to the scheduling problem.  We will
#set up the CNF for the the schedule with only the basic constraints.
#These include the constraint that every course gets scheduled into
#exactly one slot, and that no slot holds more than one course. It
#leaves out the particular constraints like 'Chinese and Music' on the
#same day' and 'History in the morning'.

#Variable numbering:  There are 8 time slots 0,..,7 and 7 courses
#0,..,6.  The variable saying course i is scheduled in slot j is
#8*i+j+1, so for example, variables 1,2,3,..,8 correspond to course 0
#being scheduled in slots 0,...,7, variable 9 to course 1 in slot 0, etc.

#We'll use the following associations:
#Slot 0: Monday morning
#Slot 1: Monday afternoon...

#Slot 7: Friday afternoon.
#Note that Wednesday is not included.

#Courses 0-6:English, Math, Chinese, History, Computer Science, Philosophy, Music

#The function creates the cnf and calls the sat solver, returning
#a satisfying assignment if one exists.  Note that the return value is
#not in very user-friendly form.  Some additional work is required to
#turn it into a readable schedule.
def schedule():
    cnf=[]
    for course in range(7):
        nextclause=[]
        for slot in range(8):
            nextclause.append(8*course+slot+1)
        cnf.append(nextclause)
    for slot in range(8):
        for course in range(6):
            for course2 in range(course+1,7):
                cnf.append([-(8*course+slot+1),-(8*course2+slot+1)])
    for course in range(7):
        for slot in range(7):
            for slot2 in range(slot+1,8):
                cnf.append([-(8*course+slot+1),-(8*course+slot2+1)])
    #Here is where you will add particular constraints to the CNF:
    cnf.append([8])
    cnf.append([41,42])
    cnf.append([25,27,29,31])
    cnf.append([-17,50])
    cnf.append([-18,49])
    cnf.append([-19,52])
    cnf.append([-20,51])
    cnf.append([-21,54])
    cnf.append([-22,53])
    cnf.append([-23,56])
    cnf.append([-24,55])
    cnf.append([-51])
    return satsolve(cnf)
