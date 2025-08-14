import cli_loading_bar as load
import time


if __name__ == '__main__':
    #instatiate the class. loadMSG is the message you print as "title". msg is a message to comunicate stuff to users
    #doneMSG is the message you print when you finish
    l = load.LoadingDot('', 'Doing stuff', doneMSG='Done!!')
    print('inizio')
    #Start animation is important to let start the thread to update the animation
    l.StartAnimation()
    for i in range(11):
        #do stuff
        #set the iteration
        l.msg = 'Stuff number ' + str(i)
        time.sleep(1)
    l.done = True
    print('end')
