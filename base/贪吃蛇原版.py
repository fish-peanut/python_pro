# 导入框架
import pygame
import random

# 设置大小长度
W = 800
H = 600
size = (W, H)

ROW = 30
COL = 40


# 定义要用的类（用来存坐标）
class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def copy(self):
        return Point(row=self.row, col=self.col)


# 定义要在哪里画
def rect(point, color):
    cell_width = W / COL
    cell_height = H / ROW
    left = point.col * cell_width
    top = point.row * cell_height
    pygame.draw.rect(window, color, (left, top, int(cell_width), int(cell_height)))


# pygame框架初始化
pygame.init()
pygame.display.set_caption('贪吃蛇')

clock = pygame.time.Clock()
window = pygame.display.set_mode(size)

# 定义蛇头
head = Point(row=0, col=0)
head_color = (0, 128, 128)
food = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
food_color = (255, 255, 0)


# 生成食物
def genfood():
    case = False
    food = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
    while not case:
        if food not in snakebody and food.row != head.row and food.col != head.col:
            case = True
        else:
            food = Point(row=random.randint(0, ROW - 1), col=random.randint(0, COL - 1))
    return food


# 定义蛇身
snakebody = []
snakecolor = (200, 200, 200)
direct = 'right'
# 计分
score = 0
# 游戏循环
quit = True
while quit:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 1073741906 or event.key == 119:
                if direct == 'left' or direct == 'right':
                    direct = 'up'
            elif event.key == 1073741905 or event.key == 115:
                if direct == 'left' or direct == 'right':
                    direct = 'down'
            elif event.key == 1073741904 or event.key == 97:
                if direct == 'up' or direct == 'down':
                    direct = 'left'
            elif event.key == 1073741903 or event.key == 100:
                if direct == 'up' or direct == 'down':
                    direct = 'right'
    # 处理身子
    snakebody.insert(0, head.copy())
    # 吃东西
    eat = (head.row == food.row and head.col == food.col)
    if eat:
        food = genfood()
        score += 1
    else:
        if len(snakebody) != 0:
            snakebody.pop()
    # 移动
    if direct == 'right':
        head.col += 1
    elif direct == 'left':
        head.col -= 1
    elif direct == 'up':
        head.row -= 1
    elif direct == 'down':
        head.row += 1
    # 设置死亡
    if head.col < 0 or head.col >= COL or head.row < 0 or head.row >= ROW:
        quit = False
    for snake in snakebody:
        if head.row == snake.row and head.col == snake.col:
            quit = False
    # 渲染画面
    pygame.draw.rect(window, (255, 255, 255), (0, 0, W, H))

    rect(head, head_color)
    for snake in snakebody:
        rect(snake, snakecolor)
    rect(food, food_color)
    # 交给计算机画
    pygame.display.update()

    # 设置帧率
    clock.tick(10)
else:
    print(f"你的分数是:{score},你好像有点菜啊QAQ")
