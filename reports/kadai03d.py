#kadai03d 16D8101021C 野口大輔　2017-10-9

import matplotlib.pyplot as plt

f=open("temperature.txt","r")
sapporo=f.readline().split()
tokyo=f.readline().split()
miyazaki=f.readline().split()
f.close()

month=[i for i in range(1,13)]
plt.plot(month,sapporo)
plt.plot(month,tokyo)
plt.plot(month,miyazaki)
plt.show()

"""
どれがどの県かわからない
"""
