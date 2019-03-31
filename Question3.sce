clear;
I = input("Enter the information bits in matrix format([1 0 0 1]): ")
info = flipdim(I,2)

subplot(2,2,1);
bar(I,0,'white');
bar(I,1,'green');
title("Info bit","fontsize",3);
p1 = poly(info , 'x' , 'c')
g1 = [1, 1, 0, 1]
p2=p1*poly([0 0 0 1], 'x', 'c')
p3=p2
g1x = poly(g1, 'x', 'c')
j=0
while(degree(p2) >= degree(g1x))
    m(degree(p2)-degree(g1x)+1)=1
    mul=poly(m,'x','c')
    d=g1x*mul
    p2=bitxor(coeff(p2),coeff(d))
    for j=length(p2):-1:1
        if p2(j)==1 then
            p2=p2(1:j)
            break
        end
    end
    p2 = poly(p2 , 'x' , 'c')
    m=0
end
p2=coeff(p2)
p2(length(p2)+1:degree(p3)+1)=0
C=bitxor(p2,coeff(p3))
C=flipdim(C,2)
disp(C,"Codeword =");
subplot(2,2,2);

bar(C,0,'white');
bar(C,1,'blue');
title("Encoded Code word","fontsize",3);
//syndrome Decoding

clear;
R = input("Enter the received word in matrix format with spaces([1 0 0 1 1 1 1]]): ")
 r= flipdim(R,2)
subplot(2,2,3);
bar(R,0,'white');
bar(R,1,'green');
title("Received word","fontsize",3);
 Rx = poly(r,'x','c')
g1 = [1, 1, 0, 1]
g1x = poly(g1, 'x', 'c')
while(degree( Rx) >= degree(g1x))
     m(degree( Rx)-degree(g1x)+1)=1
     mul=poly(m,'x','c')
     d=g1x*mul
      Rx=bitxor(coeff( Rx),coeff(d))
     for j=length( Rx):-1:1
         if  Rx(j)==1 then
              Rx= Rx(1:j)
             break
         end
     end
      Rx = poly( Rx , 'x' , 'c')
     m=0
 end
 S=coeff( Rx)
 S(1,length( S)+1:3)=0
st = [0 0 0; 1 0 0; 0 1 0; 0 0 1; 1 1 0; 0 1 1; 1 1 1; 1 0 1]
for i = 1:8
    if  S==st(i,:) then
        e(i-1)=1
        break
    end
end
e(i:7)=0
e=flipdim(e',2);
r=flipdim(r,2);
disp(r);
C=bitxor(r,e);
disp(C,'codeword =')
subplot(2,2,4);
bar(C,0,'white');
bar(C,1,'blue');
title("Decoded code word","fontsize",3);
