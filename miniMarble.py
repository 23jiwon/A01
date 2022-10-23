import time
from threading import Timer
import threading
import os
import re
import random

# 로그인시 얻은 아이디 변수
global id_1
global id_2
global id_3
global id_4
id_1 = ''
id_2 = ''
id_3 = ''
id_4 = ''
global id_list
global login_status
id_list = [id_1, id_2, id_3, id_4]

# 타이머
global sec
sec = 15

# 'map.txt'에서 불러온 배열

# 5.2.2. 맵 배열
global default_map_name
default_map_name = ['start', '타이베이', '베이징', '마닐라', '제주', 'island', '아테네', '코펜하겐', '오타와', '상파울로', 'festival', '프라하', '베를린', '모스크바', '제네바', 'airport', '런던', '파리', '뉴욕', '건국대']
# 5.2.3.1. 기본 통행료 배열
global default_fee
default_fee = [0, 500, 500, 500, 500, 0, 1000, 1000, 1000, 1000, 0, 1500, 1500, 1500, 1500, 0, 2000, 2000, 2000, 2000]
# 5.2.3.2. 인수가 배열
global takeover_fee
takeover_fee = [0, 500, 500, 500, 500, 0, 1000, 1000, 1000, 1000, 0, 1500, 1500, 1500, 1500, 0, 2000, 2000, 2000, 2000]
# 5.2.3.3. 매매가 배열
global trading_fee
trading_fee = [0, 500, 500, 500, 500, 0, 1000, 1000, 1000, 1000, 0, 1500, 1500, 1500, 1500, 0, 2000, 2000, 2000, 2000]


# 'log-〈방장아이디〉-map.txt'로 출력할 배열
# 6.1.1. 플레이어 수
global login_count
login_count = 0
login_status = False
# 6.1.2. 플레이어 정보 playerID, cash, property, status
global id_1_info
global id_2_info
global id_3_info
global id_4_info
id_1_info = [id_1,10000,10000,0]
id_2_info = [id_2,10000,10000,0]
id_3_info = [id_3,10000,10000,0]
id_4_info = [id_4,10000,10000,0]
# id info 이차원 배열
global id_info_list
id_info_list = [id_1_info,id_2_info,id_3_info,id_4_info]



# 6.1.3. 페스티벌 변수
global now_festival
now_festival = -1
# 6.1.4. 소유주 문자열 배열
global owner_list
owner_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 6.1.5. 랜드마크 문자열 배열
global landmark_list
landmark_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 6.2 활동로그에서 쓸 거 같은 변수
# 현재 턴수
global now_turn
now_turn = 0
# 현재 차례
global now_order
now_order = 0
# 플레이어 출발지 번호 (현재위치)
global player_start_location
player_start_location = [0, 0, 0, 0]
# 플레이어 도착지 번호
global player_end_location
player_end_location = [-1, -1, -1, -1]

# 프로그램 내부에서 만든 배열

# 건물 배열
global build_list
build_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# 현재 통행료 배열
global now_fee
now_fee = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
# 건물 출력용 배열
global now_building
now_building = ['━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ','━ ']
# 말 출력용 배열
global now_location
now_location = ['            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ','            ']
# 출력용 건물명 배열
global print_map_name
print_map_name = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
# 출력용 통행료 배열
global print_fee
print_fee = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

# 플레이어 색상 지정
global color_0
global color_1
global color_2
global color_3
global color_4
global color_fes
color_0 = '\033[0m'
color_1 = '\033[91m'
color_2 = '\033[92m'
color_3 = '\033[93m'
color_4 = '\033[94m'
color_fes = '\033[95m'

# 플레이어가 입력한 값
global player_input
player_input = [None]


global islandPlayer
islandPlayer = [0,0,0,0]

global is_double
is_double = 0

global landing_owner
landing_owner = None

global rank_list
rank_list = []
global rank_money_list
rank_money_list = []

global salary
salary = 10000

# ============================================================================================================
# 
#                              게임 시작 부분 / 회원가입 / 로그인 / 그만두기
# 
# ============================================================================================================


def menu():
    global id_1
    global id_2
    global id_3
    global id_4
    global login_count
    global login_status
    global id_list
    d = open('member.txt','a')
    d.close()
    while login_status == False:
        os.system('cls')
        print('====== 메인 창입니다 ======')
        print('원하는 메뉴를 골라 주세요')
        print('  register/login/quit')
        print('===============================')
        print()
        a = input("userID > ")
        if a == 'quit' or a == '종료' or a == 'q' or a == 'ㅈㄹ' or a == 'exit' or a == '나가기':
            print('====== 미니 마블 게임을 종료합니다 ======')
            time.sleep(3)
            return 0
        elif a == 'register' or a == '회원가입' or a == 'regi' or a == '가입' or a == 'r' or a == 'ㄱㅇ':
            register()
        elif a == 'login' or a == '로그인' or a == 'log' or a == '로긴' or a == 'l' or a == 'ㄹㄱㅇ':
            login()
            if login_status == True:
                print('어서오세요.')
                print(id_1 + ' 님이 접속하셨습니다.')
                print(id_2 + ' 님이 접속하셨습니다.')
                id_list.append(id_1)
                id_list.append(id_2)
                if login_count >= 3:
                    print(id_3 + ' 님이 접속하셨습니다.')
                    id_list.append(id_3)
                    if login_count == 4:
                        print(id_4 + ' 님이 접속하셨습니다.')
                        id_list.append(id_4)
                
                print()
                print('====== 게임을 시작합니다 ======')
                # 여기서부터 게임 파트
        else:
            print('[Error]: 명령어가 올바르지 않습니다. 다시 입력해 주세요.')
            time.sleep(1)
            menu()

def register():
    id_status = False
    pw_status = False
    select_status = False
    
    print('====== 회원가입 창입니다 ======')
    print('아이디와 비밀번호는 각각 6byte~16byte의 길이로 제한되며')
    print('영어 대소문자, 숫자만 입력할 수 있습니다')
    print('아이디를 입력하려면 id 입력할 아이디')
    print('비밀번호를 입력하려면 pw 입력할 비밀번호')
    print('전 화면으로 돌아가려면 back을 입력해 주세요')
    print('===============================')
    print()
    
    while select_status == False:
        a = input("userID > ")
        b = a.split()
        if b[0] == 'id' or b[0] == '아이디' or b[0] == 'i' or b[0] == '아디': 
            if len(b) >= 2:
                userid = input_id(b[1])
            else:
                print('[Error]: 회원가입 id 입력 조건에서 벗어납니다. 다시 id를 입력해 주세요.')
                continue
            if userid == '0':
                id_status = False
            else:
                id_status = True
                print('아이디가 정상 입력되었습니다')
                print('현재 아이디: ' + userid)
                
        elif b[0] == 'pw' or b[0] == '비밀번호' or b[0] == 'p' or b[0] =='비번':
            if len(b) >= 2:
                userpw = input_pw(b[1])
            else:
                print('[Error]: 회원가입 pw 입력 조건에서 벗어납니다. 다시 pw를 입력해 주세요.')
                continue
            if userpw == '0':
                pw_status = False
            else:
                pw_status = True
                print('비밀번호가 정상 입력되었습니다')
                print('현재 비밀번호: ' + userpw)
                
        elif b[0] == 'select':
            if id_status == True and pw_status == True:
                f = open('member.txt', 'a', encoding = 'utf-8')
                f.write(' ' + userid + ' ' + userpw + '\n')
                f.close()
                print('====== id: ' + userid + ' pw: ' + userpw + ' 회원가입 완료 ======')
                print()
                return
            else:
                print('[Error]: 아이디와 비밀번호를 정상적으로 입력 후 다시 select를 입력해 주세요')
                
        elif b[0] == 'back' or b[0] == '뒤로가기' or b[0] == 'b' or b[0] == 'ㄷㄹㄱㄱ':
            return
        else:
            print('[Error]: 명령어를 잘못 입력하셨습니다. 다시 입력해 주세요.')
            
        if id_status == True and pw_status == True and (b[0] == 'id' or b[0] == 'pw'):
            print('아이디와 비밀번호가 정상적으로 입력되었습니다')
            print('이대로 결정하시려면 select를 입력해 주세요')
            print('만약 아이디와 비밀번호를 변경하고 싶다면 다시 id, pw 명령어를 사용해 주세요')

    
        
def input_id(i):
    c = list(i)
    if len(i) >= 6 and len(i) <= 16:
        for d in c:
            e = ord(d)
            if e >= 48 and e <= 57:
                continue
            elif e >= 65 and e <= 90:
                continue
            elif e >= 97 and e <= 122:
                continue
            else: 
                print('[Error]: 회원가입 id 입력 조건에서 벗어납니다. 다시 id를 입력해 주세요.')
                return '0'
    else:
        print('[Error]: 회원가입 id 입력 조건에서 벗어납니다. id 길이가 짧습니다. 다시 id를 입력해 주세요.')
        return '0'
    
    with open('member.txt') as file:
        datafile = file.readlines()
            
        for line in datafile:
            i_index = line.find(' ' + i + ' ')
            if i_index >= 0:
                print('[Error]: 이미 존재하는 아이디입니다. 다른 아이디를 입력해주세요.')
                return '0'
            
    print('====== 올바른 id: ' + i + '을 입력하였습니다. ======')
    print()
    return i
        
                
def input_pw(p):
    c = list(p)
    if len(p) >= 6 and len(p) <= 16:
        for d in c:
            e = ord(d)
            if e >= 48 and e <= 57:
                continue
            elif e >= 65 and e <= 90:
                continue
            elif e >= 97 and e <= 122:
                continue
            else: 
                print('[Error]: 회원가입 pw 입력 조건에서 벗어납니다. 다시 pw를 입력해 주세요.')
                return '0'
    else:
        print('[Error]: 회원가입 pw 입력 조건에서 벗어납니다. 다시 pw를 입력해 주세요.')
        return '0'
    print('====== 올바른 pw: ' + p + '을 입력하였습니다. ======')
    print()
    return p


def login():
    global id_1
    global id_2
    global id_3
    global id_4
    global id_1_info
    global id_2_info
    global id_3_info
    global id_4_info
    global id_info_list
    global id_list
    global login_count
    global login_status
    
    login_count = 0
    login_status = False
    print('게임에 참가할 인원수를 입력해주세요. 게임은 2~4인이 함께 즐길 수 있습니다.')
    a = input('userID > ')
    if a == 'back' or a == '뒤로가기' or a == 'b' or a == 'ㄷㄹㄱㄱ':
        return
    z = a[0]
    
    while not (len(a) == 1 and ord(z) >= 50 and ord(z) <= 52):
        print('[Error]: 인자에 숫자 이외의 글자 혹은 2~4를 제외한 숫자를 입력했습니다. 숫자를 입력해주세요.')
        print()
        print('게임에 참가할 인원수를 입력해주세요.')
        a = input('userID > ')
        z = a[0]

    print(a + '명의 id와 pw를 입력받습니다. (입력형식: login <아이디> <비밀번호>)')

    while True:
        id_status = False
        already_login_status = 0 # 중복 로그인 방지
        b = input('userID > ')
        if b == 'back' or b == '뒤로가기' or b == 'b' or b == 'ㄷㄹㄱㄱ':
            id_1 = ' '
            id_2 = ' '
            id_3 = ' '
            return
        c = b.split()

        
        while not (len(c) == 3):
            if len(c) > 3:
                print('[Error]: 인자의 개수가 많습니다. 2개의 인자를 입력해주세요.')
            elif len(c) < 3:
                print('[Error]: 인자의 개수가 적습니다. 2개의 인자를 입력해주세요.')
            print()
            print(a + '명의 id와 pw를 입력받습니다.')
            b = input('userID > ')
            if b == 'back' or b == '뒤로가기' or b == 'b' or b == 'ㄷㄹㄱㄱ':
                id_1 = ' '
                id_2 = ' '
                id_3 = ' '
                return
            c = b.split()

        if c[0] == 'login' or c[0] == '로그인' or c[0] == 'log' or c[0] == '로긴' or c[0] == 'l' or c[0] == 'ㄹㄱㅇ':   
            with open('member.txt') as file:
                datafile = file.readlines()
                c = b.split()

                for line in datafile:
                    i_index = line.find(' ' + c[1] + ' ')
                    if i_index >= 0:
                        f_list = line.split()
                        pw = f_list[1]
                        if pw == c[2]:
                            if c[1] == id_1:
                                print('[Error]: 이미 접속 중인 id입니다. 다시 입력해 주세요.')
                                already_login_status = 1
                            elif c[1] == id_2:
                                print('[Error]: 이미 접속 중인 id입니다. 다시 입력해 주세요.')                                    
                                already_login_status = 1
                            elif c[1] == id_3:
                                print('[Error]: 이미 접속 중인 id입니다. 다시 입력해 주세요.')
                                already_login_status = 1
                            else:
                                print('====== 유저: ' + c[1] + ' 님 로그인 완료 ======')
                                login_count += 1
                                print(str(login_count) + '명째 로그인 중')
                                pw_status = True
                                if login_count == 1:
                                    id_1 = c[1]
                                elif login_count == 2:
                                    id_2 = c[1]
                                elif login_count == 3:
                                    id_3 = c[1]
                                elif login_count == 4:
                                    id_4 = c[1]
                                id_status = True
                                already_login_status = 2
                if login_count == int(a):
                    break
                if already_login_status == 0:
                    print('[Error]: 데이터베이스에 없는 회원정보입니다. id나 pw를 다시 확인해주세요.')
        else:
            print('[Error]: 명령어를 잘못 입력하셨습니다. 다시 입력해 주세요.')

    print('===== 유저 ' + str(login_count) + '명 로그인 완료 ======')
    print()    
    id_list = [id_1, id_2, id_3, id_4]
    id_1_info = [id_1,10000,10000,0]
    id_2_info = [id_2,10000,10000,0]
    id_3_info = [id_3,10000,10000,0]
    id_4_info = [id_4,10000,10000,0]
    id_info_list = [id_1_info,id_2_info,id_3_info,id_4_info]
    login_status = True
    return


# ============================================================================================================
# 
#                              게임 시작 부분 / 회원가입 / 로그인 / 그만두기 끝.
# 
# ============================================================================================================
# 
#                                      사용자 입력 값 판단 / 읽어오기.
# 
# ============================================================================================================
# 입력값 판단하는 함수
def input_check(require, p_input):
    match p_input:
        case 'r'|'roll'|'ㅈㅅㅇ'|'주사위':
            if(require == 'roll'):        
                return True
            else:
                return False
        case 'yes'|'네'|'예'|'ㅇ'|'ㅇㅇ'|'o'|'y':
            if(require == 'yes'):        
                return True
            else:
                return False
        case 'no'|'아니오'|'아니요'|'ㄴ'|'ㄴㄴ'|'x'|'n':
            if(require == 'no'):        
                return True
            else:
                return False
        case 'cr'|'커'|'croll'|'ㅋㅈ':
            if(require == 'roll'):        
                return 2
            else:
                return False
        case _:
            return False

# 입력한 도시 소유 판단하는 함수
def judge_own_city_name(city_name):
    global now_order
    global owner_list
    global default_map_name
    global id_list
    global player_input
    try:
        city_num = int(city_name)
        if city_num <= 0 or city_num > 20 or city_num == 5 or city_num == 10 or city_num == 15 or float(city_name) - city_num != 0:
            print('[Error]: 유효하지 않은 도시번호입니다. 특수지역을 제외한 0이상 19이하의 정수를 입력해주세요.')
            player_input=[None]
            return False
        if owner_list[city_num] != id_list[now_order]:
            print('===== ' + default_map_name[city_num] + ' 도시를 보유하고 있지 않습니다! =====')
            player_input=[None]
            return False
        else:
            return city_num
    except:
        for i in range(20):
            if city_name == default_map_name[i]:
                if owner_list[i] != id_list[now_order]: 
                    return False
                else:
                    return i

        if city_name == '출발점' or city_name == '무인도' or city_name == '축제위원회' or city_name == '공항':
            print('[Error]: 특수지역을 제외한 도시를 입력해주세요.')
            return False

        #맵 배열을 다 뒤져봐도 나오지 않음
        print('[Error]: 입력한 도시는 존재하지 않는 도시입니다.')
        player_input=[None]
        return False

# 입력한 도시 판단하는 함수
def judge_city_name(city_name):
    global now_order
    global owner_list
    global default_map_name
    global id_list
    global player_input
    try:
        city_num = int(city_name)
        if city_num < 0 or city_num > 20 or float(city_name) - city_num != 0:
            print('[Error]: 유효하지 않은 도시번호입니다. 0이상 19이하의 정수를 입력해주세요.')
            player_input=[None]
            return False
        else:

            if city_num == 0:
                return -1
            else:
                return city_num
    except:
        for i in range(20):
            if city_name == default_map_name[i]:
                if i == 0:
                    return -1
                return i
        if city_name == '출발점':
            return -1
        elif city_name == '무인도':
            return 5
        elif city_name == '축제위원회':
            return 10
        elif city_name == '공항':
            return 15
        #맵 배열을 다 뒤져봐도 나오지 않음
        print('[Error]: 입력한 도시는 존재하지 않는 도시입니다.')
        player_input=[None]
        return False

def get_player_input(player_input_ref):
    global now_order
    global id_list
    player_input_ref[0] = input(id_list[now_order] + ' > ')

      
# 제한시간 내에 사용자 명령 받는 함수 (left_time : 제한시간, require_msg : 입력받아야하는 명령어)
def input_timer(left_time, require_msg):
    global player_input
    global now_order
    global id_list
    global id_info_list
    global now_festival
    global print_map_name
    global trading_fee
    global salary
    player_input=[None]
    i_timer= threading.Thread(target=get_player_input, args=(player_input,))
    i_timer.daemon = True
    i_timer.start()  

    for i in range(left_time * 2):
        inputcheck = input_check(require_msg, player_input[0])
        if inputcheck == 1:
            return True
        elif inputcheck == 2:
            return 2
        elif player_input[0] != None:
            b_res = 0
            if re.search(' ' , player_input[0]) != None:
                b_res = 1
            if(player_input[0].isspace() or player_input[0]==''): 
                # 입력에 공백만 있다면
                print('[Error]: 인자의 개수가 적습니다. 1개의 인자를 입력해주세요.')
            elif(b_res):
                #문자열 사이에 공백이 있다면
                print('[Error]: 인자의 개수가 많습니다. 1개의 인자를 입력해주세요.')
            if require_msg == 'roll':
                print('[Error]: 주사위 굴리기 명령어를 입력해주세요.')
                player_input=[None]
                i_timer= threading.Thread(target=get_player_input, args=(player_input,))
                i_timer.daemon = True
                i_timer.start() 
            elif require_msg == 'festival':
                city_num = judge_own_city_name(player_input[0])
                if city_num != False:                 
                    print('===== ' + print_map_name[city_num].rstrip()  + ' 도시에서 축제를 시작합니다! =====')  
                    now_festival = city_num
                    time.sleep(1)
                    return True
                else:
                    print('[Error]:축제를 개최할 도시명 또는 도시번호를 입력하세요.')

                    player_input=[None]
                    i_timer= threading.Thread(target=get_player_input, args=(player_input,))
                    i_timer.daemon = True
                    i_timer.start() 
            elif require_msg == 'trip':
                city_num = judge_city_name(player_input[0])
                if city_num != False:
                    if city_num == 15:
                        print('===== 이미 공항 도시에 있습니다. =====')
                        time.sleep(1)
                        return city_num
                    if city_num == -1:
                        city_num = 0
                    print('===== ' + print_map_name[city_num].rstrip()  + '(으)로 이동합니다. =====')
                    if city_num < 15:
                        # 월급지급
                        print('===== 월급을 수령했습니다. =====')
                        id_info_list[now_order][1] += salary
                        id_info_list[now_order][2] += salary

                    player_end_location[now_order] = city_num                    
                    # 활동로그 기록
                    player_start_location[now_order] = player_end_location[now_order]
                    time.sleep(1)
                    return city_num
                else:
                    print('[Error]:여행갈 도시명 또는 도시번호를 입력하세요.')

                    player_input=[None]
                    i_timer= threading.Thread(target=get_player_input, args=(player_input,))
                    i_timer.daemon = True
                    i_timer.start()
            elif require_msg == 'build':
                if input_check('yes', player_input[0]):
                    return 2
                elif input_check('no', player_input[0]):
                    return 3
                else:
                    print('[Error]:yes 또는 no를 입력하세요')
                    player_input=[None]
                    i_timer= threading.Thread(target=get_player_input, args=(player_input,))
                    i_timer.daemon = True
                    i_timer.start()
            elif require_msg == 'sell':
                city_num = judge_own_city_name(player_input[0])
                if city_num != False:
                    return city_num
                else:
                    print('[Error]:도시명 또는 도시번호를 입력하세요.')
                    player_input=[None]
                    i_timer= threading.Thread(target=get_player_input, args=(player_input,))
                    i_timer.daemon = True
                    i_timer.start()
            elif require_msg == 'takeover':
                if input_check('yes', player_input[0]):
                    return 2
                elif input_check('no', player_input[0]):
                    return 3
                else:
                    print('[Error]:yes 또는 no를 입력하세요.')
                    player_input=[None]
                    i_timer= threading.Thread(target=get_player_input, args=(player_input,))
                    i_timer.daemon = True
                    i_timer.start()
            else:
                print('[Error]:입력이 틀렸습니다. 다시 입력하세요.')
                player_input = [None]
                i_timer= threading.Thread(target=get_player_input, args=(player_input,))
                i_timer.daemon = True
                i_timer.start()  
        time.sleep(0.5)

        
    if player_input[0] == None:
        print('\n===== %d초가 지났습니다. =====' % left_time)
        if(left_time == 10):
            bankruptcy(1)
        else:
            warning()
        print('===== enter를 입력하시면 다음 차례로 넘어갑니다. =====')
        while player_input[0] == None:
            if player_input[0] != None:
                player_input = [None]
                break
        return False
    return False




# 파산      
def bankruptcy(dice = 0):
    global id_info_list
    global now_order
    global owner_list
    global landmark_list
    global build_list
    global now_festival
    global player_input
    global rank_list
    global is_double
    global rank_money_list
    is_double = 0

    for i in range(20):
        if owner_list[i] == id_list[now_order]: 
            owner_list[i] = 0
            build_list[i] = 0
            landmark_list[i] = 0
            if now_festival == i:
                now_festival = -1

    player_start_location[now_order] = -1
    id_info_list[now_order][1] = 0 #재산 0으로 만들어서 파산 시켜버림
    id_info_list[now_order][2] = 0
    
    if dice:
        print('====== '+id_info_list[now_order][0]+'님 주사위를 던지지 않아 중도포기되었습니다 =======')
        
    elif id_info_list[now_order][3] == 2:
        print('====== '+id_info_list[now_order][0]+'님 경고 2회 누적으로 중도포기되었습니다 =======')
    else:
        print('====== '+id_info_list[now_order][0]+'님 파산하였습니다 =======')
    id_info_list[now_order][3] = 2 
    rank_list.append(id_info_list[now_order][0])
    rank_money_list.append(id_info_list[now_order][2])
    time.sleep(2)
            
# 경고, 중도포기
def warning():
    global id_info_list
    global now_order
    global owner_list
    global landmark_list
    if id_info_list[now_order][3] < 2: #경고 세는 부분
        id_info_list[now_order][3] += 1
        print('===== 경고 1회 받았습니다. =====')
        time.sleep(2)
    if id_info_list[now_order][3] == 2:
        bankruptcy()


# ============================================================================================================
# 
#                                      사용자 입력 값 판단 / 읽어오기 끝.
# 
# ============================================================================================================
# 
#                                                  맵 출력부분.
# 
# ============================================================================================================

# 화면상 출력되는 맵 이름 배열 생성
def map_name_space():
    global default_map_name
    global print_map_name
    global now_festival
    global color_0
    global color_fes
    for i in range(20):
        print_map_name[i] = default_map_name[i]
        if i == 0:
            print_map_name[i] = '출발점'
        elif i == 5:
            print_map_name[i] = '무인도'
        elif i == 10:
            print_map_name[i] = '축제위원회'
        elif i == 15:
            print_map_name[i] = '공항'
        
        # 글자수 10칸으로 맞추기위해 공백 추가
        while len(print_map_name[i].encode('cp949')) < 10:
            print_map_name[i] += ' '
        if now_festival == i:
            print_map_name[i] = color_fes + print_map_name[i] + color_0
            
# 건물이나 랜드마크 건설여부 확인하고 출력
def calculate_now_building():
    global id_1
    global id_2
    global id_3
    global id_4
    global color_0
    global color_1
    global color_2
    global color_3
    global color_4
    global owner_list
    global now_building
    global landmark_list  
    for i in range(20):
        if owner_list[i] != 0:
            if owner_list[i] == id_1:
                now_building[i] = color_1
            elif owner_list[i] == id_2:
                now_building[i] = color_2
            elif owner_list[i] == id_3:
                now_building[i] = color_3
            elif owner_list[i] == id_4:
                now_building[i] = color_4              
            if landmark_list[i] == 0:
                now_building[i] += '■'
            elif landmark_list[i] == 1:
                now_building[i] += '▲'
            now_building[i] += color_0
        else:
            now_building[i] =  '━ '

# 현재 통행료 계산
def calculate_now_fee():
    global owner_list
    global now_fee
    global print_fee
    global default_fee
    global now_festival
    for i in range(20):
        if owner_list[i] != 0:
            now_fee[i] = default_fee[i]
            if landmark_list[i] != 0:
                now_fee[i] *= 2
            if now_festival == i:
                now_fee[i] *= 2
        else:
            now_fee[i] = 0
        if now_fee[i] != 0:
            print_fee[i] = str(now_fee[i]) + ' 원'
        else:
            print_fee[i] = ''
        while len(print_fee[i].encode('cp949')) < 10:
            print_fee[i] = ' ' + print_fee[i]

# 플레이어 위치 출력
def location_player():
    global login_count
    global now_location
    for i in range(21):
        temp_location = ''
        if player_start_location[0] == i:
            temp_location += color_1 + '● ' + color_0
        else:
            temp_location += '   '
        if player_start_location[1] == i:
            temp_location += color_2 + '● ' + color_0
        else:
            temp_location += '   '
        if player_start_location[2] == i and login_count > 2:
            temp_location += color_3 + '● ' + color_0
        else:
            temp_location += '   '
        if player_start_location[3] == i and login_count > 3:
            temp_location += color_4 + '● ' + color_0
        else:
            temp_location += '   '
        now_location[i] = temp_location


# 화면상에 맵 출력
def draw_basic_map():
    global login_count
    global color_0
    global color_1
    global color_2
    global color_3
    global color_4
    global now_building
    global print_map_name
    global now_turn
    global now_fee
    global now_location
    global id_list
    global sec
    global player_input
    global id_info_list
    os.system('cls')
    map_name_space()
    location_player()
    calculate_now_fee()
    calculate_now_building()
    print('┏ ┫ 10┣ ━ %s━ ┳ ┫ 11┣ ━ %s━ ┳ ┫ 12┣ ━ %s━ ┳ ┫ 13┣ ━ %s━ ┳ ┫ 14┣ ━ %s━ ┳ ┫ 15┣ ━ %s━ ┓ ' %(now_building[10], now_building[11], now_building[12], now_building[13], now_building[14], now_building[15]))
    print('┃  %s ┃  %s ┃  %s ┃  %s ┃  %s ┃  %s ┃      현재 턴수 %d턴' %(print_map_name[10],print_map_name[11],print_map_name[12],print_map_name[13],print_map_name[14],print_map_name[15],now_turn))
    print('┃  %s ┃  %s ┃  %s ┃  %s ┃  %s ┃  %s ┃ ' %(print_fee[10], print_fee[11], print_fee[12], print_fee[13], print_fee[14], print_fee[15]))
    print('┃ %s┃ %s┃ %s┃ %s┃ %s┃ %s┃     %s 차례 %2d초' % (now_location[10], now_location[11], now_location[12], now_location[13], now_location[14], now_location[15], id_info_list[now_order][0], sec))
    print('┗ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┛')
    print('┏ ┫ 09┣ ━ %s━ ┓                                                       ┏ ┫ 16┣ ━ %s━ ┓ ┏ ┫ 01┣ ━ ━ ━ ━ ━ ━ ┓ '%(now_building[9], now_building[16]))
    if id_info_list[0][3] == 2:
        print('┃  %s ┃                                                       ┃  %s ┃ ┃ \033[31m%-18s\033[0m┃ '%(print_map_name[9],print_map_name[16],id_info_list[0][0]))
    else:
        print('┃  %s ┃                                                       ┃  %s ┃ ┃ %-18s┃ '%(print_map_name[9],print_map_name[16],id_info_list[0][0]))
    print('┃  %s ┃                                                       ┃  %s ┃ ┃ \033[30m전재산%9s 원\033[0m┃ ' %(print_fee[9],print_fee[16],id_info_list[0][2]))
    print('┃ %s┃                                                       ┃ %s┃ ┃ %15s 원┃ ' %(now_location[9], now_location[16],id_info_list[0][1]))
    print('┗ ━ ━ ━ ━ ━ ━ ┛                                                       ┗ ━ ━ ━ ━ ━ ━ ┛ ┗ ┫ '+color_1+'●'+color_0+'┣ ━ ━ ━ ━ ━ ━ ┛ ')
    print('┏ ┫ 08┣ ━ %s━ ┓                                                       ┏ ┫ 17┣ ━ %s━ ┓ ┏ ┫ 02┣ ━ ━ ━ ━ ━ ━ ┓ '%(now_building[8], now_building[17]))
    if id_info_list[1][3] == 2:
        print('┃  %s ┃                                                       ┃  %s ┃ ┃ \033[31m%-18s\033[0m┃ '%(print_map_name[8],print_map_name[17],id_info_list[1][0]))
    else:
        print('┃  %s ┃                                                       ┃  %s ┃ ┃ %-18s┃ '%(print_map_name[8],print_map_name[17],id_info_list[1][0]))
    print('┃  %s ┃                                                       ┃  %s ┃ ┃ \033[30m전재산%9s 원\033[0m┃ ' %(print_fee[8],print_fee[17],id_info_list[1][2]))
    print('┃ %s┃                                                       ┃ %s┃ ┃ %15s 원┃ ' %(now_location[8], now_location[17],id_info_list[1][1]))
    print('┗ ━ ━ ━ ━ ━ ━ ┛                                                       ┗ ━ ━ ━ ━ ━ ━ ┛ ┗ ┫ '+color_2+'●'+color_0+'┣ ━ ━ ━ ━ ━ ━ ┛ ')
    print('┏ ┫ 07┣ ━ %s━ ┓                                                       ┏ ┫ 18┣ ━ %s━ ┓ '%(now_building[7], now_building[18]), end='')
    if login_count > 2:
        print('┏ ┫ 03┣ ━ ━ ━ ━ ━ ━ ┓ ')
    else:
        print('')
    print('┃  %s ┃                                                       ┃  %s ┃ '%(print_map_name[7],print_map_name[18]), end='')
    if login_count > 2:
        if id_info_list[2][3] == 2:
            print('┃ \033[31m%-18s\033[0m┃ ' % id_info_list[2][0])
        else:
            print('┃ %-18s┃ ' % id_info_list[2][0])
    else:
        print('')
    print('┃  %s ┃                                                       ┃  %s ┃ ' %(print_fee[7],print_fee[18]), end='')
    if login_count > 2:
        print('┃ \033[30m전재산%9s 원\033[0m┃ ' % id_info_list[2][2])
    else:
        print('')
    print('┃ %s┃                                                       ┃ %s┃ ' %(now_location[7], now_location[18]), end='')
    if login_count > 2:
        print('┃ %15s 원┃ ' % id_info_list[2][1])
    else:
        print('')
    print('┗ ━ ━ ━ ━ ━ ━ ┛                                                       ┗ ━ ━ ━ ━ ━ ━ ┛ ', end='')
    if login_count > 2:
        print('┗ ┫ '+color_3+'●'+color_0+'┣ ━ ━ ━ ━ ━ ━ ┛ ')
    else:
        print('')
    print('┏ ┫ 06┣ ━ %s━ ┓                                                       ┏ ┫ 19┣ ━ %s━ ┓ '%(now_building[6], now_building[19]), end='')
    if login_count > 3:
          print('┏ ┫ 04┣ ━ ━ ━ ━ ━ ━ ┓ ')
    else:
        print('')
    print('┃  %s ┃                                                       ┃  %s ┃ '%(print_map_name[6],print_map_name[19]), end='')
    if login_count > 3:
        if id_info_list[3][3] == 2:
            print('┃ \033[31m%-18s\033[0m┃ ' % id_info_list[3][0])
        else:
            print('┃ %-18s┃ ' % id_info_list[3][0])
    else:
        print('')
    print('┃  %s ┃                                                       ┃  %s ┃ ' %(print_fee[6],print_fee[19]), end='')
    if login_count > 3:
          print('┃ \033[30m전재산%9s 원\033[0m┃ '% id_info_list[3][2])
    else:
        print('')
    print('┃ %s┃                                                       ┃ %s┃ ' %(now_location[6], now_location[19]), end='')
    if login_count > 3:
          print('┃ %15s 원┃ ' % id_info_list[3][1])
    else:
        print('')
    print('┗ ━ ━ ━ ━ ━ ━ ┛                                                       ┗ ━ ━ ━ ━ ━ ━ ┛ ', end='')
    if login_count == 4:
          print('┗ ┫ '+color_4+'●'+color_0+'┣ ━ ━ ━ ━ ━ ━ ┛ ')
    else:
        print('')
    print('┏ ┫ 05┣ ━ %s━ ┳ ┫ 04┣ ━ %s━ ┳ ┫ 03┣ ━ %s━ ┳ ┫ 02┣ ━ %s━ ┳ ┫ 01┣ ━ %s━ ┳ ┫ 00┣ ━ %s━ ┓ ' %(now_building[5], now_building[4], now_building[3], now_building[2], now_building[1], now_building[0]))
    print('┃  %s ┃  %s ┃  %s ┃  %s ┃  %s ┃  %s ┃ ' %(print_map_name[5],print_map_name[4],print_map_name[3],print_map_name[2],print_map_name[1],print_map_name[0]))
    print('┃  %s ┃  %s ┃  %s ┃  %s ┃  %s ┃  %s ┃ ' %(print_fee[5], print_fee[4], print_fee[3], print_fee[2], print_fee[1], print_fee[0]))
    print('┃ %s┃ %s┃ %s┃ %s┃ %s┃ %s┃ ' % (now_location[5], now_location[4], now_location[3], now_location[2], now_location[1], now_location[0]))
    print('┗ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┻ ━ ━ ━ ━ ━ ━ ┛')

# ============================================================================================================
# 
#                                                  맵 출력부분 끝.
# 
# ============================================================================================================
# 
#                                                   이동, 액션
# 
# ============================================================================================================


# 랜드마크는 인수가 불가능 하기 때문에 가능한 코드
# 랜드마크 함수
def landMark():
    global id_info_list
    global landmark_list
    global owner_list
    global now_order
    global trading_fee
    have_building = 0

    for i in range(20):
        if owner_list[i] == id_info_list[now_order][0] and landmark_list[i] == 0:
            landmark_list[i] = 1
            id_info_list[now_order][2] += trading_fee[i]
            have_building += 1
    if have_building > 0:
        print('===== %d개 지역 랜드마크 건설 완료! =====' % have_building)
    else:
        print('===== 랜드마크로 건설할 건물이 없습니다! =====')

    time.sleep(1)

# 무인도
def island():
    global now_order
    global islandPlayer
    global is_double
    print('===== 무인도에 도착했습니다.. =====')    
    islandPlayer[now_order] = 1
    if is_double == 3:
        player_end_location[now_order] = 5
        # 활동로그파일 기록
        player_start_location[now_order] = player_end_location[now_order]
    is_double = 0

    time.sleep(1)

# 축제 함수
def festival():
    # 보유중인 도시 없으면 넘어가는걸
    global owner_list
    global now_order
    global id_list
    own_any_city = 0
    for i in range (20):
        if owner_list[i] == id_list[now_order]:
            own_any_city += 1
    if own_any_city == 0:
        print('아무 도시도 보유하고 있지 않습니다 ㅠ')
        time.sleep(1)
        return

    print('>> festival?')
    if input_timer(15,'festival'):
        return
        
# 공항 함수
def trip():        
    print('>> trip?')
    landing_num = input_timer(15, 'trip')
    draw_basic_map()
    if landing_num != 15:

        action(landing_num)
        

# 빈 도시 매입
def build(num):
    # 보유중인 도시 없으면 넘어가는걸
    global build_list
    global owner_list
    global id_info_list
    global now_order
    global trading_fee
    if id_info_list[now_order][1] >= trading_fee[num]: #여기서 매매가 설정

        print('>> build?')
        build_flag = input_timer(15,'build')
        if build_flag == 2:
            print("====== 건설을 진행합니다 ======")
            id_info_list[now_order][1] -= trading_fee[num] #돈 지불
            id_info_list[now_order][2] -= trading_fee[num]
            # 건설 진행
            build_list[num] = 1 # 건물 리스트에 추가
            owner_list[num] = id_info_list[now_order][0]            
            id_info_list[now_order][2] += trading_fee[num]
        elif build_flag == 3:
            print("====== 건설을 포기합니다 ======")
    else:
        print("[Error]: 매입을 진행할 돈이 부족합니다. 매입을 포기합니다.")
    time.sleep(1)

def takeover(landing_num,landing_owner):
    global id_info_list
    global takeover_fee
    global landmark_list
    global trading_fee
    if(id_info_list[now_order][1] >= takeover_fee[landing_num]) and landmark_list[landing_num] == 0: #여기서 인수가 설정

        print('>> takeover?')
        takeover_flag = input_timer(15,'takeover')
        if takeover_flag == 2:
            print("====== 인수를 진행합니다 ======")
            id_info_list[now_order][1] -= takeover_fee[landing_num] #자산차감
            id_info_list[now_order][2] -= takeover_fee[landing_num]                
            id_info_list[landing_owner][1] += takeover_fee[landing_num]           
            id_info_list[landing_owner][2] = id_info_list[landing_owner][2] + takeover_fee[landing_num] - trading_fee[landing_num]

            # 인수 진행 액션 코드
            owner_list[landing_num] = id_info_list[now_order][0]
            id_info_list[now_order][2] += trading_fee[landing_num]
        elif takeover_flag == 3:
            print("====== 인수를 포기합니다 ======")
            # 건설 포기 액션 코드
    elif landmark_list[landing_num] == 1:
        print("[Error]: 랜드마크는 인수할 수 없습니다.")
    else:
        print("[Error]: 인수를 진행할 돈이 부족합니다. 인수를 포기합니다.")
    time.sleep(1)
        
def pay_fee(landing_num, all = 0):
    global now_order
    global owner_list    
    global id_info_list
    global now_fee

    global landing_owner
    landing_owner = None
    
    if all == 0:
        id_info_list[now_order][1] -= now_fee[landing_num]
        id_info_list[now_order][2] -= now_fee[landing_num]
        if id_info_list[0][0] == owner_list[landing_num]:
            id_info_list[0][1] += now_fee[landing_num]
            id_info_list[0][2] += now_fee[landing_num]
            landing_owner = 0
        elif id_info_list[1][0] == owner_list[landing_num]:
            id_info_list[1][1] += now_fee[landing_num]
            id_info_list[1][2] += now_fee[landing_num]
            landing_owner = 1
        elif id_info_list[2][0] == owner_list[landing_num]:
            id_info_list[2][1] += now_fee[landing_num]
            id_info_list[2][2] += now_fee[landing_num]
            landing_owner = 2
        elif id_info_list[3][0] == owner_list[landing_num]:
            id_info_list[3][1] += now_fee[landing_num]
            id_info_list[3][2] += now_fee[landing_num]
            landing_owner = 3
        draw_basic_map()
        print('통행료를 지불하였습니다.')
        time.sleep(1)
        takeover(landing_num,landing_owner)
    else:
        if id_info_list[0][0] == owner_list[landing_num]:
            id_info_list[0][1] += id_info_list[now_order][2]
            id_info_list[0][2] += id_info_list[now_order][2]
            landing_owner = 0
        elif id_info_list[1][0] == owner_list[landing_num]:
            id_info_list[1][1] += id_info_list[now_order][2]
            id_info_list[1][2] += id_info_list[now_order][2]
            landing_owner = 1
        elif id_info_list[2][0] == owner_list[landing_num]:
            id_info_list[2][1] += id_info_list[now_order][2]
            id_info_list[2][2] += id_info_list[now_order][2]
            landing_owner = 2
        elif id_info_list[3][0] == owner_list[landing_num]:
            id_info_list[3][1] += id_info_list[now_order][2]
            id_info_list[3][2] += id_info_list[now_order][2]
            landing_owner = 3

    time.sleep(1)
        
def sell_property(sell_num):
    global now_order
    global owner_list    
    global id_info_list
    global now_fee
    global trading_fee
    global default_map_name
    global build_list
    global landmark_list
    global now_festival
    id_info_list[now_order][1] = id_info_list[now_order][1] + trading_fee[sell_num] + (trading_fee[sell_num] * landmark_list[sell_num]) #매각된 땅값을 현금에 포함
    id_info_list[now_order][2] = id_info_list[now_order][2] + trading_fee[sell_num] + (trading_fee[sell_num] * landmark_list[sell_num]) #매각된 땅값을 전재산에 포함
    id_info_list[now_order][2] = id_info_list[now_order][2] -  trading_fee[sell_num] - (trading_fee[sell_num] * landmark_list[sell_num])
    owner_list[sell_num] = 0 #소유지를 무소유로 바꿈
    landmark_list[sell_num] = 0
    build_list[sell_num] = 0
    if now_festival == sell_num:
        now_festival = -1

    draw_basic_map()
    print('===== ' + default_map_name[sell_num] + ' 도시 매각을 진행합니다. =====')
    time.sleep(1)

        
        
        
def action(landing_num):
    global now_order
    global owner_list    
    global id_info_list
    global now_fee
    if landing_num == 0:    # 출발점
        landMark()
    elif landing_num == 5:  # 무인도
        island()
    elif landing_num == 10: # 축제위원회
        festival()
    elif landing_num == 15: # 공항
        trip()
    else:
        if owner_list[landing_num] == 0: # 빈 도시
            build(landing_num)
        elif owner_list[landing_num] != id_info_list[now_order][0]: # 남 도시
            if now_fee[landing_num] <= id_info_list[now_order][1]:
                pay_fee(landing_num)
            elif now_fee[landing_num] <= id_info_list[now_order][2] and now_fee[landing_num] > id_info_list[now_order][1]:
                while True:
                    print('>> 매각하려는 도시를 입력해주세요.')

                    sell_num = input_timer(15,'sell')
                    sell_property(sell_num)
                    if now_fee[landing_num] <= id_info_list[now_order][1]:
                        pay_fee(landing_num)
                        break
                    else:
                        print('===== 현재 현금자산은 '+ str(id_info_list[now_order][1]) + '원 입니다. 자산이 부족하므로 추가 매각을 진행합니다. =====')
                        time.sleep(1)
            else:
                pay_fee(landing_num,1)
                bankruptcy()                

        elif owner_list[landing_num] == id_info_list[now_order][0]:
            print('===== 내 도시라 편안해요~ =====')
            time.sleep(1)
            



def player_move(Dice):
    global now_order
    global now_turn
    global player_start_location
    global player_end_location
    global id_info_list
    global sec
    global salary
    player_end_location[now_order] = player_start_location[now_order] + Dice
    if player_end_location[now_order] >= 20:
        player_end_location[now_order] -= 20
        if player_end_location[now_order] > 0:
            # 월급지급
            print('===== 월급을 수령했습니다. =====')
            id_info_list[now_order][1] += salary
            id_info_list[now_order][2] += salary
    elif now_turn > 1 and player_start_location[now_order] == 0:
        print('===== 월급을 수령했습니다. =====')
        id_info_list[now_order][1] += salary
        id_info_list[now_order][2] += salary
    # 활동로그파일 기록
    player_start_location[now_order] = player_end_location[now_order]
    sec = 15
    time.sleep(1)
    draw_basic_map()
    # 액션
    action(player_start_location[now_order])

#커스텀 주사위
def custom_rollDice():
    firstDice = 0
    secondDice = 0
    global is_double
    global islandPlayer
    global now_order
    while True:
        print('주사위를 굴리세요')
        time.sleep(0.1)
        if input_timer(10,'roll'):
            firstDice = int(input('첫 주사위 :')) #첫번째 주사위
            secondDice = int(input('두번째 주사위 :')) #두번째 주사위
            totalDice = firstDice + secondDice #주사위들의 합         
            if islandPlayer[now_order] == 1:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: ' + str(secondDice) + ' =====')
                print('===== 현재 무인도에 있습니다. 이동하지 않습니다. =====')
                islandPlayer[now_order] = 0
                is_double = 0
                time.sleep(1)
                return 0
            if firstDice != secondDice:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: '+ str(secondDice) + ' =====')
                print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                player_move(totalDice)
                is_double = 0
                return True
            else:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: '+ str(secondDice) + ' =====')
                is_double += 1
                if is_double == 1:
                    print('===== 첫번째 더블! =====')
                    print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                    player_move(totalDice)
                    return True
                elif is_double == 2:
                    print('===== 두번째 더블! =====')
                    print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                    player_move(totalDice)
                    return True
                elif is_double == 3:
                    print('===== 세번째 더블! =====')
                    print('===== 무인도로 이동합니다 =====')
                    island()
                    return -1
        else:
            break
            
            
#주사위 굴리기 함수, 두개의 주사위 합이 리턴된다, 3번째 더블 나올 시에 0이 리턴된다.
def rollDice(): 
    firstDice = 0
    secondDice = 0
    global is_double
    global islandPlayer
    global now_order
    while True:
        print('주사위를 굴리세요')
        time.sleep(0.1)
        roll = input_timer(10,'roll')
        if roll == 1:
            firstDice = random.randrange(1,7) #첫번째 주사위
            secondDice = random.randrange(1,7) #두번째 주사위
            totalDice = firstDice + secondDice #주사위들의 합
            if player_end_location[now_order] == 5 and islandPlayer[now_order]:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: ' + str(secondDice) + ' =====')
                print('===== 현재 무인도에 있습니다. 이동하지 않습니다. =====')
                islandPlayer[now_order] = 0
                time.sleep(1)
                return 0
            if firstDice != secondDice:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: '+ str(secondDice) + ' =====')
                print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                player_move(totalDice)
                is_double = 0
                return True
            else:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: '+ str(secondDice) + ' =====')
                is_double += 1
                if is_double == 1:
                    print('===== 첫번째 더블! =====')
                    print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                    player_move(totalDice)
                    return True
                elif is_double == 2:
                    print('===== 두번째 더블! =====')
                    print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                    player_move(totalDice)
                    return True
                elif is_double == 3:
                    print('===== 세번째 더블! =====')
                    print('===== 무인도로 이동합니다 =====')
                    island()
                    return -1
        elif roll == 2:
            firstDice = int(input('첫 주사위 :')) #첫번째 주사위
            secondDice = int(input('두번째 주사위 :')) #두번째 주사위
            totalDice = firstDice + secondDice #주사위들의 합         
            if islandPlayer[now_order] == 1:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: ' + str(secondDice) + ' =====')
                print('===== 현재 무인도에 있습니다. 이동하지 않습니다. =====')
                islandPlayer[now_order] = 0
                is_double = 0
                time.sleep(1)
                return 0
            if firstDice != secondDice:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: '+ str(secondDice) + ' =====')
                print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                player_move(totalDice)
                is_double = 0
                return True
            else:
                print('===== 첫번째 주사위 값: ' + str(firstDice) + ', 두번째 주사위 값: '+ str(secondDice) + ' =====')
                is_double += 1
                if is_double == 1:
                    print('===== 첫번째 더블! =====')
                    print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                    player_move(totalDice)
                    return True
                elif is_double == 2:
                    print('===== 두번째 더블! =====')
                    print('===== ' + str(totalDice) + '칸 이동합니다. =====')
                    player_move(totalDice)
                    return True
                elif is_double == 3:
                    print('===== 세번째 더블! =====')
                    print('===== 무인도로 이동합니다 =====')
                    island()
                    return -1
        else:
            break

def print_rank():
    global rank_list
    global login_count
    global rank_money_list
    rank_num = 1
    for i in range(login_count-1,-1,-1):
        print(str(rank_num) + '등 ' + rank_list[i] + '/ 최종재산: ' + str(rank_money_list[i]))
        if i != 0 and rank_money_list[i] > rank_money_list[i-1]:
            rank_num += 1
    

def isSuccess():
    global now_turn
    global id_info_list
    global madelist_flag
    global login_count
    global rank_list
    global rank_money_list
    id_count = 0 #이긴 사람 아이디 번호 저장용
    global money_list
    money_list = [0, 0, 0, 0]
    if now_turn > 10:
        print('게임을 종료합니다')
        for i in range(login_count):
            money_list[i] = id_info_list[i][2]
            if id_info_list[i][3] == 2:
                money_list[i] = -1
        id_success_num = 0
        for j in range(login_count - money_list.count(-1) + 1):
            min_money = float("inf")
            id_count = 0
            for i in money_list:            
                if min_money >= i and i != -1: 
                    min_money = i
                    id_success_num = id_count                
                id_count += 1
            rank_list.append(id_info_list[id_success_num][0])
            rank_money_list.append(id_info_list[id_success_num][2])
            money_list[id_success_num] = -1            
        draw_basic_map()
        print('===== 최종 결과 ======')
        print_rank()
        return True
    elif now_turn <= 10:
        bankruptcy_count = 0
        #본인 턴 처리
        for i in range(login_count):
            if id_info_list[i][3] == 2:
                bankruptcy_count += 1
        draw_basic_map()
        if bankruptcy_count == login_count - 1:# 자길 제외하고 다 파산하면 승리
            print('===== 최종 결과 ======')
            rank_list.append(id_info_list[now_order][0])
            rank_money_list.append(id_info_list[now_order][2])
            print_rank()
            return True
    return False

'''       
id_1 = 'player1'
id_2 = 'player2'
id_3 = 'player3'
id_4 = 'player4'
login_count = 4
id_list = [id_1, id_2, id_3, id_4]
id_1_info = [id_1,1000,1000,0]
id_2_info = [id_2,1000,1000,0]
id_3_info = [id_3,1000,1000,0]
id_4_info = [id_4,1000,1000,0]
id_info_list = [id_1_info,id_2_info,id_3_info,id_4_info]
login_status = True    
'''
def main():
    global now_order
    global now_turn
    global login_count
    global id_info_list
    global sec
    #회원가입/로그인
    if menu() == 0:
        return     
    for i in range(1,12):

        now_turn = i
        for j in range(0, login_count):
            now_order = j
            #여기서부터가 플레이어의 턴, while문 내부가 차례
            while id_info_list[now_order][3] < 2 and is_double < 3:
                if isSuccess():
                    input('게임이 끝났습니다. 종료하려면 enter를 눌러주세요.')
                    return

                sec = 10
                draw_basic_map()
                rollDice()
                
                
                
                #해당 플레이어의 차례 종료
                if is_double==0:
                    break
               
               


main()
