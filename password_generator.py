import hashlib
import binascii

website = input("Please enter the website domain: ")
user_name = input("Please enter your username: ")
master_password = input("Please enter your master password: ")
version = input("Please enter a positive integer for the password version you would like to generate: ")
length = (int)(input("Please specify the length of the password you would like: "))



def generate_password(website, user_name, master_password, version):
    salt_one = website + user_name + version
    salt_two = website + user_name + version 
    middle = length
    gen_one = binascii.hexlify(hashlib.pbkdf2_hmac
                            ("sha256", master_password.encode("utf-8"),
                                                salt_one.encode("utf-8"), 100000, 32)).decode()
    gen_two = binascii.hexlify(hashlib.pbkdf2_hmac
                            ("sha256", gen_one.encode("utf-8"),
                                                salt_two.encode("utf-8"), 100000, length)).decode()
    gen_two = gen_two[:middle]
    return gen_two


print(generate_password(website, user_name, master_password, version))
