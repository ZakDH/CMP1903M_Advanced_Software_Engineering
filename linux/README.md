# Keylogger

Keylogger is a simple program that logs every key press made by the user on the keyboard. It can run in the background without detection and save the logs to a file on the computer. It is compatible with Windows, Linux, and Mac operating systems.

# Purpose
The purpose of the Keylogger project is to provide individuals or organizations with a way to monitor the usage of a computer system. The program can be used to monitor productivity, prevent unauthorized access to sensitive information, or track the activities of employees.
# Features
- Logs every key press made on the keyboard
- Runs in the background without detection
- Saves logs to a file on the computer
- Cross-platform support for Windows, Mac, and Linux operating systems


## Installation
To install the Keylogger program, follow the instructions below:

Open the terminal/command prompt on your system.
Navigate to the directory where you want to install the program.
Clone the repository using the command git clone https://github.com/{username}/{repository_name}.git.
Navigate to the Keylogger directory using the command cd Keylogger.
Install the required packages using the command

```
  pip3 install -r requirements.txt
```
or 
```
  pip3 install pyxhook
```

## Usage
Once installed, the Keylogger program can be started by running the command nohup python3 keylogger.py & in the terminal/command prompt. The program will start running in the background and automatically log every key press made on the keyboard. The logs are saved to a file on the computer, which can be accessed at any time by the user.
It is important to note that the program runs undetected by the user, and as such, may be subject to legal restrictions in certain jurisdictions. It is the responsibility of the user to ensure that the program is used in compliance with local laws and regulations.


The meaning of nohup is ‘no hangup‘.
When nohup command use with ‘&’ then it doesn’t return to shell command prompt after running the command in the background. 
```
$~/Keylogger/linux$ nohup python3 keylogger.py &
[1] 12529 //this is the keylogger's PID (process ID)
$:~/Keylogger/linux$ fg

```
# Contributors

1. Olalekan Olanrewaju (Coder)

2. Zak Hagreeves (Coder)

# License
The Keylogger project is licensed under the MIT License. See the LICENSE file for more information.






