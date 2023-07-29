"""
echo "Written by Ahmed Ali"

"""
import os
while True:
    try:
        from pyotp import TOTP as GET_OTP
        os.system("clear")
        break
    except ImportError:
        os.system("pip install pyotp")
    

class TwoFactorAuthenticator:
    def __init__(self, two_factor_key):
        self.two_factor_key = two_factor_key.replace(' ', '')
        self.otp = GET_OTP(self.two_factor_key)

    def get_otp(self):
        return self.otp.now()

    @staticmethod
    def get_2f_key_from_user():
        users_2f_key = input("Input your 2F key: ")
        return users_2f_key

if __name__ == "__main__":
    two_factor_key = TwoFactorAuthenticator.get_2f_key_from_user()
    authenticator = TwoFactorAuthenticator(two_factor_key)
    code = authenticator.get_otp()
    print("2F code:\x1b[1;92m", code)
