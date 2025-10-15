#     * * * * * * * * * 
#       * * * * * * * 
#         * * * * * 
#           * * * 
#             * 

num = int(input("Enter number :"))
for i in range(num):
      for j in range(i,0,-1):
            print(" ",end=" ")
      for k in range(i,num):
            if(i%2 != 0):
                  print(" * ",end=" ")
      print()