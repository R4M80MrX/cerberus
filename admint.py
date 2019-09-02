import admin
import sys
import os


def test():
    rc = 0
    if not admin.isUserAdmin():
        print(f'You\'re not an admin. {os.getpid()}, params: {sys.argv}')
        #rc = runAsAdmin(["c:\\Windows\\notepad.exe"])
        rc = admin.runAsAdmin()
    else:
        print(f'You are an admin! {os.getpid()} params: {sys.argv}')
        rc = 0
    x = input('Press Enter to exit.')
    return rc


if __name__ == "__main__":
    sys.exit(test())
