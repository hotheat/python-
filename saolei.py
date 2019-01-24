# 2017/10/24

import random
import turtle
from typing import List

saolei = {
    '0': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '1': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '0', '0', '0'],
        ['0', '0', '0', '1', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '2': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '3': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '4': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '1', '1', '1', '1', '1', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '5': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '6': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '7': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '8': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
    '9': [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '1', '0', '0', '0', '1', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '1', '0', '0'],
        ['0', '1', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ],
}

O = saolei.get('0')
one = saolei.get('1')
two = saolei.get('2')
three = saolei.get('3')
four = saolei.get('4')
five = saolei.get('5')
six = saolei.get('6')
seven = saolei.get('7')
eight = saolei.get('8')
nine = saolei.get('9')
num_list = [O, one, two, three, four, five, six, seven, eight, nine]


# 重新定义我们的 log 函数
def log(*args):
    print(*args)


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t._tracer(10000, 0.001)


def setpen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ====
# 测试
# 如果没有测试, 自行编写
# ====

# 定义我们用于测试的函数
# ensure 接受两个参数
# condition 是 bool, 如果为 False, 则输出 message
# 否则, 不做任何处理
def ensure(condition, message):
    # 在条件不成立的时候, 输出 message
    if not condition:
        log('*** 测试失败:', message)


a = [1, 2, 3, 1, 3, 5]


def unique(a: List) -> List:
    '''
    a 是一个 list
	返回一个 list, 包含了 a 中所有元素, 且不包含重复元素
    例如 a 是 [1, 2, 3, 1, 3, 5]
    返回 [1, 2, 3, 5]
    '''
    unique_ls = []
    for i in a:
        if i not in unique_ls:
            unique_ls.append(i)
        else:
            continue
    return unique_ls


def intersection(a: List, b: List) -> List:
    '''
    a b 都是 list
    返回一个 list, 里面的元素是同时出现在 a b 中的元素
    这个 list 中不包含重复元素
    '''
    intersect_ls = []
    for i in a:
        if i in b:
            intersect_ls.append(i)
    intersect_ls = unique(intersect_ls)
    return intersect_ls


def union(a: List, b: List) -> List:
    '''
    a b 都是 list
    返回一个 list, 里面的元素是所有出现在 a b 中的元素
    这个 list 中不包含重复元素
    '''
    c = a + b
    d = unique(c)
    return d


def difference(a: List, b: List) -> List:
    '''
    a b 都是 list
    返回一个 list, 里面的元素是
    所有在 a 中有 b 中没有的元素
    这个 list 中不包含重复元素
    '''
    diff_ls = []
    for i in a:
        if i not in b:
            diff_ls.append(i)
    return diff_ls


def difference_all(a: List, b: List) -> List:
    '''
    a b 都是 list
    返回一个 list, 里面的元素是
    所有在 a b 中的非公共元素
    这个 list 中不包含重复元素
    '''
    diff_a = difference(a, b)
    diff_b = difference(b, a)
    return diff_a + diff_b


def issubset(a: List, b: List) -> bool:
    '''
    a b 都是 list

	检查是否 a 中的每个元素都在 b 中出现
    返回 bool

    :return: bool
    '''
    for i in a:
        if i in b:
            continue
        else:
            return False
    return True


# 扫雷代码
def rect(x, y, color, size):
    setpen(x, y)
    t.pencolor('#FAEBD7')
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()


def draw_pixel(x, y, pixel, size=3):
    '''
    pixel 是一个 像素值
    像素值是只有一个字符的 str
    如果是 '0' 则画一个白色否则画黑色
	以坐标 x y 为矩形左上角顶点画一个边长为 size 的正方形
    '''
    setpen(x, y)
    if pixel == '0':
        color = 'white'
    else:
        color = '#CD5C5C'
    rect(x, y, color, size)


def draw_line(x, y, pixels, size=3):
    '''
    pixels 是一个包含了像素值的 list
	以坐标 x y 为左上角顶点画一排边长为 size 的正方形
    '''
    setpen(x, y)
    for i in range(len(pixels)):
        offset_x = x + i * size
        offset_y = y
        pixel = pixels[i]
        draw_pixel(offset_x, offset_y, pixel, size=size)


block = [
    ['0', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '1', '1', '1', '0'],

]


def draw_block(x, y, block, size=3):
    '''
    block 是一个包含了 pixels list 的 list
	(也就是一个像素方阵)
	以坐标 x y 为左上角顶点画一个边长为 size 的正方形方阵
    '''
    setpen(x, y)
    for i in range(len(block)):
        offset_x = x
        offset_y = y - size * i
        draw_line(offset_x, offset_y, block[i], size=size)


#
line = [
    block,
    block,
    block,
    block,
]


def draw_block_line(x, y, line, size=3):
    '''
    line 是一个包含了上面 block 元素的 list
    block 的宽度是 size * number_of_pixels (这个不懂就留言问)
    x y 是左上角顶点坐标
    '''
    num_pixels = len(line[0][0])
    log('num pixels', num_pixels)
    setpen(x, y)
    for i in range(len(line)):
        offset_x = x + i * size * num_pixels
        offset_y = y
        draw_block(offset_x, offset_y, line[i], size=size)


map = [
    line,
    line,
    line,
    line,
    line,
]


def draw_block_map(x, y, map, size=3):
    '''
    map 是一个包含了 line 元素的 list
    line 是一个包含了上面 block 元素的 list
    map 的高是 block_size * number_of_pixels (这个不懂就留言问)
    x y 是左上角顶点坐标

    :return: None
    '''
    num_pixels = len(line[0][0])
    setpen(x, y)
    for i in range(len(map)):
        offset_x = x
        offset_y = y - i * size * (num_pixels + 2)
        draw_block_line(offset_x, offset_y, map[i], size=size)


# 画扫雷地图
# 利用 marked_square 生成的 list
# square = [
#     [1, 2, 9, 2, 9],
#     [1, 9, 2, 2, 2],
#     [1, 2, 2, 2, 9],
#     [1, 2, 9, 2, 1],
#     [9, 2, 1, 1, 0],
# ]


def draw_mine_map(x, y, map):
    '''
    x y 是地图左上角坐标

    map 是一个 marked_square 生成的 list(如上 square 所示)
    使用之前的函数画出这个地图
    注意: 0 - 8 的字符图案都存在一个 dict 中, 你要定义好
    字符图案最好是 10 * 10 或者 15 * 15, 总之工整一点且必须是正矩形
    '''
    map_block = map[:]
    for i, row in enumerate(map):
        for j in range(len(row)):
            char = row[j]
            map_block[i][j] = num_list[char]
    draw_block_map(x, y, map_block)


# 直接使用 square 来调用画地图函数
square = [
    [1, 2, 9, 2, 9],
    [1, 9, 2, 2, 2],
    [1, 2, 2, 2, 9],
    [1, 2, 9, 2, 1],
    [9, 2, 1, 1, 0],
]


def rect_touched(x, y, w, h, point):
    '''
    x y 是一个矩形的左上角坐标
    w h 是矩形的长宽
    point 是一个包含了一对坐标的 tuple
    例如(1, 2)

    检查 point 是否在矩形中, 并返回

    :return: bool
    '''
    offset_x = x + w
    offset_y = y - h

    if (x < point[0] < offset_x) and (offset_y < point[1] < y):
        return True
    else:
        return False


# 检测点击的索引下标
# 利用 click 事件监听机制来判断
# 你点击的坐标在 map 中的索引下标
# http://vip.cocode.cc/chest/shared/165
def touched_index(x, y, x_rect=100, y_rect=100):
    '''
    x y 是鼠标点击的屏幕坐标
    根据作业 8.12, draw_mine_map 画了一个地图
    地图的左上角坐标已知
    地图的每个方格尺寸已知
    返回 (index_x, index_y)
    :return: 包含了索引下标的 tuple
    '''
    n = 7
    size = 3
    block_width = n * size
    index_x = int((x - x_rect) // block_width)
    index_y = int((y_rect - y) // block_width)
    return (index_x, index_y)


'''
touched_index
假设 map 是 5 * 5 的格子
左上角坐标是 100, 100
每个格子的长宽是 20 像素
当你点击到 150, 90 的时候
返回的索引应该是 (2, 0)
'''


def random_square_09(n, limit=3):
    '''
    返回以下格式的数据
    只包含 0 和 9
    limit 是 9 的个数
    假设 n 为 4, 返回的数据格式如下(这是格式范例, 真实数据是随机的)
    注意, 这只是一个 list, 并不是它显示的样子
    注意, 这是一个 list 不是 str
    [
        [0, 9, 0, 0],
        [0, 0, 9, 0],
        [9, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    :param n: int
    :return: 包含了 n 个『只包含 n 个「随机 0 9」的 list』的 list, 9 的个数是 limit
    '''
    square_09 = []
    for i in range(n):
        line_09 = []
        square_09.append(line_09)
        for j in range(n):
            line_09.append(0)
    r_c_list = []
    i = 0
    while i < limit:
        r = random.randint(0, n - 1)
        c = random.randint(0, n - 1)
        if (r, c) not in r_c_list:
            square_09[r][c] = 9
            r_c_list.append((r, c))
            i += 1
    return square_09


def add_square(i, j, square_table):
    loc = [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1), (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
    ]
    for k in loc:
        x = k[0]
        y = k[1]
        if square_table[x][y] != 9:
            square_table[x][y] += 1


def marked_square(array):
    '''
    array 是一个「包含了『只包含了 0 9 的 list』的 list」
    返回一个标记过的 list
    ** 注意, 使用一个新数组来存储结果, 不要直接修改老数组

    范例如下, 这是 array
    [
        [0, 9, 0, 0],
        [0, 0, 9, 0],
        [9, 0, 9, 0],
        [0, 9, 0, 0],
    ]

    这是标记后的结果
    [
        [1, 9, 2, 1],
        [2, 4, 9, 2],
        [9, 4, 9, 2],
        [2, 9, 2, 1],
    ]

    规则是, 0 会被设置为四周 8 个元素中 9 的数量

    :param array: list
    :return: 标记后的 array
    '''
    # 生成行列各加 1 的新列表矩阵
    array_cp = []
    columns = len(array[0])
    rows = len(array)
    array_cp.append([0] * (columns + 2))
    for i in array:
        array_cp.append([0] + i + [0])
    array_cp.append([0] * (columns + 2))
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if array_cp[i][j] == 9:
                add_square(i, j, array_cp)

    new_square_add = []
    for k in range(1, (len(array_cp) - 1)):
        new_square_add.append(array_cp[k][1:-1])
    return new_square_add


# 课 9.1
# 本作业基于上次的作业
def draw_label(x, y, text):
    '''
    text 是一个字符串
    以 x y 为左上角坐标画出这个字符串
    字符串中如果存在没有字符图形的字符
    就用一个特殊的字符替代(所以你需要造一个特殊的字符)
    '''
    setpen(x, y)
    t.write(text, font=("Times", 18, "bold"))


# 基于作业 8, 完成完整版的扫雷, 功能如下
# 程序初始状态, 所有格子都是空白
# 用户点击格子后, 检查点击的是什么
# 如果是雷, 则显示所有雷, 并使用 9.1 显示结束语(随便你怎么来)
# 如果是数字或者空白, 则显示这个数字或者空白
# 如果是空白, 不要求像其他扫雷那样显示附近所有空白和数字

def blank_block(n):
    block = []
    for i in range(n):
        line_block = '1' * n
        block.append(line_block)
    return block


def blank(x, y, n, land_mine):
    block = blank_block(n)
    size = 3
    draw_block(x, y, block, size=size * 7)
    square_09 = random_square_09(n, limit=land_mine)
    new_square_09 = marked_square(square_09)
    return new_square_09


x0, y0 = 0, 0
n = input('请输入 n, 生成 n * n 地图：')
n = int(n)
land_mine = int(input('请输入雷数：'))
assert land_mine <= n ** 2, '输入雷数应小于 {} 的平方'.format(str(n))
new_square = blank(x0, y0, n, land_mine)


def click_start(*args):
    x, y = args
    index_tuple = touched_index(x, y, x_rect=x0, y_rect=y0)
    if 0 <= index_tuple[0] < n and 0 <= index_tuple[1] < n:
        block_num = new_square[index_tuple[0]][index_tuple[1]]
        block = num_list[block_num]
        block_num = str(block_num)
        log('block number', block_num)
        if block_num != '9':
            offset_x = x0 + 7 * 3 * index_tuple[0]
            offset_y = y0 - 7 * 3 * index_tuple[1]
            draw_block(offset_x, offset_y, block, size=3)
        else:
            draw_mine_map(x0, y0, new_square)
            offset_x = x0
            offset_y = y0 + 7 * 3
            t.pencolor('red')
            draw_label(offset_x, offset_y, 'Game Over')


if __name__ == '__main__':
    turtle.onscreenclick(click_start)
    turtle.update()
    turtle.done()
