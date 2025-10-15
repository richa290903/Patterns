#              *    
#            *   *
#          *       *  
#        *           * 
#      * * * * * * * * * 


for i in range(6,0,-1):
      for j in range(i,0,-1):
            print(" ",end=" ")
      for k in range(i,6,1):
            if ((i<=k-1) and (i!=1)) and (k!=6-1):
                  print("   ",end=" ")
            else:
                  print(" * ",end=" ")
      print()
      
