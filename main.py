##########################################################################################
# Dzień dziewiąty
##########################################################################################
data = open("dzien9_headtail_org.txt")
dataString = data.read()
dataList = dataString.split("\n")
print(dataList)

# pip install numpy
import numpy as np
import pandas as pd


#head_temp_position tego nie trzeba, bo tylko ogon mnie interesuje
last_head_x_position=150
last_head_y_position=150
#set wynikowy dla ogona
tail_positions_set={"150 150"}
#z założeniem początku
last_tail_x_position=150
last_tail_y_position=150

for ruch_wiersz, ruch_zawart in enumerate(dataList):
    ruch_zawart_podzielony=ruch_zawart.split(' ')
    print(ruch_wiersz, ruch_zawart_podzielony)

    i=1

    if ruch_zawart_podzielony[0]=='R':
        print('Right')
        while i <= int(ruch_zawart_podzielony[1]):
            print('ruch:', i, 'w kierunku R')
            last_head_x_position+=1

            #głowa już się ruszyła. Zadanie jak się zachowuje ogon?
            if last_head_x_position-last_tail_x_position==2:
                print('czas sie ruszyc')
                if last_head_y_position==last_tail_y_position:
                    last_tail_x_position+=1
                elif last_head_y_position>last_tail_y_position:
                    last_tail_x_position+=1
                    last_tail_y_position+=1
                elif last_head_y_position<last_tail_y_position:
                    last_tail_x_position+=1
                    last_tail_y_position-=1
                else:
                    print('error')
                    break
                #print('x', last_tail_x_position, 'y', last_tail_y_position)

                last_tail_position_string = str(last_tail_x_position) + ' ' + str(last_tail_y_position)
                print('Dodaje taki punkt:', last_tail_position_string)
                tail_positions_set.add(last_tail_position_string)
            else:
                print('nie ruszaj sie')

            i+=1 #próba wyjścia z while'a

    elif ruch_zawart_podzielony[0]=='L':
        print('Left')
        while i <= int(ruch_zawart_podzielony[1]):
            print('ruch:', i, 'w kierunku L')
            last_head_x_position-=1

            #głowa już się ruszyła. Zadanie jak się zachowuje ogon?
            if last_tail_x_position-last_head_x_position==2:
                print('czas sie ruszyc')
                if last_head_y_position==last_tail_y_position:
                    last_tail_x_position-=1
                elif last_head_y_position>last_tail_y_position:
                    last_tail_x_position-=1
                    last_tail_y_position+=1
                elif last_head_y_position<last_tail_y_position:
                    last_tail_x_position-=1
                    last_tail_y_position-=1
                else:
                    print('error')
                    break
                #print('x', last_tail_x_position, 'y', last_tail_y_position)
                last_tail_position_string = str(last_tail_x_position) + ' ' + str(last_tail_y_position)
                print('Dodaje taki punkt:', last_tail_position_string)
                tail_positions_set.add(last_tail_position_string)
            else:
                print('nie ruszaj sie')

            i += 1

    elif ruch_zawart_podzielony[0]=='D':
        print('Down')
        while i <= int(ruch_zawart_podzielony[1]):
            print('ruch:', i, 'w kierunku D')
            last_head_y_position-=1

            #głowa już się ruszyła. Zadanie jak się zachowuje ogon?
            if last_tail_y_position-last_head_y_position==2:
                print('czas sie ruszyc')
                if last_head_x_position==last_tail_x_position:
                    last_tail_y_position-=1
                elif last_head_x_position>last_tail_x_position:
                    last_tail_x_position+=1
                    last_tail_y_position-=1
                elif last_head_x_position<last_tail_x_position:
                    last_tail_x_position-=1
                    last_tail_y_position-=1
                else:
                    print('error')
                    break
                print('x', last_tail_x_position, 'y', last_tail_y_position)
                last_tail_position_string = str(last_tail_x_position) + ' ' + str(last_tail_y_position)
                print('Dodaje taki punkt:', last_tail_position_string)
                tail_positions_set.add(last_tail_position_string)
            else:
                print('nie ruszaj sie')

            i += 1


    elif ruch_zawart_podzielony[0]=='U':
        print('Up')
        while i <= int(ruch_zawart_podzielony[1]):
            print('ruch:', i, 'w kierunku U')
            last_head_y_position+=1

            # głowa już się ruszyła. Zadanie jak się zachowuje ogon?
            if last_head_y_position - last_tail_y_position == 2:
                print('czas sie ruszyc')
                if last_head_x_position == last_tail_x_position:
                    last_tail_y_position += 1
                elif last_head_x_position > last_tail_x_position:
                    last_tail_x_position += 1
                    last_tail_y_position += 1
                elif last_head_x_position < last_tail_x_position:
                    last_tail_x_position -= 1
                    last_tail_y_position += 1
                else:
                    print('error')
                    break
                print('x', last_tail_x_position, 'y', last_tail_y_position)
                last_tail_position_string = str(last_tail_x_position) + ' ' + str(last_tail_y_position)
                print('Dodaje taki punkt:', last_tail_position_string)
                tail_positions_set.add(last_tail_position_string)
            else:
                print('nie ruszaj sie')

            i += 1

    else:
        print('error')

print(tail_positions_set)

print('dlugosc to:', len(tail_positions_set))

#Odpowiedź to: 6470

#tail_positions_set