'''
str = :00000:0000"00000:00000:000000"

請使用list 分割及重組元素

[99999:00000:00000:00000:00000]  第一圈
[00000:99999:00000:00000:00000]  第二圈
[00000:00000:99999:00000:00000]  第三圈
[00000:00000:00000:99999:00000]  第四圈
[00000:00000:00000:00000:99999]  第五圈
'''

old_str='00000:00000:00000:00000:00000'
img_list= old_str.split(':') #用冒號分割字串
img_list[0]='99999'
new_str=':'.join(img_list) #用冒號連結list
print(new_str)
for i in range(4):
    img_list[i]='00000'
    img_list[i+1]='99999'
    new_str=':'.join(img_list) #用冒號連結list
    print(new_str)