v=int(input('Please input your estimate number of visitors:'))


for i in range(0,v+1):

    su=i/10
    subfee=15*su
    ad=0.8*i

    if i<50000:
        net=subfee+ad-200000
    else:
        net=subfee+ad-200000-0.001*(i-50000)
    if net>=0:
        print('visitor=',i)
        break
if net<0:
    print('net income is',net)
