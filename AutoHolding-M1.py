import keyboard
from pynput.mouse import Button, Controller
import time
import colorama

colorama.init()

mouse = Controller()

start_holding = 'Ctrl+0'
stop_holder = 'Ctrl+C'
sleeping_time = 46

def autoM1():
    while True:
        if keyboard.is_pressed(start_holding) == True:
            try:
                mouse.press(Button.left)
                time.sleep(sleeping_time)
                mouse.release(Button.left)
            except:
                print(f'{colorama.Fore.RED}Error desconocido.{colorama.Fore.RESET}')
        elif keyboard.is_pressed(stop_holder) == True:
            exit(1)
        
def main():
    print(colorama.Fore.LIGHTCYAN_EX)
    print(f" Este programa mantiene pulsado el clic izquierdo por '{sleeping_time} segundos', una estimación de lo que se\n tarda en cocinar con el palo en DayZ, tener esto en cuenta.\n")
    print(" Si necesitas parar antes, simplemente pulsa tú mismo una vez el clic izquierdo.\n")
    print(colorama.Fore.RESET)

    print(f"        {colorama.Fore.LIGHTBLUE_EX}· GitHub:{colorama.Fore.RESET}  {colorama.Fore.LIGHTMAGENTA_EX}https://github.com/SrCroqueta{colorama.Fore.RESET}")
    print(f"        {colorama.Fore.LIGHTBLUE_EX}· Twitch:{colorama.Fore.RESET}  {colorama.Fore.LIGHTMAGENTA_EX}https://www.twitch.tv/srcroqueta_{colorama.Fore.RESET}")
    print(f"        {colorama.Fore.LIGHTBLUE_EX}· Twitter:{colorama.Fore.RESET} {colorama.Fore.LIGHTMAGENTA_EX}https://twitter.com/SrCroqueta_{colorama.Fore.RESET}")

    print(f"{colorama.Fore.LIGHTYELLOW_EX}\n\n Usa '{start_holding}' para iniciar AutoHolding-M1, o pulsa '{stop_holder}' para cerrar este programa.{colorama.Fore.RESET}")
    autoM1()

if __name__ == "__main__":
    main()
