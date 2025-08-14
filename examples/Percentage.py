import cli_loading_bar as load
import time


if __name__ == '__main__':
    #instatiate the class. Iteration is where you want to start in the ber, total is the number of step you want
    #fill is char you want in the bar. You can also use emoji but it doesn't work fine
    l = load.LoadingPercentage(0, 10, fill= '   ', loadingMSG= 'My love is growing')
    print('inizio')
    #Start animation is important to let start the thread to update the animation
    l.StartAnimation()
    for i in range(11):
        #do stuff
        #set the iteration
        l.iteration = i
        #set the string you want to print
        l.suffix = 'Iterazione n: ' + str(i)
        time.sleep(1)
    l.done = True
    print('end')
