import pyautogui, keyboard, psutil, os
from time import sleep
from multiprocessing import Process

def alt_tab():
    counter = 0
    while True:
        pyautogui.keyDown('alt')
        sleep(0.2)
        pyautogui.keyDown('tab')
        sleep(0.2)
        pyautogui.keyUp('alt')
        pyautogui.keyUp('tab')
        sleep(5)
        counter += 1
        if counter == 1:
            print(f'{counter} iteration has been done. It gives about {counter*6/60} minutes of idle.')
        else:
            print(f'{counter} iterations have been done. It gives about {counter*6/60} minutes of idle.')

def f8_await():
    while True:
        if keyboard.is_pressed('f8') and side_process_pid.is_running():
            if side_process_pid.as_dict().get('status') != 'stopped':
                side_process_pid.suspend()
                print('Process suspended. If you press ctrl + c now, the console can also suspend. Consider F8/F12')
            else:
                side_process_pid.resume()
                print('Process resumed.')
        elif keyboard.is_pressed('f12') and side_process_pid.is_running():
            side_process.terminate()
            print('Process terminated.')
            break
        elif not side_process_pid.is_running():
            side_process.terminate()
            print('Something went wrong.')
            break
        sleep(0.1)


if __name__ == '__main__':
    os.system('cls')
    pyautogui.FAILSAFE = True

    side_process = Process(target=alt_tab)
    side_process.start()
    print('''
Process started.
Press F8 to pause/resume.
Press F12 to terminate.''')

    side_process_pid = psutil.Process(side_process.pid)
    f8_await()
