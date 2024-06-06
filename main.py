import pygame
import random
import time
import json
WIDTH = 1000
HEIGHT = 850
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
blue_top = (83, 62, 171)
blue_soft = (57, 20, 175)
orangebg = (232, 210, 102)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
goodYellow = (255, 211, 0)
DARK_BLUE = (0, 0, 100)
Light_green = (0, 255, 0)
title_rect_color = (166, 146, 88)
light_blue = (73, 140, 182)
grey = (169, 169, 169)
button_blue = (72, 117, 183)
orange_button = (209, 150, 46)
greenShowdown = (84, 171, 122)

day_gift_coin = ['coin', 'coin_strong', 'gems']
skins_all_shop = ['spik_sakura', 'poco_pirate']
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brawlik")

clock = pygame.time.Clock()
myFileW = open("notes_data.json", mode='w', encoding='utf-8')
icon = pygame.image.load('icon.ico')
pygame.display.set_icon(icon)
bg_default = pygame.image.load('otherModels/bg1.png')
bg_2 = pygame.image.load('otherModels/bg2.png')
heart = pygame.image.load('otherModels/heard.png')
spikImage = pygame.image.load('brawlers/spik.png')
spik_sakura = pygame.image.load('skins/spik_sakura.png')
edgarImage = pygame.image.load('brawlers/edgar.png')
bit_8Image = pygame.image.load('brawlers/8_bit.png')
crowImage = pygame.image.load('brawlers/crow.png')
frenkImage = pygame.image.load('brawlers/frenk.png')
geylImage = pygame.image.load('brawlers/geyl.png')
leonImage = pygame.image.load('brawlers/leon.png')
mrs_piImage = pygame.image.load('brawlers/Msr_Pi.png')
pocoImage = pygame.image.load('brawlers/poco.png')
poco_pirateSkin = pygame.image.load('skins/poco_pirate.png')
stuImage = pygame.image.load('brawlers/stu.png')
surgeImage = pygame.image.load('brawlers/Surge.png')
box_image = pygame.image.load('otherModels/box.png')
big_box_image = pygame.image.load('otherModels/big_box.png')
mega_box_image = pygame.image.load('otherModels/mega_box.png')
spik_bs = spikImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
edgar_bs = edgarImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
bit_8_bs = bit_8Image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
crowI_bs = crowImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
frenk_bs = frenkImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
geyl_bs = geylImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
leon_bs = leonImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
mrs_pi_bs = mrs_piImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
poco_bs = pocoImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
stu_bs = stuImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
surge_bs = surgeImage.get_rect(center=(WIDTH // 2, HEIGHT // 2))
box_bs = box_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
big_box_bs = big_box_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
mega_box_bs = mega_box_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
boolet = pygame.image.load('otherModels/boolet.png')
map = pygame.image.load('otherModels/Map.png')
coin_strong_image = pygame.image.load('otherModels/coin_strong.png')
gems_image = pygame.image.load('otherModels/gems.png')
coin_image = pygame.image.load('otherModels/coin.png')
search_bg = pygame.image.load('otherModels/search-BS.jpg')
showdown = pygame.image.load('otherModels/showdown.png')
banka = pygame.image.load('otherModels/banka.png')
win = pygame.image.load('otherModels/win.png')
lose = pygame.image.load('otherModels/lose.png')
gerchSmall = pygame.image.load('otherModels/gerch.png')
gerchBig = pygame.image.load('otherModels/gerchBig.png')
warn1 = pygame.image.load('otherModels/warn1.png')
warn2 = pygame.image.load('otherModels/warn2.png')
warn3 = pygame.image.load('otherModels/warn3.png')
warn4 = pygame.image.load('otherModels/warn4.png')
zone = pygame.image.load('otherModels/zone.png')
meteor = pygame.image.load('otherModels/meteor.png')
search_bg = pygame.transform.scale(search_bg, (WIDTH, HEIGHT))

map = pygame.transform.scale(map, (1200, 1200))
bg_2 = pygame.transform.scale(bg_2, (WIDTH, HEIGHT))
sound1 = pygame.mixer.Sound("music_bs1.mp3")
sound2 = pygame.mixer.Sound("music_bs2.mp3")
sound3 = pygame.mixer.Sound("music_bs3.mp3")
sound4 = pygame.mixer.Sound("music_bs4.mp3")
search_sound = pygame.mixer.Sound('laser_load_01.mp3')
sound_onGame = pygame.mixer.Sound('slugfest-2.mp3')


def write(data, filename):
    dates = json.dumps(data)
    dates = json.loads(str(dates))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dates, file, indent=2)


def read(filename):
    with open(filename, 'r') as j:
        json_data = json.load(j)
        return json_data


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None, borders=0):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
        self.borderRadius = borders

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(screen, self.fill_color, self.rect, border_radius=self.borderRadius)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(screen, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


####################################################################
class Label(Area):
    def outline(self, frame_color, thickness):
        pygame.draw.rect(screen, frame_color, self.rect, thickness)

    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Brawler():
    def __init__(self, photo, rect, health, speed):
        self.photo = photo
        self.health = health
        self.speed = speed
        self.rect = rect

    def find_health(self):
        return self.health

    def find_speed(self):
        return self.speed

    def find_brawler(self):
        return self.photo

    def find_rect(self):
        return self.rect


class Skin_Brawler(Brawler):
    def __init__(self, skin, rect, health, speed):
        self.health = health
        self.speed = speed
        self.rect = rect
        self.skin = skin

    def find_skin(self):
        return self.skin


def box(bg, gem, count):
    if listB['currency'][gem] >= count:

        if bg == 1:
            screen.blit(bg_default, (0, 0))
        elif bg == 2:
            screen.blit(bg_2, (0, 0))
        rand_box = random.choices(['coin', 'coin_strong', 'gems', 'brawlers'], weights=[50, 35, 13, 2], k=2)
        win = {}
        for i in range(2):
            if rand_box[i] == 'coin':
                rand_count = random.randrange(10, 200)
                listB['currency']['coin'] += rand_count
                win[i] = f'Coins: {rand_count}'
            elif rand_box[i] == 'coin_strong':
                rand_count = random.randrange(5, 100)
                listB['currency']['coin_strong'] += rand_count
                win[i] = f'Coins_strong: {rand_count}'
            elif rand_box[i] == 'gems':
                rand_count = random.randrange(5, 25)
                listB['currency']['gems'] += rand_count
                win[i] = f'Gems: {rand_count}'
            elif rand_box[i] == 'brawlers':
                locked_brawlers = []
                rare = 0
                epik = 0
                legen = 0
                print(len(locked_brawlers))
                if listB['brawlers']['poco']['unlock'] != True:
                    locked_brawlers.append('poco')
                    rare += 1
                if listB['brawlers']['stu']['unlock'] != True:
                    locked_brawlers.append('stu')
                    rare += 1
                if listB['brawlers']['mrs_pi']['unlock'] != True:
                    locked_brawlers.append('mrs_pi')
                    rare += 1

                if listB['brawlers']['serge']['unlock'] != True:
                    locked_brawlers.append('serge')
                    epik += 1
                if listB['brawlers']['geyl']['unlock'] != True:
                    locked_brawlers.append('geyl')
                    epik += 1
                if listB['brawlers']['edgar']['unlock'] != True:
                    locked_brawlers.append('edgar')
                    epik += 1
                if listB['brawlers']['frenk']['unlock'] != True:
                    locked_brawlers.append('frenk')
                    epik += 1

                if listB['brawlers']['8_bit']['unlock'] != True:
                    locked_brawlers.append('8_bit')
                    legen += 1
                if listB['brawlers']['crow']['unlock'] != True:
                    locked_brawlers.append('crow')
                    legen += 1
                if listB['brawlers']['leon']['unlock'] != True:
                    locked_brawlers.append('leon')
                    legen += 1
                if listB['brawlers']['spik']['unlock'] != True:
                    locked_brawlers.append('spik')
                    legen += 1

                if len(locked_brawlers) == 0:
                    win[i] = f'Compensation: 30 gems'
                    listB['currency']['gems'] += 30
                else:
                    weightsBraw = []
                    if rare != 0:
                        if rare >= 1:
                            weightsBraw.append(20)
                            if rare >= 2:
                                weightsBraw.append(20)
                                if rare == 3:
                                    weightsBraw.append(20)
                    if epik != 0:
                        if epik >= 1:
                            weightsBraw.append(10)
                            if epik >= 2:
                                weightsBraw.append(10)
                                if epik >= 3:
                                    weightsBraw.append(10)
                                    if epik == 4:
                                        weightsBraw.append(10)

                    if legen != 0:
                        if legen >= 1:
                            weightsBraw.append(3)
                            if legen >= 2:
                                weightsBraw.append(3)
                                if legen >= 3:
                                    weightsBraw.append(3)
                                    if legen == 4:
                                        weightsBraw.append(3)

                    print(locked_brawlers, '         ', weightsBraw)
                    print(i)
                    rand_brawler = random.choices(locked_brawlers, weights=weightsBraw, k=1)[0]
                    listB['brawlers'][rand_brawler]['unlock'] = True
                    win[i] = f'Brawler: {rand_brawler}'
        button1 = Label(200, 200, 250, 100, title_rect_color)
        button1.set_text(win[0], 25, WHITE)
        button1.draw(10, 7)
        button2 = Label(200 + 300, 200, 250, 100, title_rect_color)
        button2.set_text(win[1], 25, WHITE)
        button2.draw(10, 7)
        listB['currency'][gem] -= count
        print(listB['currency']['gem_box'])
        running = True
        while running:
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    running = False
                    scene_main(1, bg)
                elif event.type == pygame.QUIT:
                    running = False
                    write(listB, 'tests.json')
            clock.tick(FPS)
            pygame.display.update()
    else:
        scene_main(1, bg)


def big_box(bg):
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    rand_box = random.choices(['coin', 'coin_strong', 'gems', 'brawlers'], weights=[50, 35, 13, 2], k=3)
    win = {}
    for i in range(3):
        if rand_box[i] == 'coin':
            rand_count = random.randrange(10, 200)
            listB['currency']['coin'] += rand_count
            win[i] = f'Coins: {rand_count}'
        elif rand_box[i] == 'coin_strong':
            rand_count = random.randrange(5, 100)
            listB['currency']['coin_strong'] += rand_count
            win[i] = f'Coins_strong: {rand_count}'
        elif rand_box[i] == 'gems':
            rand_count = random.randrange(5, 25)
            listB['currency']['gems'] += rand_count
            win[i] = f'Gems: {rand_count}'
        elif rand_box[i] == 'brawlers':
            locked_brawlers = []
            rare = 0
            epik = 0
            legen = 0
            print(len(locked_brawlers))
            if listB['brawlers']['poco']['unlock'] != True:
                locked_brawlers.append('poco')
                rare += 1
            if listB['brawlers']['stu']['unlock'] != True:
                locked_brawlers.append('stu')
                rare += 1
            if listB['brawlers']['mrs_pi']['unlock'] != True:
                locked_brawlers.append('mrs_pi')
                rare += 1

            if listB['brawlers']['serge']['unlock'] != True:
                locked_brawlers.append('serge')
                epik += 1
            if listB['brawlers']['geyl']['unlock'] != True:
                locked_brawlers.append('geyl')
                epik += 1
            if listB['brawlers']['edgar']['unlock'] != True:
                locked_brawlers.append('edgar')
                epik += 1
            if listB['brawlers']['frenk']['unlock'] != True:
                locked_brawlers.append('frenk')
                epik += 1

            if listB['brawlers']['8_bit']['unlock'] != True:
                locked_brawlers.append('8_bit')
                legen += 1
            if listB['brawlers']['crow']['unlock'] != True:
                locked_brawlers.append('crow')
                legen += 1
            if listB['brawlers']['leon']['unlock'] != True:
                locked_brawlers.append('leon')
                legen += 1
            if listB['brawlers']['spik']['unlock'] != True:
                locked_brawlers.append('spik')
                legen += 1

            if len(locked_brawlers) == 0:
                win[i] = f'Compensation: 30 gems'
                listB['currency']['gems'] += 30
            else:
                weightsBraw = []
                if rare != 0:
                    if rare >= 1:
                        weightsBraw.append(20)
                        if rare >= 2:
                            weightsBraw.append(20)
                            if rare == 3:
                                weightsBraw.append(20)
                if epik != 0:
                    if epik >= 1:
                        weightsBraw.append(10)
                        if epik >= 2:
                            weightsBraw.append(10)
                            if epik >= 3:
                                weightsBraw.append(10)
                                if epik == 4:
                                    weightsBraw.append(10)

                if legen != 0:
                    if legen >= 1:
                        weightsBraw.append(3)
                        if legen >= 2:
                            weightsBraw.append(3)
                            if legen >= 3:
                                weightsBraw.append(3)
                                if legen == 4:
                                    weightsBraw.append(3)

                print(locked_brawlers, '         ', weightsBraw)
                print(i)
                rand_brawler = random.choices(locked_brawlers, weights=weightsBraw, k=1)[0]
                listB['brawlers'][rand_brawler]['unlock'] = True
                win[i] = f'Brawler: {rand_brawler}'
    button1 = Label(200, 200, 250, 100, title_rect_color)
    button1.set_text(win[0], 25, WHITE)
    button1.draw(10, 7)
    button2 = Label(200 + 300, 200, 250, 100, title_rect_color)
    button2.set_text(win[1], 25, WHITE)
    button2.draw(10, 7)
    button3 = Label(350, 450, 250, 100, title_rect_color)
    button3.set_text(win[2], 25, WHITE)
    button3.draw(10, 7)
    listB['currency']['gems'] -= 60
    running = True
    while running:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                running = False
                scene_main(1, bg)
            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def mega_box(bg):
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    rand_box = random.choices(['coin', 'coin_strong', 'gems', 'brawlers'], weights=[50, 35, 13, 2], k=5)
    win = {}
    print('ddddd ')
    for i in range(5):
        if rand_box[i] == 'coin':
            rand_count = random.randrange(10, 200)
            listB['currency']['coin'] += rand_count
            win[i] = f'Coins: {rand_count}'
        elif rand_box[i] == 'coin_strong':
            rand_count = random.randrange(5, 100)
            listB['currency']['coin_strong'] += rand_count
            win[i] = f'Coins_strong: {rand_count}'
        elif rand_box[i] == 'gems':
            rand_count = random.randrange(5, 25)
            listB['currency']['gems'] += rand_count
            win[i] = f'Gems: {rand_count}'
        elif rand_box[i] == 'brawlers':
            locked_brawlers = []
            rare = 0
            epik = 0
            legen = 0
            print(len(locked_brawlers))
            if listB['brawlers']['poco']['unlock'] != True:
                locked_brawlers.append('poco')
                rare += 1
            if listB['brawlers']['stu']['unlock'] != True:
                locked_brawlers.append('stu')
                rare += 1
            if listB['brawlers']['mrs_pi']['unlock'] != True:
                locked_brawlers.append('mrs_pi')
                rare += 1

            if listB['brawlers']['serge']['unlock'] != True:
                locked_brawlers.append('serge')
                epik += 1
            if listB['brawlers']['geyl']['unlock'] != True:
                locked_brawlers.append('geyl')
                epik += 1
            if listB['brawlers']['edgar']['unlock'] != True:
                locked_brawlers.append('edgar')
                epik += 1
            if listB['brawlers']['frenk']['unlock'] != True:
                locked_brawlers.append('frenk')
                epik += 1

            if listB['brawlers']['8_bit']['unlock'] != True:
                locked_brawlers.append('8_bit')
                legen += 1
            if listB['brawlers']['crow']['unlock'] != True:
                locked_brawlers.append('crow')
                legen += 1
            if listB['brawlers']['leon']['unlock'] != True:
                locked_brawlers.append('leon')
                legen += 1
            if listB['brawlers']['spik']['unlock'] != True:
                locked_brawlers.append('spik')
                legen += 1

            if len(locked_brawlers) == 0:
                win[i] = f'Compensation: 30 gems'
                listB['currency']['gems'] += 30
            else:
                weightsBraw = []
                if rare != 0:
                    if rare >= 1:
                        weightsBraw.append(20)
                        if rare >= 2:
                            weightsBraw.append(20)
                            if rare == 3:
                                weightsBraw.append(20)
                if epik != 0:
                    if epik >= 1:
                        weightsBraw.append(10)
                        if epik >= 2:
                            weightsBraw.append(10)
                            if epik >= 3:
                                weightsBraw.append(10)
                                if epik == 4:
                                    weightsBraw.append(10)

                if legen != 0:
                    if legen >= 1:
                        weightsBraw.append(3)
                        if legen >= 2:
                            weightsBraw.append(3)
                            if legen >= 3:
                                weightsBraw.append(3)
                                if legen == 4:
                                    weightsBraw.append(3)

                print(locked_brawlers, '         ', weightsBraw)
                print(i)
                rand_brawler = random.choices(locked_brawlers, weights=weightsBraw, k=1)[0]
                listB['brawlers'][rand_brawler]['unlock'] = True
                win[i] = f'Brawler: {rand_brawler}'
    button1 = Label(200, 200, 250, 100, title_rect_color)
    button1.set_text(win[0], 25, WHITE)
    button1.draw(10, 7)
    button2 = Label(200 + 300, 200, 250, 100, title_rect_color)
    button2.set_text(win[1], 25, WHITE)
    button2.draw(10, 7)
    button3 = Label(100, 450, 250, 100, title_rect_color)
    button3.set_text(win[2], 25, WHITE)
    button3.draw(10, 7)
    button4 = Label(400, 450, 250, 100, title_rect_color)
    button4.set_text(win[3], 25, WHITE)
    button4.draw(10, 7)
    button5 = Label(700, 450, 250, 100, title_rect_color)
    button5.set_text(win[4], 25, WHITE)
    button5.draw(10, 7)
    listB['currency']['gems'] -= 80
    running = True
    while running:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                running = False
                scene_main(1, bg)
            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


time_now = int(time.time())
listB = {
    'trophies': 0,
    'brawlers': {
        'spik': {
            'unlock': None,
            'skins': {
                'spik_sakura': None,

            },
            'gerch': None

        },
        '8_bit': {
            'unlock': None,
            'skins': None,
            'gerch': None
        },
        'crow': {
            'unlock': None,
            'skins': None,
            'gerch': None
        },
        'edgar': {
            'unlock': None,
            'skins': None,
            'gerch': None
        },
        'frenk': {
            'unlock': None,
            'skins': None,
            'gerch': None
        },
        'geyl': {
            'unlock': None,
            'skins': None,
            'gerch': None
        },
        'leon': {
            'unlock': None,
            'skins': None,
            'gerch': None
        },
        'poco': {
            'unlock': True,
            'skins': {
                'poco_pirate': None
            },
            'gerch': None
        },
        'stu': {
            'unlock': None,
            'skins': None,
            'gerch': None
        },
        'serge': {
            'unlock': None,
            'skins': None,
            'gerch': None
        },
        'mrs_pi': {
            'unlock': None,
            'skins': None,
            'gerch': None
        }
    },
    'currency': {
        'coin': 0,
        'coin_strong': 0,
        'gems': 0,
        'gem_box': 0,
        'gem_bigbox': 0
    },
    'gift_day': {
        "time_click": 0,
        'time_gift': 0,
        'time_next_gift': 0,
        'item_gift': None,
        'amount_gift': None
    },
    'buy_shop': {
        "buy1": "coin",
        "buy1num": 200,
        "click1": 0,
        "buy2": "coin",
        "buy2num": 200,
        "click2": 0,
        "buy3": "coin",
        "buy3num": 200,
        "click3": 0,
        "buy4": "coin",
        "buy4num": 200,
        "click4": 0
    },
    "skins_shop": {
        "skins_1": None,
        "skins_2": None,
        "next_skins": 0
    }
}
if listB != read('tests.json'):
    listB = read('tests.json')

skins_shop = []

if listB['brawlers']['poco']['unlock'] == True:
    if listB['brawlers']['poco']['skins']["poco_pirate"] != True:
        skins_shop.append("poco_pirate")

if listB['brawlers']['spik']['unlock'] == True:
    if listB['brawlers']['spik']['skins']['spik_sakura'] != True:
        skins_shop.append("spik_sakura")


spik = Brawler(spikImage, spik_bs, 3, 12)
sakura_spik_skin = Skin_Brawler(spik_sakura, spik_bs, spik.find_health(), spik.find_speed())
bit_8 = Brawler(bit_8Image, bit_8_bs, 5, 5)
edgar = Brawler(edgarImage, edgar_bs, 2, 14)
frenk = Brawler(frenkImage, frenk_bs, 4, 9)
geyl = Brawler(geylImage, geyl_bs, 3, 10)
leon = Brawler(leonImage, leon_bs, 3, 14)
mrs_pi = Brawler(mrs_piImage, mrs_pi_bs, 3, 12)
poco = Brawler(pocoImage, poco_bs, 3, 11)
stu = Brawler(stuImage, stu_bs, 1, 16)
surge = Brawler(surgeImage, surge_bs, 3, 13)
crow = Brawler(crowImage, crowI_bs, 2, 15)
poco_pirate_skin = Skin_Brawler(poco_pirateSkin, poco_bs, poco.find_health(), poco.find_speed())

brawlernow = poco


# Цикл игры
def scene_main(run, bg):
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))

    running = True
    if run == 0:
        sound2.play(100)
        run += 1
    try:
        screen.blit(brawlernow.find_brawler(), (450, 325))
    except:
        screen.blit(brawlernow.find_skin(), (450, 325))

    while running:
        title_text = Label(25, 50, 100, 35, title_rect_color, 5)
        title_text.set_text(' Brawlik', 20, WHITE)
        title_text.draw(7, 5)

        trophies = Label(150, 50, 300, 60, light_blue, 10)
        trophies.set_text('Trophies: ' + str(listB['trophies']), 25, WHITE)
        trophies.draw(25, 12)

        button_go = Label(750, 700, 200, 75, orange_button, 10)
        button_go.set_text('Play', 40, WHITE)
        button_go.draw(60, 10)

        gems_box = str(listB['currency']["gem_box"]) + '/500'
        button_box = Label(50, 700, 200, 75, light_blue, 10)
        button_box.set_text('Box', 40, WHITE)
        button_box.draw(80, 0)
        screen.blit(box_image, (60, 710))

        mode = Label(340, 700, 340, 75, greenShowdown, 10)
        mode.set_text('Showdown', 20, WHITE)
        mode.draw(125, 3)
        screen.blit(showdown, (350, 720))

        button_box_text = Label(140, 700, 0, 0, title_rect_color)
        button_box_text.set_text(gems_box, 13, WHITE)
        button_box_text.draw(40, 50)

        edit_music_button = Label(50, 350, 175, 40, button_blue, 10)
        edit_music_button.set_text('Edit music', 20, WHITE)
        edit_music_button.draw(35, 7)

        edit_bg_button = Label(50, 300, 175, 40, button_blue, 10)
        edit_bg_button.set_text('Edit background', 20, WHITE)
        edit_bg_button.draw(5, 7)

        shop_button = Label(775, 300, 175, 40, button_blue, 10)
        shop_button.set_text('Shop', 20, WHITE)
        shop_button.draw(60, 7)

        brawler_button = Label(775, 350, 175, 40, button_blue, 10)
        brawler_button.set_text('Brawlers', 20, WHITE)
        brawler_button.draw(45, 7)

        screen.blit(coin_image, (460, 50))
        coin_counter = Label(530, 62, 90, 40, (0, 0, 0), 10)
        coin_counter.set_text(' '+str(listB['currency']['coin']), 20, WHITE)
        coin_counter.draw(0, 5)

        screen.blit(coin_strong_image, (635, 50))
        coin_strong_counter = Label(705, 62, 90, 40, (0, 0, 0), 10)
        coin_strong_counter.set_text(' ' + str(listB['currency']['coin_strong']), 20, WHITE)
        coin_strong_counter.draw(0, 5)

        screen.blit(gems_image, (810, 50))
        gems_counter = Label(880, 62, 90, 40, (0, 0, 0), 10)
        gems_counter.set_text(' ' + str(listB['currency']['gems']), 20, WHITE)
        gems_counter.draw(0, 5)

        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # музыка
                if edit_music_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    scene_music(bg)
                # фон
                elif edit_bg_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    scene_bg(bg)
                # магазин
                elif shop_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    shop_page1(bg)
                # бокс
                elif button_box.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    box(bg, 'gem_box', 500)
                # кнопка play
                elif button_go.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    scene_game_hotZone(brawlernow)
                # выбор персов
                elif brawler_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    brawlermenu(bg)
                else:
                    print('не попал')
            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def brawlerPrew(bg, brawler):
    global brawlernow
    rareColor = (76, 111, 179)
    epikColor = (142, 45, 210)
    legenColor = (240, 189, 15)
    rareBrawler = ''
    a = {'poco': poco, 'stu': stu, 'mrs_pi': mrs_pi, 'serge': surge, 'geyl': geyl, 'edgar': edgar, 'frenk': frenk,
         '8_bit': bit_8, 'crow': crow, 'leon': leon, 'spik': spik}
    b = {'poco': rareColor, 'stu': rareColor, 'mrs_pi': rareColor,
         'serge': epikColor, 'geyl': epikColor, 'edgar': epikColor, 'frenk': epikColor,
         '8_bit': legenColor, 'crow': legenColor, 'leon': legenColor, 'spik': legenColor}
    skins = {'spik_sakura_skin': sakura_spik_skin,

             'poco_pirate_skin': poco_pirate_skin}
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    textInfo = [f"Brawler's Health: {a[brawler].find_health()}",
                f"Brawler's Speed: {a[brawler].find_speed()}"]
    if b[brawler] == rareColor:
        rareBrawler = 'Rare'
    elif b[brawler] == epikColor:
        rareBrawler = "Epic"
    elif b[brawler] == legenColor:
        rareBrawler = "Legendary"

    title_text = Label(40, 60, 300, 100, b[brawler], 5)
    title_text.set_text(brawler, 20, WHITE)
    title_text.draw(150, 50)
    Rare = Label(65, 75, 0, 0, b[brawler], 5)
    Rare.set_text(rareBrawler, 20, WHITE)
    Rare.draw(0, 0)
    info = Label(600, 230, 300, 400, button_blue, 5)
    info.set_text(textInfo[0], 20, WHITE)
    info.draw(50, 20)
    info1 = Label(600, 280, 0, 0, button_blue, 5)
    info1.set_text(textInfo[1], 20, WHITE)
    info1.draw(50, 20)
    screen.blit(a[brawler].find_brawler(), (400, 325))
    try:

        brawlerses = []
        for i in listB['brawlers'][brawler]['skins']:

            b = listB['brawlers'][brawler]['skins'][i]
            if b:
                brawlerses.append(i)
        if len(brawlerses) == 0:
            back = Label(10, 10, 40, 40, title_rect_color, 5)
            back.set_text('<--', 20, WHITE)
            back.draw(0, 5)

            skin = Label(250, 700, 80, 80, button_blue, 5)
            skin.set_text('', 20, WHITE)
            skin.draw(50, 20)
            screen.blit(a[brawler].find_brawler(), (230, 680))

        if len(brawlerses) == 1:
            back = Label(10, 10, 40, 40, title_rect_color, 5)
            back.set_text('<--', 20, WHITE)
            back.draw(0, 5)
            screen.blit(a[brawler].find_brawler(), (230, 680))

            skin = Label(250, 700, 80, 80, button_blue, 5)
            skin.set_text('', 20, WHITE)
            skin.draw(50, 20)
            screen.blit(a[brawler].find_brawler(), (230, 680))

            skin1 = Label(350, 700, 80, 80, button_blue, 5)
            skin1.set_text('', 20, WHITE)
            skin1.draw(50, 20)
            skinss = skins[brawlerses[0] + '_skin']
            screen.blit(skinss.find_skin(), (330, 680))

        if len(brawlerses) == 2:
            back = Label(10, 10, 40, 40, title_rect_color, 5)
            back.set_text('<--', 20, WHITE)
            back.draw(0, 5)

            skin = Label(250, 700, 80, 80, button_blue, 5)
            skin.set_text('', 20, WHITE)
            skin.draw(50, 20)
            screen.blit(a[brawler].find_brawler(), (230, 680))

            skin1 = Label(350, 700, 80, 80, button_blue, 5)
            skin1.set_text('', 20, WHITE)
            skin1.draw(50, 20)
            skinss = skins[brawlerses[0] + '_skin']

            screen.blit(skinss.find_skin(), (330, 680))
            skin2 = Label(450, 700, 80, 80, button_blue, 5)
            skin2.set_text('', 20, WHITE)
            skin2.draw(50, 20)

            skinss1 = skins[brawlerses[1] + '_skin']
            screen.blit(skinss1.find_skin(), (430, 680))
    except:
        back = Label(10, 10, 40, 40, title_rect_color, 5)
        back.set_text('<--', 20, WHITE)
        back.draw(0, 5)

        skin = Label(250, 700, 80, 80, button_blue, 5)
        skin.set_text('', 20, WHITE)
        skin.draw(50, 20)
        screen.blit(a[brawler].find_brawler(), (230, 680))

    running = True
    while running:
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back.rect.collidepoint(event.pos):
                    running = False
                    brawlermenu(bg)
                try:
                    if skin.rect.collidepoint(event.pos):
                        brawlernow = a[brawler]

                        running = False
                        scene_main(1, bg)
                    if skin1.rect.collidepoint(event.pos):
                        brawlernow = skinss

                        running = False
                        scene_main(1, bg)
                    if skin2.rect.collidepoint(event.pos):
                        brawlernow = skinss1

                        running = False
                        scene_main(1, bg)
                except:
                    pass
            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def brawlermenu(bg):
    global brawlernow
    global unlocked_brawlers
    a = {'poco': poco, 'stu': stu, 'mrs_pi': mrs_pi, 'serge': surge, 'geyl': geyl, 'edgar': edgar, 'frenk': frenk,
         '8_bit': bit_8, 'crow': crow, 'leon': leon, 'spik': spik}

    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    running = True
    unlocked_brawlers = []

    if listB['brawlers']['poco']['unlock'] == True:
        unlocked_brawlers.append('poco')
    if listB['brawlers']['spik']['unlock'] == True:
        unlocked_brawlers.append('spik')
    if listB['brawlers']['8_bit']['unlock'] == True:
        unlocked_brawlers.append('8_bit')
    if listB['brawlers']['crow']['unlock'] == True:
        unlocked_brawlers.append('crow')
    if listB['brawlers']['edgar']['unlock'] == True:
        unlocked_brawlers.append('edgar')
    if listB['brawlers']['frenk']['unlock'] == True:
        unlocked_brawlers.append('frenk')
    if listB['brawlers']['geyl']['unlock'] == True:
        unlocked_brawlers.append('geyl')
    if listB['brawlers']['leon']['unlock'] == True:
        unlocked_brawlers.append('leon')
    if listB['brawlers']['stu']['unlock'] == True:
        unlocked_brawlers.append('stu')
    if listB['brawlers']['serge']['unlock'] == True:
        unlocked_brawlers.append('serge')
    if listB['brawlers']['mrs_pi']['unlock'] == True:
        unlocked_brawlers.append('mrs_pi')

    while running:
        title_text = Label(350, 50, 300, 75, title_rect_color, 20)
        title_text.set_text(f'Brawlers {len(unlocked_brawlers)} / 11', 30, WHITE)
        title_text.draw(25, 15)

        back = Label(10, 10, 150, 40, title_rect_color, 20)
        back.set_text('Menu return', 20, WHITE)
        back.draw(12, 5)

        if len(unlocked_brawlers) >= 1:
            button_1 = Label(50, 175, 250, 150, grey, 20)
            button_1.set_text(unlocked_brawlers[0], 20, BLACK)
            button_1.draw(100, 115)
            screen.blit(a[unlocked_brawlers[0]].find_brawler(), (115, 195))
        if len(unlocked_brawlers) >= 2:
            button_2 = Label(350, 175, 250, 150, grey, 20)
            button_2.set_text(unlocked_brawlers[1], 20, BLACK)
            button_2.draw(105, 115)
            screen.blit(a[unlocked_brawlers[1]].find_brawler(), (410, 175))

        if len(unlocked_brawlers) >= 3:
            button_3 = Label(650, 175, 250, 150, grey, 20)
            button_3.set_text(unlocked_brawlers[2], 20, BLACK)
            button_3.draw(100, 115)
            screen.blit(a[unlocked_brawlers[2]].find_brawler(), (715, 165))

        if len(unlocked_brawlers) >= 4:
            button_4 = Label(50, 475, 250, 150, grey, 20)
            button_4.set_text(unlocked_brawlers[3], 20, BLACK)
            button_4.draw(100, 115)
            screen.blit(a[unlocked_brawlers[3]].find_brawler(), (110, 475))

        if len(unlocked_brawlers) >= 5:
            button_5 = Label(350, 475, 250, 150, grey, 20)
            button_5.set_text(unlocked_brawlers[4], 20, BLACK)
            button_5.draw(98, 115)
            screen.blit(a[unlocked_brawlers[4]].find_brawler(), (410, 485))

        if len(unlocked_brawlers) >= 6:
            button_6 = Label(650, 475, 250, 150, grey, 20)
            button_6.set_text(unlocked_brawlers[5], 20, BLACK)
            button_6.draw(100, 115)
            screen.blit(a[unlocked_brawlers[5]].find_brawler(), (710, 485))

        if len(unlocked_brawlers) >= 7:
            next_page = Label(925, 375, 50, 50, title_rect_color, 15)
            next_page.set_text('>', 20, BLACK)
            next_page.draw(18, 10)

        # if len(unlocked_brawlers) >= 7:
        #     button_7 = Label(50, 175, 250, 150, grey)
        #     button_7.set_text(unlocked_brawlers[0], 20, BLACK)
        #     button_7.draw(100, 115)
        # if len(unlocked_brawlers) >= 8:
        #     button_8 = Label(50, 175, 250, 150, grey)
        #     button_8.set_text(unlocked_brawlers[0], 20, BLACK)
        #     button_8.draw(100, 115)
        # if len(unlocked_brawlers) >= 9:
        #     button_9 = Label(50, 175, 250, 150, grey)
        #     button_9.set_text(unlocked_brawlers[0], 20, BLACK)
        #     button_9.draw(100, 115)
        # if len(unlocked_brawlers) >= 10:
        #     button_1 = Label(50, 175, 250, 150, grey)
        #     button_1.set_text(unlocked_brawlers[0], 20, BLACK)
        #     button_1.draw(100, 115)
        # if len(unlocked_brawlers) >= 11:
        #     button_1 = Label(50, 175, 250, 150, grey)
        #     button_1.set_text(unlocked_brawlers[0], 20, BLACK)
        #     button_1.draw(100, 115)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back.rect.collidepoint(event.pos):
                    running = False
                    scene_main(1, bg)
                if len(unlocked_brawlers) >= 1:
                    if button_1.rect.collidepoint(event.pos):
                        if unlocked_brawlers[0] == 'poco':
                            brawlerPrew(bg, 'poco')
                        elif unlocked_brawlers[0] == 'spik':
                            brawlerPrew(bg, 'spik')
                        elif unlocked_brawlers[0] == '8_bit':
                            brawlerPrew(bg, '8_bit')
                        elif unlocked_brawlers[0] == 'crow':
                            brawlerPrew(bg, 'crow')
                        elif unlocked_brawlers[0] == 'edgar':
                            brawlerPrew(bg, 'edgar')
                        elif unlocked_brawlers[0] == 'frenk':
                            brawlerPrew(bg, 'frenk')
                        elif unlocked_brawlers[0] == 'geyl':
                            brawlerPrew(bg, 'geyl')
                        elif unlocked_brawlers[0] == 'leon':
                            brawlerPrew(bg, 'leon')
                        elif unlocked_brawlers[0] == 'stu':
                            brawlerPrew(bg, 'stu')
                        elif unlocked_brawlers[0] == 'serge':
                            brawlerPrew(bg, 'serge')
                        elif unlocked_brawlers[0] == 'mrs_pi':
                            brawlerPrew(bg, 'mrs_pi')
                        running = False

                    if len(unlocked_brawlers) >= 2:
                        if button_2.rect.collidepoint(event.pos):
                            if unlocked_brawlers[1] == 'poco':
                                brawlerPrew(bg, 'poco')
                            elif unlocked_brawlers[1] == 'spik':
                                brawlerPrew(bg, 'spik')
                            elif unlocked_brawlers[1] == '8_bit':
                                brawlerPrew(bg, '8_bit')
                            elif unlocked_brawlers[1] == 'crow':
                                brawlerPrew(bg, 'crow')
                            elif unlocked_brawlers[1] == 'edgar':
                                brawlerPrew(bg, 'edgar')
                            elif unlocked_brawlers[1] == 'frenk':
                                brawlerPrew(bg, 'frenk')
                            elif unlocked_brawlers[1] == 'geyl':
                                brawlerPrew(bg, 'geyl')
                            elif unlocked_brawlers[1] == 'leon':
                                brawlerPrew(bg, 'leon')
                            elif unlocked_brawlers[1] == 'stu':
                                brawlerPrew(bg, 'stu')
                            elif unlocked_brawlers[1] == 'serge':
                                brawlerPrew(bg, 'serge')
                            elif unlocked_brawlers[1] == 'mrs_pi':
                                brawlerPrew(bg, 'mrs_pi')
                            running = False

                    if len(unlocked_brawlers) >= 3:
                        if button_3.rect.collidepoint(event.pos):
                            if unlocked_brawlers[2] == 'poco':
                                brawlerPrew(bg, 'poco')
                            elif unlocked_brawlers[2] == 'spik':
                                brawlerPrew(bg, 'spik')
                            elif unlocked_brawlers[2] == '8_bit':
                                brawlerPrew(bg, '8_bit')
                            elif unlocked_brawlers[2] == 'crow':
                                brawlerPrew(bg, 'crow')
                            elif unlocked_brawlers[2] == 'edgar':
                                brawlerPrew(bg, 'edgar')
                            elif unlocked_brawlers[2] == 'frenk':
                                brawlerPrew(bg, 'frenk')
                            elif unlocked_brawlers[2] == 'geyl':
                                brawlerPrew(bg, 'geyl')
                            elif unlocked_brawlers[2] == 'leon':
                                brawlerPrew(bg, 'leon')
                            elif unlocked_brawlers[2] == 'stu':
                                brawlerPrew(bg, 'stu')
                            elif unlocked_brawlers[2] == 'serge':
                                brawlerPrew(bg, 'serge')
                            elif unlocked_brawlers[2] == 'mrs_pi':
                                brawlerPrew(bg, 'mrs_pi')
                            running = False

                    if len(unlocked_brawlers) >= 4:
                        if button_4.rect.collidepoint(event.pos):
                            if unlocked_brawlers[3] == 'poco':
                                brawlerPrew(bg, 'poco')
                            elif unlocked_brawlers[3] == 'spik':
                                brawlerPrew(bg, 'spik')
                            elif unlocked_brawlers[3] == '8_bit':
                                brawlerPrew(bg, '8_bit')
                            elif unlocked_brawlers[3] == 'crow':
                                brawlerPrew(bg, 'crow')
                            elif unlocked_brawlers[3] == 'edgar':
                                brawlerPrew(bg, 'edgar')
                            elif unlocked_brawlers[3] == 'frenk':
                                brawlerPrew(bg, 'frenk')
                            elif unlocked_brawlers[3] == 'geyl':
                                brawlerPrew(bg, 'geyl')
                            elif unlocked_brawlers[3] == 'leon':
                                brawlerPrew(bg, 'leon')
                            elif unlocked_brawlers[3] == 'stu':
                                brawlerPrew(bg, 'stu')
                            elif unlocked_brawlers[3] == 'serge':
                                brawlerPrew(bg, 'serge')
                            elif unlocked_brawlers[3] == 'mrs_pi':
                                brawlerPrew(bg, 'mrs_pi')
                            running = False

                    if len(unlocked_brawlers) >= 5:
                        if button_5.rect.collidepoint(event.pos):
                            if unlocked_brawlers[4] == 'poco':
                                brawlerPrew(bg, 'poco')
                            elif unlocked_brawlers[4] == 'spik':
                                brawlerPrew(bg, 'spik')
                            elif unlocked_brawlers[4] == '8_bit':
                                brawlerPrew(bg, '8_bit')
                            elif unlocked_brawlers[4] == 'crow':
                                brawlerPrew(bg, 'crow')
                            elif unlocked_brawlers[4] == 'edgar':
                                brawlerPrew(bg, 'edgar')
                            elif unlocked_brawlers[4] == 'frenk':
                                brawlerPrew(bg, 'frenk')
                            elif unlocked_brawlers[4] == 'geyl':
                                brawlerPrew(bg, 'geyl')
                            elif unlocked_brawlers[4] == 'leon':
                                brawlerPrew(bg, 'leon')
                            elif unlocked_brawlers[4] == 'stu':
                                brawlerPrew(bg, 'stu')
                            elif unlocked_brawlers[4] == 'serge':
                                brawlerPrew(bg, 'serge')
                            elif unlocked_brawlers[4] == 'mrs_pi':
                                brawlerPrew(bg, 'mrs_pi')
                            running = False

                    if len(unlocked_brawlers) >= 6:
                        if button_6.rect.collidepoint(event.pos):
                            if unlocked_brawlers[5] == 'poco':
                                brawlerPrew(bg, 'poco')
                            elif unlocked_brawlers[5] == 'spik':
                                brawlerPrew(bg, 'spik')
                            elif unlocked_brawlers[5] == '8_bit':
                                brawlerPrew(bg, '8_bit')
                            elif unlocked_brawlers[5] == 'crow':
                                brawlerPrew(bg, 'crow')
                            elif unlocked_brawlers[5] == 'edgar':
                                brawlerPrew(bg, 'edgar')
                            elif unlocked_brawlers[5] == 'frenk':
                                brawlerPrew(bg, 'frenk')
                            elif unlocked_brawlers[5] == 'geyl':
                                brawlerPrew(bg, 'geyl')
                            elif unlocked_brawlers[5] == 'leon':
                                brawlerPrew(bg, 'leon')
                            elif unlocked_brawlers[5] == 'stu':
                                brawlerPrew(bg, 'stu')
                            elif unlocked_brawlers[5] == 'serge':
                                brawlerPrew(bg, 'serge')
                            elif unlocked_brawlers[5] == 'mrs_pi':
                                brawlerPrew(bg, 'mrs_pi')
                            running = False

                    if len(unlocked_brawlers) >= 7:
                        if next_page.rect.collidepoint(event.pos):
                            running = False
                            brawlermenu2(bg)

            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def brawlermenu2(bg):
    global brawlernow
    a = {'poco': poco, 'stu': stu, 'mrs_pi': mrs_pi, 'serge': surge, 'geyl': geyl, 'edgar': edgar, 'frenk': frenk,
         '8_bit': bit_8, 'crow': crow, 'leon': leon, 'spik': spik}
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    running = True
    while running:
        title_text = Label(350, 50, 300, 75, title_rect_color, 20)
        title_text.set_text(f'Brawlers {len(unlocked_brawlers)} / 11', 30, WHITE)
        title_text.draw(25, 15)

        next_page = Label(15, 375, 50, 50, title_rect_color, 15)
        next_page.set_text('<', 20, BLACK)
        next_page.draw(15, 10)

        back = Label(10, 10, 150, 40, title_rect_color, 20)
        back.set_text('Menu return', 20, WHITE)
        back.draw(12, 5)

        if len(unlocked_brawlers) >= 7:
            button_7 = Label(50, 175, 250, 150, grey, 20)
            button_7.set_text(unlocked_brawlers[6], 20, BLACK)
            button_7.draw(102, 115)
            screen.blit(a[unlocked_brawlers[6]].find_brawler(), (115, 185))

        if len(unlocked_brawlers) >= 8:
            button_8 = Label(350, 175, 250, 150, grey, 20)
            button_8.set_text(unlocked_brawlers[7], 20, BLACK)
            button_8.draw(102, 115)
            screen.blit(a[unlocked_brawlers[7]].find_brawler(), (415, 175))

        if len(unlocked_brawlers) >= 9:
            button_9 = Label(650, 175, 250, 150, grey, 20)
            button_9.set_text(unlocked_brawlers[8], 20, BLACK)
            button_9.draw(108, 115)
            screen.blit(a[unlocked_brawlers[8]].find_brawler(), (720, 175))

        if len(unlocked_brawlers) >= 10:
            button_10 = Label(50, 475, 250, 150, grey, 20)
            button_10.set_text(unlocked_brawlers[9], 20, BLACK)
            button_10.draw(100, 115)
            screen.blit(a[unlocked_brawlers[9]].find_brawler(), (115, 475))

        if len(unlocked_brawlers) >= 11:
            button_11 = Label(350, 475, 250, 150, grey, 20)
            button_11.set_text(unlocked_brawlers[10], 20, BLACK)
            button_11.draw(95, 115)
            screen.blit(a[unlocked_brawlers[10]].find_brawler(), (415, 485))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back.rect.collidepoint(event.pos):
                    running = False
                    scene_main(1, bg)
                if len(unlocked_brawlers) >= 7:
                    if button_7.rect.collidepoint(event.pos):
                        if unlocked_brawlers[6] == 'poco':
                            brawlerPrew(bg, 'poco')
                        elif unlocked_brawlers[6] == 'spik':
                            brawlerPrew(bg, 'spik')
                        elif unlocked_brawlers[6] == '8_bit':
                            brawlerPrew(bg, '8_bit')
                        elif unlocked_brawlers[6] == 'crow':
                            brawlerPrew(bg, 'crow')
                        elif unlocked_brawlers[6] == 'edgar':
                            brawlerPrew(bg, 'edgar')
                        elif unlocked_brawlers[6] == 'frenk':
                            brawlerPrew(bg, 'frenk')
                        elif unlocked_brawlers[6] == 'geyl':
                            brawlerPrew(bg, 'geyl')
                        elif unlocked_brawlers[6] == 'leon':
                            brawlerPrew(bg, 'leon')
                        elif unlocked_brawlers[6] == 'stu':
                            brawlerPrew(bg, 'stu')
                        elif unlocked_brawlers[6] == 'serge':
                            brawlerPrew(bg, 'serge')
                        elif unlocked_brawlers[6] == 'mrs_pi':
                            brawlerPrew(bg, 'mrs_pi')
                        running = False

                if len(unlocked_brawlers) >= 8:
                    if button_8.rect.collidepoint(event.pos):
                        if unlocked_brawlers[7] == 'poco':
                            brawlerPrew(bg, 'poco')
                        elif unlocked_brawlers[7] == 'spik':
                            brawlerPrew(bg, 'spik')
                        elif unlocked_brawlers[7] == '8_bit':
                            brawlerPrew(bg, '8_bit')
                        elif unlocked_brawlers[7] == 'crow':
                            brawlerPrew(bg, 'crow')
                        elif unlocked_brawlers[7] == 'edgar':
                            brawlerPrew(bg, 'edgar')
                        elif unlocked_brawlers[7] == 'frenk':
                            brawlerPrew(bg, 'frenk')
                        elif unlocked_brawlers[7] == 'geyl':
                            brawlerPrew(bg, 'geyl')
                        elif unlocked_brawlers[7] == 'leon':
                            brawlerPrew(bg, 'leon')
                        elif unlocked_brawlers[7] == 'stu':
                            brawlerPrew(bg, 'stu')
                        elif unlocked_brawlers[7] == 'serge':
                            brawlerPrew(bg, 'serge')
                        elif unlocked_brawlers[7] == 'mrs_pi':
                            brawlerPrew(bg, 'mrs_pi')
                        running = False

                if len(unlocked_brawlers) >= 9:
                    if button_9.rect.collidepoint(event.pos):
                        if unlocked_brawlers[8] == 'poco':
                            brawlerPrew(bg, 'poco')
                        elif unlocked_brawlers[8] == 'spik':
                            brawlerPrew(bg, 'spik')
                        elif unlocked_brawlers[8] == '8_bit':
                            brawlerPrew(bg, '8_bit')
                        elif unlocked_brawlers[8] == 'crow':
                            brawlerPrew(bg, 'crow')
                        elif unlocked_brawlers[8] == 'edgar':
                            brawlerPrew(bg, 'edgar')
                        elif unlocked_brawlers[8] == 'frenk':
                            brawlerPrew(bg, 'frenk')
                        elif unlocked_brawlers[8] == 'geyl':
                            brawlerPrew(bg, 'geyl')
                        elif unlocked_brawlers[8] == 'leon':
                            brawlerPrew(bg, 'leon')
                        elif unlocked_brawlers[8] == 'stu':
                            brawlerPrew(bg, 'stu')
                        elif unlocked_brawlers[8] == 'serge':
                            brawlerPrew(bg, 'serge')
                        elif unlocked_brawlers[8] == 'mrs_pi':
                            brawlerPrew(bg, 'mrs_pi')
                        running = False

                if len(unlocked_brawlers) >= 10:
                    if button_10.rect.collidepoint(event.pos):
                        if unlocked_brawlers[9] == 'poco':
                            brawlerPrew(bg, 'poco')
                        elif unlocked_brawlers[9] == 'spik':
                            brawlerPrew(bg, 'spik')
                        elif unlocked_brawlers[9] == '8_bit':
                            brawlerPrew(bg, '8_bit')
                        elif unlocked_brawlers[9] == 'crow':
                            brawlerPrew(bg, 'crow')
                        elif unlocked_brawlers[9] == 'edgar':
                            brawlerPrew(bg, 'edgar')
                        elif unlocked_brawlers[9] == 'frenk':
                            brawlerPrew(bg, 'frenk')
                        elif unlocked_brawlers[9] == 'geyl':
                            brawlerPrew(bg, 'geyl')
                        elif unlocked_brawlers[9] == 'leon':
                            brawlerPrew(bg, 'leon')
                        elif unlocked_brawlers[9] == 'stu':
                            brawlerPrew(bg, 'stu')
                        elif unlocked_brawlers[9] == 'serge':
                            brawlerPrew(bg, 'serge')
                        elif unlocked_brawlers[9] == 'mrs_pi':
                            brawlerPrew(bg, 'mrs_pi')
                        running = False

                if len(unlocked_brawlers) >= 11:
                    if button_11.rect.collidepoint(event.pos):
                        if unlocked_brawlers[10] == 'poco':
                            brawlerPrew(bg, 'poco')
                        elif unlocked_brawlers[10] == 'spik':
                            brawlerPrew(bg, 'spik')
                        elif unlocked_brawlers[10] == '8_bit':
                            brawlerPrew(bg, '8_bit')
                        elif unlocked_brawlers[10] == 'crow':
                            brawlerPrew(bg, 'crow')
                        elif unlocked_brawlers[10] == 'edgar':
                            brawlerPrew(bg, 'edgar')
                        elif unlocked_brawlers[10] == 'frenk':
                            brawlerPrew(bg, 'frenk')
                        elif unlocked_brawlers[10] == 'geyl':
                            brawlerPrew(bg, 'geyl')
                        elif unlocked_brawlers[10] == 'leon':
                            brawlerPrew(bg, 'leon')
                        elif unlocked_brawlers[10] == 'stu':
                            brawlerPrew(bg, 'stu')
                        elif unlocked_brawlers[10] == 'serge':
                            brawlerPrew(bg, 'serge')
                        elif unlocked_brawlers[10] == 'mrs_pi':
                            brawlerPrew(bg, 'mrs_pi')
                        running = False

                if next_page.rect.collidepoint(event.pos):
                    print('tssss')
                    running = False
                    brawlermenu(bg)
            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def shop_page1(bg):
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    a = {'poco': poco, 'stu': stu, 'mrs_pi': mrs_pi, 'serge': surge, 'geyl': geyl, 'edgar': edgar, 'frenk': frenk,
         '8_bit': bit_8, 'crow': crow, 'leon': leon, 'spik': spik}
    buy_shop = ['gems', 'gerch', 'coin']
    gems_count = [10, 20, 30, 25]
    gerchBrawler = ["spik", "leon", "8_bit", "crow", "frenk", "edgar", "geyl", "stu", "poco", "surge", "mrs_pi"]
    coin_count = [200, 250, 300, 400, 350, 500, 450]
    running = True
    title_text = Label(450, 50, 0, 0, goodYellow)
    title_text.set_text('Shop', 40, WHITE)
    title_text.draw(0, 0)
    gift_button = Label(50, 150, 300, 600, goodYellow)
    gift_button.set_text('Gift Day', 20, BLACK)
    gift_button.draw(100, 25)
    home_button = Label(50, 50, 150, 50, title_rect_color)
    home_button.set_text('Return menu', 15, WHITE)
    home_button.draw(25, 15)
    right_button = Label(900, 380, 50, 50, title_rect_color)
    right_button.set_text('>', 40, WHITE)
    right_button.draw(10, 0)
    bottom_text = Label(350, 770, 0, 0, WHITE)
    bottom_text.set_text('Daily events ', 25, WHITE)
    bottom_text.draw(0, 0)
    # ·
    bottom_text1 = Label(515, 775, 0, 0, WHITE)
    bottom_text1.set_text('· Skins · Boxes', 20, WHITE)
    bottom_text1.draw(0, 0)
    if time_now >= listB['gift_day']['time_next_gift']:
        rand1 = random.choice(buy_shop)
        rand2 = random.choice(buy_shop)
        rand3 = random.choice(buy_shop)
        rand4 = random.choice(buy_shop)
        if rand1 == 'gerch':
            choice1 = random.choice(gerchBrawler)
        elif rand1 == 'coin':
            choice1 = random.choice(coin_count)
        elif rand1 == 'gems':
            choice1 = random.choice(gems_count)
        if rand2 == 'gerch':
            choice2 = random.choice(gerchBrawler)
        elif rand2 == 'coin':
            choice2 = random.choice(coin_count)
        elif rand2 == 'gems':
            choice2 = random.choice(gems_count)
        if rand3 == 'gerch':
            choice3 = random.choice(gerchBrawler)
        elif rand3 == 'coin':
            choice3 = random.choice(coin_count)
        elif rand3 == 'gems':
            choice3 = random.choice(gems_count)
        if rand4 == 'gerch':
            choice4 = random.choice(gerchBrawler)
        elif rand4 == 'coin':
            choice4 = random.choice(coin_count)
        elif rand4 == 'gems':
            choice4 = random.choice(gems_count)
        listB['buy_shop']['buy1'] = rand1
        listB['buy_shop']['buy2'] = rand2
        listB['buy_shop']['buy3'] = rand3
        listB['buy_shop']['buy4'] = rand4
        listB['buy_shop']['buy1num'] = choice1
        listB['buy_shop']['buy2num'] = choice2
        listB['buy_shop']['buy3num'] = choice3
        listB['buy_shop']['buy4num'] = choice4

        listB['gift_day']['time_click'] = 0
        coin_gift = random.choice(day_gift_coin)
        listB['gift_day']['item_gift'] = coin_gift
        if coin_gift == 'coin_strong':
            amount_gift = random.randrange(1, 200)
            listB['gift_day']['time_next_gift'] = time_now + 86400
            listB['gift_day']['amount_gift'] = amount_gift
        elif coin_gift == 'coin':
            amount_gift = random.randrange(1, 1000)
            listB['gift_day']['time_next_gift'] = time_now + 86400
            listB['gift_day']['amount_gift'] = amount_gift
        elif coin_gift == 'gems':
            amount_gift = random.randrange(1, 20)
            listB['gift_day']['time_next_gift'] = time_now + 86400
            listB['gift_day']['amount_gift'] = amount_gift
    if listB['gift_day']['item_gift'] == 'coin_strong':
        screen.blit(coin_strong_image, (160, 400))
    elif listB['gift_day']['item_gift'] == 'coin':
        screen.blit(coin_image, (160, 400))
    elif listB['gift_day']['item_gift'] == 'gems':
        screen.blit(gems_image, (160, 400))
    amount_text = Label(100, 650, 0, 0, WHITE)
    amount_text.set_text('Amount gift day:' + str(listB['gift_day']['amount_gift']), 20, BLACK)
    amount_text.draw(0, 0)
    buy1_button = Label(420, 150, 200, 150, light_blue)
    buy1_button.set_text(f"{listB['buy_shop']['buy1']} {listB['buy_shop']['buy1num']}", 20, BLACK)
    buy1_button.draw(20, 10)
    buy2_button = Label(650, 150, 200, 150, light_blue)
    buy2_button.set_text(f"{listB['buy_shop']['buy2']} {listB['buy_shop']['buy2num']}", 20, BLACK)
    buy2_button.draw(20, 10)
    buy3_button = Label(420, 450, 200, 150, light_blue)
    buy3_button.set_text(f"{listB['buy_shop']['buy3']} {listB['buy_shop']['buy3num']}", 20, BLACK)
    buy3_button.draw(20, 10)
    buy4_button = Label(650, 450, 200, 150, light_blue)
    buy4_button.set_text(f"{listB['buy_shop']['buy4']} {listB['buy_shop']['buy4num']}", 20, BLACK)
    buy4_button.draw(20, 10)
    if listB['gift_day']['time_click'] == 1:
        already_text = Label(60, 550, 0, 0, WHITE)
        already_text.set_text('You have already received the reward', 15, BLACK)
        already_text.draw(0, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if gift_button.rect.collidepoint(event.pos):
                    if listB['gift_day']['time_click'] == 0:
                        listB['gift_day']['time_gift'] = time_now + 86400
                        listB['gift_day']['time_next_gift'] = listB['gift_day']['time_gift']
                        if listB['gift_day']['item_gift'] == 'coin_strong':
                            listB['currency']['coin_strong'] += listB['gift_day']['amount_gift']
                            print('+ coin strong')
                        elif listB['gift_day']['item_gift'] == 'coin':
                            listB['currency']['coin'] += listB['gift_day']['amount_gift']
                            print('+ coin')
                        elif listB['gift_day']['item_gift'] == 'gems':
                            listB['currency']['gems'] += listB['gift_day']['amount_gift']
                            print('+ gems')
                        listB['gift_day']['time_click'] += 1
                elif home_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    scene_main(1, bg)


                elif right_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    shop_page2(bg)

            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def shop_page2(bg):
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    running = True
    title_text = Label(450, 50, 0, 0, goodYellow)
    title_text.set_text('Shop', 40, WHITE)
    title_text.draw(0, 0)
    home_button = Label(50, 50, 150, 50, title_rect_color)
    home_button.set_text('Return menu', 15, WHITE)
    home_button.draw(25, 15)
    skins_1 = Label(200, 200, 200, 400, title_rect_color)
    skins_2 = Label(550, 200, 200, 400, title_rect_color)
    sell30 = Label(550, 200, 0, 0, title_rect_color)

    right_button = Label(900, 380, 50, 50, title_rect_color)
    right_button.set_text('>', 40, WHITE)
    right_button.draw(10, 0)
    left_button = Label(50, 380, 50, 50, title_rect_color)
    left_button.set_text('<', 40, WHITE)
    left_button.draw(10, 0)
    bottom_text = Label(350, 775, 0, 0, WHITE)
    bottom_text.set_text('Daily events ·', 20, WHITE)
    bottom_text.draw(0, 0)
    # ·
    bottom_text1 = Label(500, 770, 0, 0, WHITE)
    bottom_text1.set_text('Skins', 25, WHITE)
    bottom_text1.draw(0, 0)
    bottom_text2 = Label(570, 775, 0, 0, WHITE)
    bottom_text2.set_text(' · Boxes', 20, WHITE)
    bottom_text2.draw(0, 0)
    if listB['skins_shop']['next_skins'] <= time_now:
        listB['skins_shop']['next_skins'] = time_now + 86400
        print(len(skins_shop))
        if len(skins_shop) >= 1:
            skin1 = random.choice(skins_shop)

            if skin1 == 'spik_sakura':
                skins_1.set_text('Sakura Spik', 15, WHITE)
                skins_1.draw(25, 15)
                screen.blit(gems_image, (200, 500))
                sell60 = Label(275, 515, 0, 0, title_rect_color)
                sell60.set_text('60 gems', 25)
                sell60.draw()
                screen.blit(spik_sakura, (240, 335))
                listB['skins_shop']['skins_1'] = "spik_sakura"

            elif skin1 == 'poco_pirate':
                skins_1.set_text('Poco Pirate', 15, WHITE)
                skins_1.draw(25, 15)
                screen.blit(gems_image, (200, 500))
                sell30 = Label(275, 515, 0, 0, title_rect_color)
                sell30.set_text('30 gems', 25)
                sell30.draw()
                screen.blit(poco_pirateSkin, (240, 335))
                listB['skins_shop']['skins_1'] = 'poco_pirateSkin'
        if len(skins_shop) >= 2:
            for i in skins_shop:
                if skin1 == i:
                    skins_shop.remove(i)
            skin2 = random.choice(skins_shop)
            print('dsfj_____________')
            if skin2 == 'poco_pirate':
                skins_2.set_text('Poco Pirate', 15, WHITE)
                skins_2.draw(25, 15)
                screen.blit(gems_image, (550, 500))
                screen.blit(poco_pirateSkin, (575, 335))
                listB['skins_shop']['skins_2'] = 'poco_pirateSkin'
            elif skin2 == 'spik_sakura':
                skins_2.set_text('Sakura Spik', 15, WHITE)
                skins_2.draw(25, 15)
                screen.blit(gems_image, (550, 500))
                screen.blit(spik_sakura, (575, 335))
                listB['skins_shop']['skins_2'] = 'spik_sakura'

        print(listB['skins_shop']['next_skins'])
    else:
        print(listB['skins_shop']['next_skins'])
        if listB['skins_shop']['skins_1'] == 'spik_sakura':
            skins_1.set_text('Sakura Spik', 15, WHITE)
            skins_1.draw(25, 15)
            sell60 = Label(275, 515, 0, 0, title_rect_color)
            sell60.set_text('60 gems', 25)
            sell60.draw()
            screen.blit(gems_image, (200, 500))
            screen.blit(spik_sakura, (240, 335))

        if listB['skins_shop']['skins_2'] == 'poco_pirateSkin':
            skins_2.set_text('Poco Pirate', 15, WHITE)
            skins_2.draw(25, 15)
            screen.blit(gems_image, (550, 500))
            screen.blit(poco_pirateSkin, (575, 335))

        if listB['skins_shop']['skins_1'] == 'poco_pirateSkin':
            skins_1.set_text('Poco Pirate', 15, WHITE)
            skins_1.draw(25, 15)
            sell30 = Label(275, 515, 0, 0, title_rect_color)
            sell30.set_text('30 gems', 25)
            sell30.draw()
            screen.blit(gems_image, (200, 500))
            screen.blit(poco_pirateSkin, (240, 335))



        if listB['skins_shop']['skins_2'] == 'spik_sakura':
            skins_2.set_text('Sakura Spik', 15, WHITE)
            skins_2.draw(25, 15)
            screen.blit(gems_image, (550, 500))
            screen.blit(spik_sakura, (575, 335))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if right_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    shop_page3(bg)
                elif home_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    scene_main(1, bg)

                elif skins_1.rect.collidepoint(event.pos):
                    skinn1 = listB['skins_shop']['skins_1']
                    if skinn1 == 'poco_pirateSkin':
                        if listB['currency']['gems'] >= 30:
                            listB['currency']['gems'] -= 30
                            if listB['skins_shop']['skins_2'] == None:
                                listB['skins_shop']['skins_1'] = None
                            else:
                                listB['skins_shop']['skins_1'] = listB['skins_shop']['skins_2']
                                listB['skins_shop']['skins_2'] = None
                            listB['brawlers']['poco']['skins']['poco_pirate'] = True
                    elif skinn1 == 'spik_sakura':
                        if listB['currency']['gems'] >= 60:
                            listB['currency']['gems'] -= 60
                            if listB['skins_shop']['skins_2'] == None:
                                listB['skins_shop']['skins_1'] = None
                            else:
                                listB['skins_shop']['skins_1'] = listB['skins_shop']['skins_2']
                                listB['skins_shop']['skins_2'] = None
                            listB['brawlers']['spik']['skins']['spik_sakura'] = True
                    running = False
                    scene_main(1, bg)



                elif skins_2.rect.collidepoint(event.pos):
                    skinn2 = listB['skins_shop']['skins_2']
                    if skinn2 == 'poco_pirateSkin':
                        if listB['currency']['gems'] >= 30:
                            listB['currency']['gems'] -= 30
                            listB['skins_shop']['skins_2'] = None
                            listB['brawlers']['poco']['skins']['poco_pirate'] = True

                    elif skinn2 == 'spik_sakura':
                        if listB['currency']['gems'] >= 60:
                            listB['currency']['gems'] -= 60
                            listB['skins_shop']['skins_2'] = None
                            listB['brawlers']['spik']['skins']['spik_sakura'] = True

                            print('spik')
                    running = False
                    scene_main(1, bg)

                elif left_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    shop_page1(bg)

            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def shop_page3(bg):
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    running = True
    title_text = Label(450, 50, 0, 0, goodYellow)
    title_text.set_text('Shop', 40, WHITE)
    title_text.draw(0, 0)
    home_button = Label(50, 50, 150, 50, title_rect_color)
    home_button.set_text('Return menu', 15, WHITE)
    home_button.draw(25, 15)
    left_button = Label(50, 380, 50, 50, title_rect_color)
    left_button.set_text('<', 40, WHITE)
    left_button.draw(10, 0)
    bottom_text = Label(350, 775, 0, 0, WHITE)
    bottom_text.set_text('Daily events · Skins ·', 20, WHITE)
    bottom_text.draw(0, 0)
    # ·

    bottom_text1 = Label(570, 770, 0, 0, WHITE)
    bottom_text1.set_text('Boxes', 25, WHITE)
    bottom_text1.draw(0, 0)
    button_box = Label(170, 300, 230, 200, light_blue, 10)
    button_box.set_text('Box', 40, WHITE)
    button_box.draw(80, 45)
    screen.blit(box_image, (200, 350))
    cost_button_box = Label(170, 370, 0, 0, light_blue, 10)
    cost_button_box.set_text('30 gems', 30, WHITE)
    cost_button_box.draw(80, 45)
    screen.blit(gems_image, (170, 400))
    button_bigbox = Label(420, 300, 230, 200, light_blue, 10)
    button_bigbox.set_text('Big box', 40, WHITE)
    button_bigbox.draw(50, 45)
    screen.blit(big_box_image, (420, 350))
    cost_button_bigbox = Label(420, 370, 0, 0, light_blue, 10)
    cost_button_bigbox.set_text('60 gems', 30, WHITE)
    cost_button_bigbox.draw(80, 45)
    screen.blit(gems_image, (420, 400))
    button_megabox = Label(670, 300, 230, 200, light_blue, 10)
    button_megabox.set_text('Mega box', 40, WHITE)
    button_megabox.draw(40, 45)
    screen.blit(mega_box_image, (660, 350))
    cost_button_megabox = Label(670, 370, 0, 0, light_blue, 10)
    cost_button_megabox.set_text('80 gems', 30, WHITE)
    cost_button_megabox.draw(80, 45)
    screen.blit(gems_image, (670, 400))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if home_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    scene_main(1, bg)
                elif left_button.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    shop_page2(bg)
                elif button_box.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    box(bg, 'gems', 30)
                elif button_bigbox.rect.collidepoint(event.pos):
                    if listB['currency']['gems'] >= 60:
                        print('Удачно!')
                        running = False
                        big_box(bg)
                elif button_megabox.rect.collidepoint(event.pos):
                    if listB['currency']['gems'] >= 80:
                        print('Удачно!')
                        running = False
                        mega_box(bg)
            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def scene_music(bg):
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    running = True
    while running:
        title_text = Label(300, 50, 400, 100, title_rect_color, 25)
        title_text.set_text('Edit music', 40, WHITE)
        title_text.draw(90, 25)

        edit_music_button1 = Label(50, 400, 280, 75, title_rect_color, 25)
        edit_music_button1.set_text('Bad Randoms music', 25, WHITE)
        edit_music_button1.draw(15, 20)

        edit_music_button2 = Label(375, 400, 280, 75, title_rect_color, 25)
        edit_music_button2.set_text('Menu music 2', 25, WHITE)
        edit_music_button2.draw(50, 20)

        edit_music_button3 = Label(700, 400, 280, 75, title_rect_color, 25)
        edit_music_button3.set_text('Menu music 3', 25, WHITE)
        edit_music_button3.draw(50,20)

        edit_music_button4 = Label(50, 600, 280, 75, title_rect_color, 25)
        edit_music_button4.set_text('Menu music 4', 25, WHITE)
        edit_music_button4.draw(50, 20)

        edit_music_button_stop = Label(375, 600, 280, 75, title_rect_color, 25)
        edit_music_button_stop.set_text('Music stop', 25, WHITE)
        edit_music_button_stop.draw(70, 20)

        edit_music_button_continue = Label(700, 600, 280, 75, title_rect_color, 25)
        edit_music_button_continue.set_text('Menu return', 25, WHITE)
        edit_music_button_continue.draw(60, 20)

        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if edit_music_button1.rect.collidepoint(event.pos):
                    print('Удачно!')
                    sound1.stop()
                    sound2.stop()
                    sound3.stop()
                    sound4.stop()
                    sound1.play(100)
                elif edit_music_button2.rect.collidepoint(event.pos):
                    print('Удачно!')
                    sound1.stop()
                    sound2.stop()
                    sound3.stop()
                    sound4.stop()
                    sound2.play(100)
                elif edit_music_button3.rect.collidepoint(event.pos):
                    print('Удачно!')
                    sound1.stop()
                    sound2.stop()
                    sound3.stop()
                    sound4.stop()
                    sound3.play(100)
                elif edit_music_button4.rect.collidepoint(event.pos):
                    print('Удачно!')
                    sound1.stop()
                    sound2.stop()
                    sound3.stop()
                    sound4.stop()
                    sound4.play(100)
                elif edit_music_button_stop.rect.collidepoint(event.pos):
                    print('Удачно!')
                    sound1.stop()
                    sound2.stop()
                    sound3.stop()
                    sound4.stop()
                elif edit_music_button_continue.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    scene_main(1, bg)

                else:
                    print('не попал')

            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def scene_bg(bg):
    if bg == 1:
        screen.blit(bg_default, (0, 0))
    elif bg == 2:
        screen.blit(bg_2, (0, 0))
    running = True
    while running:
        title_text = Label(300, 50, 400, 100, title_rect_color, 25)
        title_text.set_text('Edit background', 40, WHITE)
        title_text.draw(40, 25)

        edit_bg_button = Label(45, 400, 250, 75, title_rect_color, 25)
        edit_bg_button.set_text('Background 1', 25, WHITE)
        edit_bg_button.draw(35, 20)

        edit_bg_button2 = Label(375, 400, 250, 75, title_rect_color, 25)
        edit_bg_button2.set_text('Background 2', 25, WHITE)
        edit_bg_button2.draw(35, 20)
        edit_bg_button3 = Label(700, 400, 250, 75, title_rect_color, 25)
        edit_bg_button3.set_text('Menu return', 25, WHITE)
        edit_bg_button3.draw(45, 20)
        # Ввод процесса (события)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if edit_bg_button3.rect.collidepoint(event.pos):
                    print('Удачно!')
                    running = False
                    scene_main(1, bg)
                elif edit_bg_button2.rect.collidepoint(event.pos):
                    bg = 2
                    screen.blit(bg_2, (0, 0))
                elif edit_bg_button.rect.collidepoint(event.pos):
                    bg = 1
                    screen.blit(bg_default, (0, 0))

                else:
                    print('не попал')
            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
        clock.tick(FPS)
        pygame.display.update()


def scene_over_showdown(brawler, score, timer):
    screen.fill(light_blue)
    try:
        brawlerP = brawler.find_brawler()
    except:
        brawlerP = brawler.find_skin()

    screen.blit(brawlerP, (420, 420))
    if timer >= 50:
        if timer / score <= 8:
            screen.blit(win, (0, 0))
            title_text = Label(100, 50, 0, 0, title_rect_color)
            title_text.set_text('WIN', 25, WHITE)
            title_text.draw(0, 0)
            listB['trophies'] += 10
            listB['currency']['gem_box'] += random.randrange(5, 15) * score
            print(listB['currency']['gem_box'])
            play_exit_don = Label(800, 700, 100, 75, title_rect_color, 20)
            play_exit_don.set_text('Exit', 25, WHITE)
            play_exit_don.draw(25, 20)
        else:
            screen.blit(lose, (0, 0))
            title_text = Label(100, 50, 0, 0, title_rect_color)
            title_text.set_text('LOSE', 25, WHITE)
            title_text.draw(0, 0)
            play_exit_don = Label(800, 700, 100, 75, title_rect_color, 20)
            play_exit_don.set_text('Exit', 25, WHITE)
            play_exit_don.draw(50, 20)
            if listB['trophies'] >= 10:
                listB['trophies'] -= 5

    else:
        screen.blit(lose, (0, 0))
        lose_text = Label(50, 20, 0, 0, title_rect_color)
        lose_text.set_text('LOSE', 50, WHITE)
        lose_text.draw(0, 0)
        play_exit_don = Label(800, 700, 100, 75, title_rect_color, 20)
        play_exit_don.set_text('Exit', 25, WHITE)
        play_exit_don.draw(25, 20)
        if listB['trophies'] >= 10:
            listB['trophies'] -= 8
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_exit_don.rect.collidepoint(event.pos):
                    print('Удачно!')
                    scene_main(0, 1)
            elif event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')

        clock.tick(FPS)
        pygame.display.update()
def scene_game_hotZone(brawler):
    screen.blit(search_bg, (0, 0))
    pygame.display.update()
    sound1.stop()
    sound2.stop()
    sound3.stop()
    sound4.stop()
    search_sound.play()
    time.sleep(2)
    timeMet = 1.5
    timePreMet = 0.3
    faze = 1
    coordx = random.randrange(100,700)
    coordy = random.randrange(100, 700)
    coordx1 = random.randrange(100, 700)
    coordy1 = random.randrange(100, 700)
    coordx2 = random.randrange(100, 700)
    coordy2 = random.randrange(100, 700)
    last = 0

    # screen.blit(warn1,(300,300))
    # screen.blit(meteor,(300,300))
    # screen.blit(warn2, (300, 300))
    # screen.blit(warn3, (300, 300))
    # screen.blit(warn4, (300, 300))
    # screen.blit(zone, (600, 300))
    start_timer = time.time()
    running = True
    while running:
        screen.blit(map,(-10,-10))
        end_time = time.time()
        print(last)
        print(end_time - (start_timer+last))
        if end_time - (start_timer+last) >= timeMet:
            if faze == 1:
                screen.blit(warn4, (coordx, coordy))
                screen.blit(warn4, (coordx1, coordy1))
                screen.blit(warn4, (coordx2, coordy2))
                if end_time - (start_timer+last+timeMet) >= timeMet:
                    faze+=1
            elif faze == 2:
                screen.blit(warn3, (coordx, coordy))
                screen.blit(warn3, (coordx1, coordy1))
                screen.blit(warn3, (coordx2, coordy2))

                if end_time - (start_timer+last+2*timeMet) >= timeMet:
                    faze+=1
            elif faze == 3:
                screen.blit(warn2, (coordx, coordy))
                screen.blit(warn2, (coordx1, coordy1))
                screen.blit(warn2, (coordx2, coordy2))

                if end_time - (start_timer+last+3*timeMet) >= timeMet:
                    faze+=1
            elif faze == 4:
                screen.blit(warn1, (coordx, coordy))
                screen.blit(warn1, (coordx1, coordy1))
                screen.blit(warn1, (coordx2, coordy2))

                if end_time - (start_timer+last+4*timeMet) >= timePreMet:
                    faze += 1
            elif faze == 5:
                screen.blit(warn1, (coordx, coordy))
                screen.blit(warn1, (coordx1, coordy1))
                screen.blit(warn1, (coordx2, coordy2))

                if end_time - (start_timer+last+4*timeMet+timePreMet) >= timePreMet:
                    faze += 1
            elif faze == 6:
                screen.blit(warn1, (coordx, coordy))
                screen.blit(warn1, (coordx2, coordy2))
                screen.blit(warn1, (coordx1, coordy1))
                if end_time - (start_timer + last + 4 * timeMet + 2*timePreMet) >= timePreMet:
                    coordx = random.randrange(100, 700)
                    coordy = random.randrange(100, 700)
                    coordx1 = random.randrange(100, 700)
                    coordy1 = random.randrange(100, 700)
                    faze = 1
                    last = last + 4 * timeMet + 2*timePreMet
                    if timeMet >= 0.3:
                        timeMet -=0.1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
                # game_score = game_score
                # local_time = local_time
                # scene_over_showdown(game_score, local_time)
                # print('gg')
        # button = pygame.key.get_pressed()
        # if button[pygame.K_UP] or button[pygame.K_w]:
        #     brawlerR.y -= brawlerSpeed
        # elif button[pygame.K_RIGHT] or button[pygame.K_d]:
        #     brawlerR.x += brawlerSpeed
        # elif button[pygame.K_LEFT] or button[pygame.K_a]:
        #     brawlerR.x -= brawlerSpeed
        # elif button[pygame.K_DOWN] or button[pygame.K_s]:
        #     brawlerR.y += brawlerSpeed

        clock.tick(FPS)
        pygame.display.update()

def scene_game_showdown(brawler):
    screen.blit(search_bg, (0, 0))
    pygame.display.update()
    sound1.stop()
    sound2.stop()
    sound3.stop()
    sound4.stop()
    search_sound.play()
    time.sleep(2)
    banka_x = random.randrange(50, 950)
    banka_y = random.randrange(50, 950)
    notall = [0, 1150]

    start_time = time.time()
    speed = 10
    sec = 2
    game_score = 0
    gerx = 0
    posdx = 1150
    gery = 0
    posdy = 1150
    gerx1 = 0
    posdx1 = 1150
    gery1 = 0
    posdy1 = 1150
    gerx2 = 0
    posdx2 = 1150
    gery2 = 0
    posdy2 = 1150
    xory = random.randrange(0, 2)
    xory1 = random.randrange(0, 2)
    xory2 = random.randrange(0, 2)
    brawlerR = brawler.find_rect()
    try:
        brawlerP = brawler.find_brawler()
    except:
        brawlerP = brawler.find_skin()

    brawlerHealth = int(brawler.find_health())
    brawlerSpeed = brawler.find_speed()
    xheard = 300
    xheard1 = 360
    xheard2 = 420
    xheard3 = 470
    xheard4 = 520
    yheard = 40
    if xory == 0:
        x = int(random.choice(notall))
        y = random.randrange(1, 900)
    else:
        y = int(random.choice(notall))
        x = random.randrange(1, 900)
    if xory1 == 0:
        x1 = int(random.choice(notall))
        y1 = random.randrange(1, 900)
    else:
        y1 = int(random.choice(notall))
        x1 = random.randrange(1, 900)
    if xory2 == 0:
        x2 = int(random.choice(notall))
        y2 = random.randrange(1, 900)
    else:
        y2 = int(random.choice(notall))
        x2 = random.randrange(1, 900)
    running = True
    while running:
        end_time = time.time()
        screen.blit(map, (-10, -10))
        screen.blit(brawlerP, (brawlerR))
        screen.blit(boolet, (x, y))
        screen.blit(boolet, (x1, y1))
        screen.blit(boolet, (x2, y2))

        local_time = int(end_time - start_time)
        screen.blit(banka, (banka_x, banka_y))
        title_text = Label(20, 50, 180, 65, title_rect_color, 20)
        title_text.set_text('Время: ' + str(local_time), 25, WHITE)
        title_text.draw(15, 15)

        score = Label(800, 50, 180, 65, title_rect_color, 20)
        score.set_text('Счёт: ' + str(game_score), 25, WHITE)
        score.draw(25, 15)
        if local_time == sec:
            print(sec)
            sec += 2
            screen.blit(banka, (banka_x, banka_y))
            banka_x = random.randrange(50, 950)
            banka_y = random.randrange(50, 950)

        if brawlerR.collidepoint(banka_x, banka_y):
            game_score += 1
            banka_x = 10000
        elif brawlerR.collidepoint(x, y):
            gerx = 0
            gery = 0
            posdx = 1150
            posdy = 1150
            xory = random.randrange(0, 2)
            if xory == 0:
                x = int(random.choice(notall))
                y = random.randrange(1, 900)
            else:
                y = int(random.choice(notall))
                x = random.randrange(1, 900)

            brawlerHealth -= 1
        elif brawlerR.collidepoint(x1, y1):
            gerx1 = 0
            gery1 = 0
            posdx1 = 1150
            posdy1 = 1150
            xory1 = random.randrange(0, 2)
            if xory1 == 0:
                x1 = int(random.choice(notall))
                y1 = random.randrange(1, 900)
            else:
                y1 = int(random.choice(notall))
                x1 = random.randrange(1, 900)

            brawlerHealth -= 1
        elif brawlerR.collidepoint(x2, y2):
            gerx2 = 0
            gery2 = 0
            posdx2 = 1150
            posdy2 = 1150
            xory2 = random.randrange(0, 2)
            if xory2 == 0:
                x2 = int(random.choice(notall))
                y2 = random.randrange(1, 900)
            else:
                y2 = int(random.choice(notall))
                x2 = random.randrange(1, 900)

            brawlerHealth -= 1
        if xory == 0:
            # print(x,y,'0')
            if x == gerx:
                x += speed
                gerx += speed
            elif x == posdx:
                print(posdx, 'ger')
                x -= speed
                posdx -= speed
        elif xory == 1:
            # print(x,y,'1')
            if y == gery:
                y += speed
                gery += speed
            elif y == posdy:
                print(posdy, 'ger')
                y -= speed
                posdy -= speed
        if gerx == 1100:
            xory = random.randrange(0, 2)
            if xory == 0:
                x = int(random.choice(notall))
                y = random.randrange(1, 900)
            else:
                y = int(random.choice(notall))
                x = random.randrange(1, 900)
        if gery == 1100:
            xory = random.randrange(0, 1)
            if xory == 0:
                x = int(random.choice(notall))
                y = random.randrange(1, 900)
            else:
                y = int(random.choice(notall))
                x = random.randrange(1, 900)
        if posdx == -100:
            xory = random.randrange(0, 2)
            if xory == 0:
                x = int(random.choice(notall))
                y = random.randrange(1, 900)
            else:
                y = int(random.choice(notall))
                x = random.randrange(1, 900)
        if posdy == -100:
            xory = random.randrange(0, 1)
            if xory == 0:
                x = int(random.choice(notall))
                y = random.randrange(1, 900)
            else:
                y = int(random.choice(notall))
                x = random.randrange(1, 900)
        if gerx == 1100:
            gerx = 0
            gery = 0
            posdx = 1150
            posdy = 1150

        elif gery == 1100:
            gerx = 0
            gery = 0
            posdx = 1150
            posdy = 1150

        elif posdx == -100:
            gerx = 0
            gery = 0
            posdx = 1150
            posdy = 1150

        elif posdy == -100:
            gerx = 0
            gery = 0
            posdx = 1150
            posdy = 1150
        if xory1 == 0:
            # print(x,y,'0')
            if x1 == gerx1:
                x1 += speed
                gerx1 += speed
            elif x1 == posdx1:
                print(posdx1, 'ger')
                x1 -= speed
                posdx1 -= speed
        elif xory1 == 1:
            # print(x,y,'1')
            if y1 == gery1:
                y1 += speed
                gery1 += speed
            elif y1 == posdy1:
                print(posdy1, 'ger')
                y1 -= speed
                posdy1 -= speed
        if gerx1 == 1100:
            xory1 = random.randrange(0, 2)
            if xory1 == 0:
                x1 = int(random.choice(notall))
                y1 = random.randrange(1, 900)
            else:
                y1 = int(random.choice(notall))
                x1 = random.randrange(1, 900)
        if gery1 == 1100:
            xory1 = random.randrange(0, 1)
            if xory1 == 0:
                x1 = int(random.choice(notall))
                y1 = random.randrange(1, 900)
            else:
                y1 = int(random.choice(notall))
                x1 = random.randrange(1, 900)
        if posdx1 == -100:
            xory1 = random.randrange(0, 2)
            if xory1 == 0:
                x1 = int(random.choice(notall))
                y1 = random.randrange(1, 900)
            else:
                y1 = int(random.choice(notall))
                x1 = random.randrange(1, 900)
        if posdy1 == -100:
            xory1 = random.randrange(0, 1)
            if xory1 == 0:
                x1 = int(random.choice(notall))
                y1 = random.randrange(1, 900)
            else:
                y1 = int(random.choice(notall))
                x1 = random.randrange(1, 900)
        if gerx1 == 1100:
            gerx1 = 0
            gery1 = 0
            posdx1 = 1150
            posdy1 = 1150

        elif gery1 == 1100:
            gerx1 = 0
            gery1 = 0
            posdx1 = 1150
            posdy1 = 1150

        elif posdx1 == -100:
            gerx1 = 0
            gery1 = 0
            posdx1 = 1150
            posdy1 = 1150

        elif posdy1 == -100:
            gerx1 = 0
            gery1 = 0
            posdx1 = 1150
            posdy1 = 1150

        if xory2 == 0:
            # print(x,y,'0')
            if x2 == gerx2:
                x2 += speed
                gerx2 += speed
            elif x2 == posdx2:
                print(posdx2, 'ger')
                x2 -= speed
                posdx2 -= speed
        elif xory2 == 1:
            # print(x,y,'1')
            if y2 == gery2:
                y2 += speed
                gery2 += speed
            elif y2 == posdy2:
                print(posdy2, 'ger')
                y2 -= speed
                posdy2 -= speed
        if gerx2 == 1100:
            xory2 = random.randrange(0, 2)
            if xory2 == 0:
                x2 = int(random.choice(notall))
                y2 = random.randrange(1, 900)
            else:
                y2 = int(random.choice(notall))
                x2 = random.randrange(1, 900)
        if gery2 == 1100:
            xory2 = random.randrange(0, 1)
            if xory2 == 0:
                x2 = int(random.choice(notall))
                y2 = random.randrange(1, 900)
            else:
                y2 = int(random.choice(notall))
                x2 = random.randrange(1, 900)
        if posdx2 == -100:
            xory2 = random.randrange(0, 2)
            if xory2 == 0:
                x2 = int(random.choice(notall))
                y2 = random.randrange(1, 900)
            else:
                y2 = int(random.choice(notall))
                x2 = random.randrange(1, 900)
        if posdy2 == -100:
            xory2 = random.randrange(0, 1)
            if xory2 == 0:
                x2 = int(random.choice(notall))
                y2 = random.randrange(1, 900)
            else:
                y2 = int(random.choice(notall))
                x2 = random.randrange(1, 900)
        if gerx2 == 1100:
            gerx2 = 0
            gery2 = 0
            posdx2 = 1150
            posdy2 = 1150

        elif gery2 == 1100:
            gerx2 = 0
            gery2 = 0
            posdx2 = 1150
            posdy2 = 1150

        elif posdx2 == -100:
            gerx2 = 0
            gery2 = 0
            posdx2 = 1150
            posdy2 = 1150

        elif posdy2 == -100:
            gerx2 = 0
            gery2 = 0
            posdx2 = 1150
            posdy2 = 1150

        if brawlerR.y < 0:
            brawlerR.y = 0
        elif brawlerR.x < 0:
            brawlerR.x = 0
        elif brawlerR.y > HEIGHT - brawlerR.height:
            brawlerR.y = HEIGHT - brawlerR.height
        elif brawlerR.x > WIDTH - brawlerR.height:
            brawlerR.x = WIDTH - brawlerR.height
        if brawlerHealth == 5:
            screen.blit(heart, (xheard, yheard))
            screen.blit(heart, (xheard1, yheard))
            screen.blit(heart, (xheard2, yheard))
            screen.blit(heart, (xheard3, yheard))
            screen.blit(heart, (xheard4, yheard))
        elif brawlerHealth == 4:
            screen.blit(heart, (xheard, yheard))
            screen.blit(heart, (xheard1, yheard))
            screen.blit(heart, (xheard2, yheard))
            screen.blit(heart, (xheard3, yheard))
        elif brawlerHealth == 3:
            screen.blit(heart, (xheard, yheard))
            screen.blit(heart, (xheard1, yheard))
            screen.blit(heart, (xheard2, yheard))
        elif brawlerHealth == 2:
            screen.blit(heart, (xheard, yheard))
            screen.blit(heart, (xheard1, yheard))
        elif brawlerHealth == 1:
            screen.blit(heart, (xheard, yheard))
        elif brawlerHealth == 0:
            running = False
            game_score = game_score
            local_time = local_time
            print(game_score, local_time)
            scene_over_showdown(brawler, game_score, local_time)

        # Ввод процесса (события)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                write(listB, 'tests.json')
                # game_score = game_score
                # local_time = local_time
                # scene_over_showdown(game_score, local_time)
                # print('gg')
        button = pygame.key.get_pressed()
        if button[pygame.K_UP] or button[pygame.K_w]:
            brawlerR.y -= brawlerSpeed
        elif button[pygame.K_RIGHT] or button[pygame.K_d]:
            brawlerR.x += brawlerSpeed
        elif button[pygame.K_LEFT] or button[pygame.K_a]:
            brawlerR.x -= brawlerSpeed
        elif button[pygame.K_DOWN] or button[pygame.K_s]:
            brawlerR.y += brawlerSpeed

        clock.tick(FPS)
        pygame.display.update()


scene_main(0, 1)
pygame.quit()
