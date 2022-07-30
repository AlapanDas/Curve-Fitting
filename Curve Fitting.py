import csv
import matplotlib.pyplot as plt
import numpy as np
n=0
X=0
Y=0
sum_of_y=0
sum_of_x=0
sum_of_xsquare=0
sum_of_xy=0
sum_of_xcube=0
sum_of_xquad=0
sum_of_yxsquare=0
choice=int(input("Enter 1 for Straight Line and 2 for Parabola"))
f=open(r"data.csv")
text=csv.reader(f)
for i in text:    
     if(i==[]):
          break; 
     sum_of_x+=float(i[0])
     sum_of_y+=float(i[1])
     sum_of_xy+=(float(i[0])*float(i[1]))
     sum_of_xsquare+=float(i[0])**2
     sum_of_xcube+=float(i[0])**3
     sum_of_xquad+=float(i[0])**4
     sum_of_yxsquare+=(float(i[0])**2)*float(i[1])
     n+=1
     # next(text)
if(choice==1):
     a=round(((n*sum_of_xy)-(sum_of_y*sum_of_x))/(n*sum_of_xsquare-(sum_of_x**2)),3)
     b=round(((sum_of_y-((n*sum_of_xy-(sum_of_x*sum_of_y))/(n*sum_of_xsquare - sum_of_x**2)*sum_of_x))/n),3)
     if(b<0):
          print("y=({})x+({})".format(a,b))
          Y=a
          X=-b/a
     else:
          Y=b
          X=-a/b
          print("y=({})x+({})".format(b,a))
     xpoints=np.array([0,X])
     ypoints=np.array([0,Y])
     plt.plot(xpoints,ypoints)
elif(choice==2):
     A=np.array([[n,sum_of_x,sum_of_xsquare],[sum_of_x,sum_of_xsquare,sum_of_xcube],[sum_of_xsquare,sum_of_xcube,sum_of_xquad]])
     B=np.array([sum_of_y,sum_of_xy,sum_of_yxsquare])
     try:
          C=np.linalg.solve(A,B)
          print("y=({:.2f})x^2+({:.2f})x+({:.2f})".format(C[0],C[1],C[2]))
          x=np.linspace(-10,10,100)
          y=C[0]*x**2 + C[1]*x + C[2]
          fig=plt.figure()
          plt.plot(x,y)
          plt.show()
     except:
          print("Singular Error ")


plt.show()