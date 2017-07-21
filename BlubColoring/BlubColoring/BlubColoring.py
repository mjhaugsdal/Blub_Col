
##
## Blub Coloring
##
##
 


global k

def main():

    print("Original Data:")
    DataList = [[ 0,  0,  0 , 0, 0,   0,  0,  0, 0, 0, 0, 0 ],
                [ 0, 'x','x','x','x','x', 0, 'x',0,0,'x', 0 ],
                [ 0, 'x', 0 , 0, 0,  'x', 0, 'x',0,'x',0, 0 ],
                [ 0, 'x','x','x','x','x', 0, 'x','x', 0,0,0 ],
                [ 0, 'x', 0 , 0, 0,  'x', 0, 'x',0,'x',0, 0 ],
                [ 0, 'x', 0 , 0, 0,  'x', 0, 'x',0,0,'x', 0 ],
                [ 0,  0 , 0, 0,   0,  0,  0, 0, 0, 0, 0 , 0 ]]

   
    #print (DataList)

    #Print Original Data:
    for x in range (0, 7):
        print("")
        for y in range (0, 11):
            if DataList[x][y] == 0:
                print (' ', end = "")
            else:
                print (DataList[x][y] , end="" ) 


    print('\n')

 
    #Copy List, keep old
    f = DataList[:]
  
    #Original color
    k = 1

    #Color(x,y) is the color of a blob containing (x,y)

    #Scan looking for a blob.
    for x in range (0, 5):
        for y in range (0, 10):
            if(DataList[x][y]  != 0):
                #print(x,y)
                f[x][y] = k
   
    #f[i][j] = k # Our first Blob

    #Scan left->right, top->bottom

    for x in range (0, 7):
        for y in range (0, 11):
            if f[x][y] != 0:
                
                #IF F(xu,yu = 1 & f(xl, yl = 0)

                if f[x-1][y] != 0 and f[x][y-1] == 0:
                   # print("COLOR XC == XU")
                    f[x][y] = f[x-1][y]
                
                #IF f(xl, yl) = 1 & f(xu, yu) = 0
                if f[x][y-1] != 0 and f[x-1][y] == 0:
                    
                    f[x][y] = f[x][y-1]
                    #color (xc,yc) = color(xl,yl)

                #if f(xl, yl) = 1  & f(xu, yu) = 1
                if f[x-1][y] != 0 and f[x][y-1] != 0 :
                   
                   #
                   f[x][y] = f[x][y-1]
                   #
                   f[x][y-1] = f[x-1][y]


                   #color (xc,yc) = color(xl,yl)

                #Diagonal!
                #Check Down+Left, Down+right, Up+Left, Up+Right
                
                #

                if f[x-1][y] == 0 and f[x][y-1] == 0:

                    if f[x+1][y-1] != 0 or f[x-1][y-1] != 0:

                        f[x][y] = k-1
                    
                    else:
                        f[x][y] = k
                        k+=1            
                   
                    #if()




               # if f[x][y+1]] == 1 and f[x-1][y]]

    
    print("New image")
    for x in range (0, 7):
        print("")
        for y in range (0, 11):
            if f[x][y] == 0:
                print (' ', end = "")
            else:
                print (f[x][y] , end="" ) 


    print('\n')





def COLOR(x,y):



    return color

main()


