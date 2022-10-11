global id_1
global id_2
global id_3
global id_4
global login_count
global login_status
global id_list
id_1 = ' '
id_2 = ' '
id_3 = ' '
id_4 = ' '
id_list = []
login_count = 0
login_status = False

def menu():
    global id_1
    global id_2
    global id_3
    global id_4
    global login_count
    global login_status
    global id_list
    
    while login_status == False:
        print('====== 메인 창입니다 ======')
        print('원하는 메뉴를 골라 주세요')
        print('  register/login/quit')
        print('===============================')
        print()
        a = input("userID > ")
        if a == 'quit' or a == '종료' or a == 'q' or a == 'ㅈㄹ' or a == 'exit' or a == '나가기':
            print('====== 미니 마블 게임을 종료합니다 ======')
            print()
            return
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
            
        if id_status == True and pw_status == True:
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
    global login_count
    global login_status
    
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
    login_status = True
    return


menu()
