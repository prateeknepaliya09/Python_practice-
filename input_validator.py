# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:50:40 2016

@author: Prateek
"""

#input that rejects junk

def read_single_keypress() -> str:
    """Waits for a single keypress on stdin.
    -- from :: http://stackoverflow.com/a/6599441/4532996
    """

    import termios, fcntl, sys, os
    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save) # copy the stored version to update
    # iflag
    attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK
                  | termios.ISTRIP | termios.INLCR | termios. IGNCR
                  | termios.ICRNL | termios.IXON )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios. PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                  | termios.ISIG | termios.IEXTEN)
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
    # read a single keystroke
    try:
        ret = sys.stdin.read(1) # returns a single character
    except KeyboardInterrupt:
        ret = 0
    finally:
        # restore old state
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
    return ret

def until_not_multi(chars) -> str:
    """read stdin until !(chars)"""
    import sys
    chars = list(chars)
    y = ""
    sys.stdout.flush()
    while True:
        i = read_single_keypress()
        _ = sys.stdout.write(i)
        sys.stdout.flush()
        if i not in chars:
            break
        y += i
    return y

def _can_you_vote() -> str:
    """a practical example:
    test if a user can vote based purely on keypresses"""
    print("can you vote? age : ", end="")
    x = int("0" + until_not_multi("0123456789"))
    if not x:
        print("\nsorry, age can only consist of digits.")
        return
    print("your age is", x, "\nYou can vote!" if x >= 18 else "Sorry! you can't vote")

_can_you_vote()