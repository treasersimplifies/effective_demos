__author__ = "* * treaser 2017 * * "

import sys
# import this

# effective python rule no.1
print(sys.version_info)
print(sys.version)
# rule no.3
chinese = "帮我拉下野，谢谢！"
chinese2 = chinese.encode('utf=8')
chinese = chinese2.decode('utf-8')
# rule no.5-no.6
cn = chinese[-1:1:-1]   # 注意如果是倒序输出，则要从-1到1，而不是1到-1
print(cn)
# rule no.7-no.8
list_character = ['I', ' ', 'a', 'm', ' ', 'a', ' ', 'p', 'o', 'e', 't']
list_number = range(1, 11)
square_filtered = [x**2 for x in list_number if x % 2 == 0]   # 列表推导
print(square_filtered)
two_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x**2 for row in two_d for x in row if x % 2 == 0]
print(flat)

