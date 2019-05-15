import math
int_val=4
int_val2=2
print(int_val+int_val2)
print('%d + %d = %d' % (int_val,int_val2,int_val+int_val2))
print(int_val ** int_val2)
print(type(int_val))
int_val='abc'
print(int_val)
print(type(int_val))

print('华氏摄氏度转摄氏度 F=1.8C+32')

# hsd = float(input('请输入华氏摄氏度:'))
hsd = 72
ssd = (hsd-32)/1.8
print(' %.1f华氏度等于%.1f摄氏度' % (hsd,ssd))
#半径
raudios = 24
# 周长
perim = 2 * math.pi * raudios
# 面积
area = math.pi * raudios *raudios

print('半径: %.2f 周长: %.2f 面积:%.2f' % (raudios,perim,area))