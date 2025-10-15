#   *         *
#   * *     * *
#   *   * *   *
#   *   * *   * 
#   * *     * *
#   *         *



for i in range(6,0,-1):
      for j in range(i,6,1):
            if(j==5 or j==i):
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      for k in range(1,i):
            print(" ",end=' ')
      for m in range(i,1,-1):
            print(" ",end=' ')
      for n in range(i,6,1):
            if(n==5 or n==1 or n==i):
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()   


for i in range(6,0,-1):
      for j in range(1,i):
            if(j==1 or j==5 or j>=i-1):
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      for k in range(i,6,1):
            print(" ",end=" ")
      for m in range(i,6):
            print(" ",end=" ")
      for n in range(i,1,-1):
            if(n==2 or n==6 or n==i):
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()