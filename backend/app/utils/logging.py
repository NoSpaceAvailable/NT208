from datetime import date

class Foreground:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class Background:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class Style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'

date_fmt = "%d-%m-%Y %H:%M"

def p(msg, _type = "INFO", color = Background.GREEN, where = __file__):
    print(now() + Foreground.CYAN + f"[{where}] " + Style.RESET_ALL + color + _type + Style.RESET_ALL + " " + msg)

def now():
        return Background.GREEN + date.today().strftime(date_fmt) + Style.RESET_ALL + " "

def info(msg, where = __file__):
    p(msg, where = where)

def warn(msg, where = __file__):
    p(msg, "WARN" ,Background.YELLOW, where = where)

def error(msg, where = __file__):
    p(msg, "FAIL" ,Background.RED, where = where)