import vlc
import signal
import sys

CEND = '\33[0m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CPURPLE = '\33[35m'
BOLD = '\033[1m'


def bang(x, y):
    signal.alarm(0)
    print('\n\n' + CPURPLE + BOLD + 'БА-БАХ!!!' + CEND)
    sys.exit()


def enter_code():
    code = input('Введите код для отмены операции самоуничтожения: ')
    if code == 'swordfish':
        return True


def nothing(x, y):
    pass


def tries(q):
    signal.signal(signal.SIGINT, nothing)
    signal.signal(signal.SIGALRM, bang)
    signal.alarm(30)
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
    p = vlc.MediaPlayer("alarm.mp3")
    p.play()
    print(CRED + 'ВНИМАНИЕ! Запущен механизм самоуничтожения!' + CEND + '\n')
    tries(3)

except (SystemExit, KeyboardInterrupt):
    pass

except EOFError:
    print(CRED + '\n\nПлохая идея!' + CEND)
    bang(0, 0)

except ValueError:
    print(CRED + 'Код не принят!\n' + CEND)

except:
    print('Что-то пошло не так...')
    bang(0, 0)
