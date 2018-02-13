


import random
import os


###############################################################################

#A little code for interfacing the SAT solver sat4j to Python.
#The jar file either has to reside in the same directory as the
#one in which this program is run, or the code has to be modified
#to include the path name for sat4j.jar.

#The function satsolve takes as an argument a list of lists of
#integers. Each list of integers is a clause in a CNF formula.
#Positive entries 1,2,3,... denote un-negated literals p_1,p_2, etc.
#Negative entries -1,-2,-3 denote the corresponding negated literals.

#satsolve uses the list to create a CNF specification file in
#in DIMACS format, then makes a system call to sat4j to solve it.
#The output is redirected to a temporary file.

#The function then captures this output, and returns a Python dictionary.
#If the formula is unsatisfiable, the dictionary is empty.  Otherwise it
#contains a satisfying assignment in the format {1:False,2:True,...}.

#The specification file and the raw output of sat4j are left around for you
#to inspect. If you call with the keyword cleanup set to be True, the files are
#removed

def satsolve(cnf,cleanup=False):
    idtag=random.randint(100000,999999)
    numclauses=len(cnf)
    numvars=max([max([abs(x) for x in y])for y in cnf])
    specfilename=str(idtag)+'.spec'
    solutionfilename=str(idtag)+'.solution'
    f=open(specfilename,'w')
    f.write('p cnf '+str(numvars)+ ' '+str(numclauses)+'\n')
    for clause in cnf:
        for literal in clause:
            f.write(str(literal)+' ')
        f.write('0\n')
    f.close()
    os.system('java -jar sat4j.jar'+' '+specfilename + '>' + solutionfilename)
    solution={}
    f2 = open(solutionfilename,'r')
    nextline = f2.readline()
    #read lines until you see the tag 'SATISFIABLE' or 'UNSATISFIABLE'
    while ('SATISFIABLE' not in nextline):
        nextline=f2.readline()
    if nextline[2]!='U': #cnf is satisfiable, so we fill solution with assignment
        nextline=f2.readline()
        nextline=nextline[1:]
        tokens=nextline.split()
        j=0
        while(tokens[j]!='0'):
            variable=abs(int(tokens[j]))
            if tokens[j][0]=='-':
                solution[variable]=False
            else:
                solution[variable]=True
            j+=1
    if cleanup:
        os.remove(specfilename)
        os.remove(solutionfilename)
    return solution
    
        
 
    
