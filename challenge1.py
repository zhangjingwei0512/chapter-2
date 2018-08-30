v=int(input('Please input your estimate number of visitors:'))
su=v/10
subfee=15*su
ad=0.8*v
if v<50000:
    net=subfee+ad-200000
else:
    net=subfee+ad-200000-0.001*(v-50000)
print(net)
