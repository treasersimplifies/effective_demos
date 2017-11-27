# rule no.15
def sort_priority3(number, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            return (0, x)
        return (1 , x)
    number.sort(key=helper)
    return found

# rule no.16


# bad one:
def index_words(text):
    result = []
    if text:
        result.append(0)    # 手动添加0，所以首单词也能被识别
    for index,letter in enumerate(text):    #将一段字符串变成生成器
        if letter == ' ':   # ???
            result.append(index+1)
    return result


# good one (the same sense as the former):
def index_words_iter(text):
    if text:
        yield 0
    for index,letter in enumerate(text):
        if letter == ' ':
            yield index + 1
# 这个函数返回的是一个generator。


# another good one:
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset
# 这个函数返回的是也一个generator。

# rule no.17


def norm(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def norm_copy(numbers):
    numbers = list(numbers)   # 关键的一句，因为传进来的numbers会是一个迭代器，因此不能直接使用，而应该转化为列表。
    # 但是这样一来又是提高不了效率（占用过多内存）了。。。。最好的解决办法是定义一个容器类, see also in demo_classes.py
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)
