info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
new_id = input('请输入新的学号')
info['id'] = int(new_id)
print('修改之后的id为：%d' % info['id'])
