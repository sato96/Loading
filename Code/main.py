# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from Loading import LoadingDot, LoadingPercentage, LoadingBar
import time
##quindi devo settare iterazione e totale, chiaramente posso fare così:
##funziona comunque con il thread ma total va messo, posso metterlo obbligatorio in fase di inizializzazione
#per supportere le emoji bisogna contare i pixel che occupano -> questo funziona per le faccine ⏲
def Percentage(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd=""):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '⏲' * (length - filledLength) *len(fill)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    #sys.stdout.write('\r' + prefix + bar + percent + suffix + printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # l = LoadingDot()
    # #l = LoadingBar(logMsg=False)
    l = LoadingPercentage(0, 10, length=10, fill= '  ', loadingMSG= 'My love is growing')
    #
    # l.msg = 'Messaggio lungo'
    print('inizio')
    l.StartAnimation()
    # time.sleep(1)
    for i in range(11):
        l.iteration = i
        l.suffix = 'Iterazione n: ' + str(i)
        time.sleep(1)

    # long process here
    l.done = True
    print('end')
    # print(l.getLogMsg())
    # l.saveLogMsg()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
