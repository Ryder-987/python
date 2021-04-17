old_str="05050:05050:05050:99999:09990"
img_list=old_str.split(':')
length=len(img_list)
print(length)
print(img_list)

img_list[0]='55555'
new_str=':'.join(img_list)
print(new_str)