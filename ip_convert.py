# coding=utf-8
'''
convert ip into binary form.
'''
ip = raw_input()
ip_list = ip.split('.')
converted_ip_list = []
for i in ip_list:
    t = bin(int(i)).split('b')[1]
    if len(t) < 8:
        t = (8 - len(t)) * '0' + t
    converted_ip_list.append(t)
print '.'.join(converted_ip_list)
