'''
Assignment 3 for BIM A+3
calculating different geometrical characteristics of a polygon shape
Date: 01/12/2019
Author: Lizhen Qin
'''

#数据读入
#enter the coordinates
print('Enter x and y coordinates for polygon points: ',end='')
points_num=int(input())
#判断是否是多边形
#Determine if it is a polygon
if points_num <3:
    print("Error!!!!!!!It is not a polygon!!!!!")

else:
    print('\n'+'Enter x and y coordinates for polygon points ...'+'\n'+'TIP: the points must be ordered counter clockwise ^_^')
    x=[]
    y=[]

    for num in range(points_num):
        print('Point '+str(num+1)+': ',end='')
        xi,yi=(map(float,input().split()))
        x.append(xi)
        y.append(yi)


#输出点的坐标
#Output the coordinates of the points
    print('\n'+'Point'+'\t'+'x'+'\t'+'y')
    print('-'*20)
    for num in range(points_num):
        print(' '+str(num+1)+'%.2f' %x[num] +'\t'+ '%.2f' %y[num])
        
    print(' ')


#参数定义
#define Parameters 
    Ax_sum=0
    Sx_sum=0
    Sy_sum=0
    Ix_sum=0
    Iy_sum=0
    Iy_sum=0
    Ixy_sum=0

#参数求和部分计算
#Parameter summation-part of calculation
    for i in range(points_num):
        if i<points_num-1:
            i0=i
            i1=i+1
        else:
            i0=i
            i1=0
        
        x_plus=x[i1]+x[i0]
        x_minus=x[i1]-x[i0]
        y_plus=y[i1]+y[i0]
        y_minus=y[i1]-y[i0]
        x_multi=x[i1]*x[i0]
        y_multi=y[i1]*y[i0]

        Ax_sum += x_plus*y_minus
        Sx_sum += x_minus*(pow(y_plus,2)-y_multi)
        Sy_sum += y_minus*(pow(x_plus,2)-x_multi)
        Ix_sum += x_minus*y_plus*(pow(y[i0],2)+pow(y[i1],2))
        Iy_sum += y_minus*x_plus*(pow(x[i0],2)+pow(x[i1],2))
        Ixy_sum += y_minus * ( (y[i1])*(pow(x_plus,2)+2*pow(x[i1],2)) + y[i0]*(pow(x_plus,2)+2*pow(x[i0],2)) )

#参数计算
#Parameter calculation
    Ax=1/2*Ax_sum
    Sx=-1/6*Sx_sum
    Sy=1/6*Sy_sum
    Ix=-1/12*Ix_sum
    Iy=1/12*Iy_sum
    Ixy=-1/24*Ixy_sum

    xt=Sy/Ax
    yt=Sx/Ax

    Ixt=Ix-pow(yt,2)*Ax
    Iyt=Iy-pow(xt,2)*Ax
    Ixyt=Ixy+xt*yt*Ax

#输出结果
#output the results
    print('Geometric characteristics:')
    print('Ax:'+'\t'+'%.2f' %Ax)
    print('Sx:'+'\t'+'%.2f' %Sx)
    print('Sx:'+'\t'+'%.2f' %Sy)
    print('Ix:'+'\t'+'%.2f' %Ix)
    print('Ix:'+'\t'+'%.2f' %Iy)
    print('Ixy:'+'\t'+'%.2f' %Ixy)
    print('xt:'+'\t'+'%.2f' %xt)
    print('yt:'+'\t'+'%.2f' %yt)
    print('Ixt:'+'\t'+'%.2f' %Ixt)
    print('Iyt:'+'\t'+'%.2f' %Iyt)
    print('Ixyt:'+'\t'+'%.2f' %Ixyt)

