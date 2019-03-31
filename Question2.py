def allzero(s):
    if s.count('0')==len(s):
        return 1
    else:
        return 0
def add(p, q):
    r = str(int(p[0])^int(q[0]))
    for i in range(1,len(p)):
        r=r+str(int(p[i])^int(q[i]))
    return r
def distance(p, q):
    k=0
    for i in range(0,len(p)):
        if p[i]==q[i]:
            k+=1
    return len(p)-k
def weight(p):
    return p.count('1')
        
N = int(input("The length of codeword is:"))

K = int(input("The number of information bits are:"))

T = int(input("The number of (n,k) codewords you want to enter:"))

S = []
flag1=0
flag2=0
flag3=0
for _ in range(0,T):
    I = input("Enter the codeword:")
    S.append(I)
#####condition one there should be atleast one all zero code present
for i in range(0,T):
    if(allzero(S[i])==1):
        flag1=1
        break
####sum of two codeword must be present in the codewords and dist of the two codewords must be equal to weight of the summed codeword
Dist=[]
Weight=[]
for i in range(0,T):
    for j in range(0,T):
        W=add(S[i],S[j])
        print("The codeword added",S[i],"^",S[j],"=",W)
        if W in S:
            print("distance is:" ,distance(S[i],S[j]),"and weight is:",weight(W))
            if(distance(S[i],S[j])==weight(W)):
                Dist.append(distance(S[i],S[j]))
                Weight.append(weight(W))
                flag2+=1
            else:
                break
        else:
            break
###minimum distance of the codeword == minimum weight of the codeword
if min(Dist)==min(Weight):
    flag3=1
if flag1==1 and flag2==T*T and flag3==1:
    print("Yes, linear block code word")
else:
    print("No, not a linear block code word") 
