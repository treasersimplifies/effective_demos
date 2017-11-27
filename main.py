__author__ = "* * treaser 2017 * * "

import sys
from demo_functions import *
from  demo_classes import *
# import this

# effective python rule no.1
print('=====rule no.1=====')
print(sys.version_info)
print(sys.version)

# rule no.3
print('=====rule no.3=====')
chinese = "帮我拉下野，谢谢！"
chinese2 = chinese.encode('utf=8')
chinese = chinese2.decode('utf-8')

# rule no.5-no.6
print('=====rule no.5-no.6=====')
cn = chinese[-1:1:-1]   # 注意如果是倒序输出，则要从-1到1，而不是1到-1
print(cn)

# rule no.7-no.8
print('=====rule no.7-no.8=====')
list_character = ['I', ' ', 'a', 'm', ' ', 'a', ' ', 'p', 'o', 'e', 't']
list_number = range(1, 11)
square_filtered = [x**2 for x in list_number if x % 2 == 0]   # 列表推导
print(square_filtered)
two_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x**2 for row in two_d for x in row if x % 2 == 0]
print(flat)

# rule no.9 generator displaces list by iterator
print('=====rule no.9=====')
a = []
b = []
i = 0
points = ((a[4*i+3], a[4*i+4]) for a[i] in open('test.txt'))
print(points)

# rule no.10 enumerate(generator) displaces range
print('=====rule no.10=====')
movie_list = ['Spotlight', 'La La Land', 'A Big Short', 'Fast Furious']
for i, item in enumerate(movie_list, 1):    # 1表示i开始之值，像字典一样处理数组
    print('No. ' + str(i) + ' movie is : ' + str(item))

# rule no.11 zip: turn two iterators to ONE generator
print('=====rule no.11=====')
director_list = ['T M', 'D C', 'A M', 'F G']
for movie,director in zip(movie_list, director_list):
    print(movie, " is directed by ", director)

# rule no.13 try/except/else/finally
print('=====rule no.13=====')
test_handld = open('test.txt')
try:
    data1 = test_handld.read()
    print(data1)
except UnicodeDecodeError:
    data = "None"
else:
    data = [int(x)**2 for x in data1 if not x == ' ']
finally:
    test_handld.close()
print(data)

# rule no.14 use exception in place of None

# rule no.15 closure nonlocal
print('=====rule no.15=====')
number = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
found = sort_priority3(number, group)   # in demo_function
print('Found:', found)
print(number)

# rule no.16 use generator(yield) to displace list if is the return of a function
print('=====rule no.16=====')
text = 'Four score and seven years ago...'
result = index_words(text)   # 比较奇怪的是为什么开头的F也算在内呢？？难道F前面有有个 ' ' ?...终于知道了，原来是手动加了一个0
print(result[:3])
result = list(index_words_iter(text))   # 将generator变成list
print(result[:3])   # same output
with open('rule16.txt', 'r') as f:
    it = index_file(f)  # 将generator直接转化为list会变成0，试过了
    result = list(it)
    print(result[:3])

# rule no.17
print('=====rule no.17=====')
result = norm([15, 35, 80])
print('result 1 :', result)
it = read_visits('rule17.txt')
result = norm_copy(it)
print('result 2 :', result)
visits = ReadVisits('rule17.txt')   # new iter
result = norm(visits)   # 这里要传给norm函数，而不是norm_copy，因为后者会复制一个list，导致内存占用较高。
#  可以直接传一个class进去是因为，传进去后会直接自动调用class.__iter__
print('result 3 :', result)

# rule no.18-no.21
print('=====rule no.18=====')

