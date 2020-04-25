import vlc
import signal
import sys

CEND = '\33[0m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CPURPLE = '\33[35m'
BOLD = '\033[1m'


def bang(x, y):
    print('\n\n' + CPURPLE + BOLD + 'БА-БАХ!!!' + CEND)
    p = vlc.MediaPlayer("alarm.mp3")
    p.play()
    sys.exit()


def enter_code():
    code = input('Введите код для отмены операции самоуничтожения: ')
    if code == 'swordfish':
        return True


def tries(q):
    signal.signal(signal.SIGALRM, bang)
    signal.alarm(5)
    for x in range(q):
        if enter_code():
            signal.alarm(0)
            print(CGREEN + 'WIN' + CEND + '\n')
            sys.exit()
        if x == 2:
            bang(0, 0)
        else:
            print(CRED + 'Код не принят!\n' + CEND)


try:
    print(CRED + 'WNIMANIE!' + CEND + '\n')
    tries(3)
    sleep(1)

except:
    print('Error! Взрываемся)')
    bang(0, 0)
