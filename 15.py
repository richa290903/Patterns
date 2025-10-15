#     *       *
#       *   *   
#         *    
#       *   *  
#     *       *

for i in range(5):
      for j in range(5):
            if(j==i or j==5-i-1):
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()
              