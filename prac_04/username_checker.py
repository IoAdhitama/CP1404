"""
Prompts the user for a username
and checks whether the input matches
a list of authorized users
"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
                 'InterpreterInterface', 'StartServer', 'bob']

    username = str(input("Enter username: "))
    if username in usernames:
        print("Access Granted.")
    else:
        print("Access Denied.")


main()
