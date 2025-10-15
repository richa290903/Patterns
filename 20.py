#     *   * * *
#     *   *  
#     * * * * *
#         *   *
#     * * *   *


for i in range(11):
      for j in range(11):
            if ((j==0 and i<5) or (j==5) or (i==5) or (i==0 and j>5) or (j==10 and i>5) or (i==10 and j<5)):
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()