import time
from threading import Timer
import threading
import os
from pyautogui import press, typewrite, hotkey


global at_island

#로그인시 얻은 아이디 변수
global id_1
global id_2
global id_3
global id_4
id_1 = 'p1'
id_2 = 'p2'
id_3 = 'p3'
id_4 = 'p4'
global id_list

id_list = [id_1, id_2, id_3, id_4]

#6.1.1. 플레이어 수
global login_count
login_count = 4

#6.1.2 플레이어 정보
at_island = 0   #이건 로그에서 저장받아오기

global id_1_info
global id_2_info
global id_3_info
global id_4_info
global id_info_list
id_1_info = [id_1,10000,10000,0]
id_2_info = [id_2,10000,10000,0]
id_3_info = [id_3,10000,10000,0]
id_4_info = [id_4,10000,10000,0]

#id info 이차원 배열
id_info_list = [id_1_info,id_2_info,id_3_info,id_4_info]

is_double = True


def input_check(require, player_input):
   match player_input:
      case 'roll'|'ㅈㅅㅇ'|'주사위':
         if(require == 'roll'):        
            return True
         else:
            return False
      

def get_player_input(player_input_ref):
    global now_order
    global id_list
    
    player_input_ref[0] = input(id_list[now_order]+' > ')




    

      
# 제한시간 내에 사용자 명령 받는 함수 (left_time : 제한시간)
def input_timer(left_time, require_msg):
    global player_input
    global now_order
    global id_list
    
    player_input=[None]
    input_timer= threading.Thread(target=get_player_input, args=(player_input,))
    input_timer.daemon = True

    input_timer.start()  
    for i in range(1, left_time):
        if input_check(require_msg,player_input[0]):
           return True
        elif player_input[0] != None:
           print('입력이 틀렸습니다.')
           player_input=[None]
           input_timer= threading.Thread(target=get_player_input, args=(player_input,))
           input_timer.daemon = True
           input_timer.start()

        time.sleep(1)
        
    if player_input[0] == None:
        press('enter')
        player_input=[None]
        print('===== %d초가 지났습니다. =====' % left_time)
        if(left_time == 10):
            print('===== 중도포기 하였습니다. =====')
            time.sleep(2)
            
            # 중도포기 함수 자리
            id_info_list[now_order][3] = 2
        else:
            print('===== 경고 1회 받았습니다. =====')
            time.sleep(2)
            # 경고 함수 자리
    else:
        
        time.sleep(2)




   

def main():
   #회원가입/로그인
   
   #인원

   #startgame

   #drawmap
   global now_order

   for i in range(10):
      for j in range(0, 4):

         #여기서부터가 플레이어의 턴, while문 내부가 차례
         while (at_island < 2 and id_info_list[j][3] < 2 and is_double):
            now_order = j
            valid_input = input_timer(10,'roll')

            


            if(valid_input):
               print('rolled dice')
               # 이동, 액션 함수 자리



               #해당 플레이어의 차례 종료
               break

               

               
               


main()








               
