from fractions import Fraction
##Fraction class automatically reduces fractions

def enum():
    print "0"
    ls = []
    n = 1
    d = 1
    f = Fraction(n,d)
    count = 2
    while True:
        for i in range(count):
            f = Fraction(n,d)
            n = i + 1
            d = count - i
            if f not in ls:
                print str(f)
                print "-" + str(f)
                ls.append(f)
        count = count + 1
            
        
            

print enum()











