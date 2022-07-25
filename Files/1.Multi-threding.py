import time
import threading
def calc_square(number):
    print("Calcualting square number")
    for n in number:
        time.sleep(1)
        print("square: ", n*n)
def calc_cube(number):
    print("calculate cube of numner")
    for n in number:
        time.sleep(1)
        print("Cube: ",n*n*n)
arr=[2,3,4]

t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()