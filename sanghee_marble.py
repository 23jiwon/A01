import time
from threading import Timer
import threading
import os
from pyautogui import press, typewrite, hotkey


global at_island
global id_1_info

at_island = 0
id_1_info = ['p1',10000,10000,0]
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
    player_input_ref[0] = input('p1 > ')

      
# 제한시간 내에 사용자 명령 받는 함수 (left_time : 제한시간)
def player_order(left_time, require_msg):
    global player_input
    global now_order
    global id_list
    global player_input_flag 
    player_input=[None]
    input_timer= threading.Thread(target=get_player_input, args=(player_input,))
    input_timer.daemon = True
    input_timer.start()  

    for i in range(1, left_time):
        if input_check(require_msg,player_input[0]):
           return True
           break
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
        else:
            print('===== 경고 1회 받았습니다. =====')
            time.sleep(2)
            # 경고 함수 자리
    else:
        # 이동, 액션 함수 자리
        time.sleep(2)




   

def main():
   #회원가입/로그인
   
   #인원

   #startgame

   #drawmap

   for i in range(10):
      for j in range(0, 4):

         #여기서부터가 플레이어의 턴, while문 내부가 차례
         while (at_island < 2 and id_1_info[3] < 2 and is_double):
            valid_input = player_order(10,'roll')

            if(valid_input):
               print('rolled dice')

               
               


main()








               
