Keylogger Class Documentation
The Keylogger class's primary purpose is to record and keep track of the individual keystrokes made on a computer keyboard. There are three different methods available within this class: init(), on_key_press(), and start().
init() Method
The init() procedure creates a log file with the current date and time as its starting point. It takes no arguments.
on_key_press() Method
Every time a key is pressed on the keyboard, the on_key_press() method is called upon to perform its function. It records the key press events in the log file, with the exception of the 'Enter' key, which is recorded as a newline character instead. Only one argument is required, which is: the action that was brought about by pressing the key.
start() Method
The start() method is responsible for the creation of a new HookManager object, the configuration of the on_key_press() method as the key down event handler, and the setting of the keyboard hook. After that, it begins to listen for keyboard events using the hook until the user cancels the listener or an exception is thrown.
Overall, the Keylogger class is a useful tool for monitoring and logging keyboard events, and its methods and functionality can be easily integrated into other applications.
