####question1 generate a (7, 4) hamming code
import matplotlib.pyplot as plt
import numpy as np
def plot_bar(C, T):
    x = []
    for i in range(0,len(C)):
                   if C[i]==1:
                       x.append(i+1)
    plt.bar(x,height=1,width=0.2,align="center")
    tic=[k for k in range(1,len(C)+1)] 
    plt.xticks(tic,tuple(tic))
    plt.title(T)
    
I = input("information code") ####information code

info =[]
for i in I:
    info.append(int(i))
    

label1 = info

P1 = str(int(I[0])^int(I[1])^int(I[2]))
P2 = str(int(I[1])^int(I[2])^int(I[3]))
P3 = str(int(I[0])^int(I[1])^int(I[3]))

plt.title("Codeword from Information word")
plt.subplot(2,1,1)
plot_bar(label1,"Information word")

print("The parity bits are",P1,P2,P3)
I=I+P1+P2+P3

IW =[]
for i in I:
    IW.append(int(i))

label2 = IW
plt.subplot(2,1,2)
plot_bar(label2,"codeword")
plt.show()

print("The output codeword is", I)

W = input("The codeword recieved is")
S1 = str(int(W[0])^int(W[1])^int(W[2])^int(W[4]))
S2 = str(int(W[1])^int(W[2])^int(W[3])^int(W[5]))
S3 = str(int(W[0])^int(W[1])^int(W[3])^int(W[6]))

RW = []
for i in W:
    RW.append(int(i))


print("The syndrome is",S1,S2,S3)

if S1=='0':
    if S2=='0':
        if S3=='0':
            E="0000000"
        else:
            E="0000001"
    else:
        if S3=="0":
            E="0000010"
        else:
            E="0001000"
else:
    if S2=='0':
        if S3=='0':
            E="0000100"
        else:
            E="1000000"
    else:
        if S3=="0":
            E="0010000"
        else:
            E="0100000"
C = str(int(W[0])^int(E[0]))
for i in range(1,7):
    C =C+str(int(W[i])^int(E[i]))

OW = []
for i in C:
    OW.append(int(i))
K = OW
plt.title("Codeword from recieved word")
plt.subplot(2,1,1)
plot_bar(RW,"recieved word")
plt.subplot(2,1,2)
plot_bar(K,"codeword");
plt.show()
print("The input string obtain is ",C);
    
            
