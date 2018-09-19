#kadai02x 16D8101021C 野口大輔　2017-10-02

for i in range(1,100):
 for j in range(i,100):
  for k in range(j,100):
   if i+j+k<100 and i**2+j**2==k**2:
    print(i+j+k,"(",i,"",j,"",k,")")

