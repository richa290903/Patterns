#   *         *
#   * *     * *
#   * * * * * *
#   * * * * * * 
#   * *     * *
#   *         *


for i in range(4,0,-1):
      for j in range(i,4,1):
            print("*",end=" ")
      for k in range(1,i):
            print(" ",end=' ')
      for m in range(i,1,-1):
            print(" ",end=' ')
      for n in range(i,4,1):
            print("*",end=" ")
      print()   


for i in range(4,0,-1):
      for j in range(1,i):
            print("*",end=" ")
      for k in range(i,4,1):
            print(" ",end=" ")
      for m in range(i,4):
            print(" ",end=" ")
      for n in range(i,1,-1):
            print("*",end=" ")
      print()