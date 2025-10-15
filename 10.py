#     * 
#     * *  
#     *   * 
#     *     * 
#     * * * * *

for i in range(6):
      for j in range(i):
            if(i==0 or j==0 or i==5 or j>=i-1  ):
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()