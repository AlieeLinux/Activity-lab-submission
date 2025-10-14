"""
Author: AieeLinux
"""

username="Kyouko"
password="toshinou"
is_2fa_enabled=False
twoFaCode=123456

try:
    input_username = input("Username: ")
    
    if is_2fa_enabled:
        input_2fa = int(input("Enter 2fa code: "))
        
        if input_2fa == twoFaCode and input_username == username:
            print("Login Successful!")
        else:
            print("Login Failed!")

    else:
        input_password = input("Password: ")

        if username == input_username and password == input_password:
            print("Login Successful!")
        else:
            print("Login Failed!")

except Exception:
    print("Login Failed!")