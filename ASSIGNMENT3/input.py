import sys
import termios
import tty
import signal


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(fd)
    try:
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def alarm_handler(signum, frame):
    raise KeyboardInterrupt


def input_with_timeout(timeout):
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        ch = getch()
        signal.alarm(0)
        return ch
    except KeyboardInterrupt:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None
