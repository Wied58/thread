
# https://stackoverflow.com/questions/64579763/python-checking-if-there-is-an-input-from-user-without-stopping-the-loop


from threading import Thread
from sys import exit
from random import random
from datetime import datetime
from time import sleep


#def background():
#    while True:
#        time.sleep(3)
#        print('background task')



def background():

    with open('/home/pi/grafana_project/csv_test.csv', 'w') as file: 

        file.write(f"index,dt_string,data1,data2\n")

        x=0
        while True:    # infinite loop


            x += 1

            now = datetime.now()

            # YYYY-MM-DD HH:MM:SS 
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

            data1 = round(random(), 4)
            data2 = round(random(), 4)

            file.write(f"{x},{dt_string},{data1},{data2}\n")
            file.flush()
            print(f"{x},{dt_string},{data1},{data2}\n")

            sleep(1)

# test comment
# another test

def handling_input(inp):
    print('Got {}'.format(inp))

# the program starts here 

print("Type q to exit!")

t = Thread(target=background)
t.daemon = True
t.start()



while True:
    inp = input()
    handling_input(inp)
    if inp == 'q':
        print('quitting')
        exit()



