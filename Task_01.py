from colorama import init , Fore , Style
init(autoreset=True)


def Encryption(plain_text,encrypt_key):
    key = int(encrypt_key)
    cipher_text = ""
   
    for text in plain_text:
        # print(text)
        if text.isalpha(): #check 1
         if text.islower(): #check 2
            # print(ord(text))

          num = (ord(text) -97  + key) % 26
        #   print(num)
          cipher_text = cipher_text + chr(num + 97)
         else:
             num = (ord(text) - 65  + key) % 26
             cipher_text = cipher_text +  chr(num + 65 )
        else:
             cipher_text = cipher_text + text

    # return cipher_text
             
             
    print( "CIPHER TEXT IS : " , Fore.YELLOW + cipher_text)



def Decryption(cipher_text , decrypt_key):
    key = int(decrypt_key)
    plain_text = ""
    for text in cipher_text:
        if text.isalpha():
            if text.islower():
                num = (ord(text)-97 - key) % 26
                plain_text = plain_text  + chr(num + 97)
            else:
                num = (ord(text) - 65 - key) % 26
                plain_text = plain_text + chr(num + 65)
        else:
                    plain_text = plain_text + text

    
    print( "PLAIN TEXT IS   "  ,Fore.PINK +  plain_text)


def main():
    while True:
        print(Fore.CYAN + "1. Encryption of Text")
        print(Fore.CYAN + "2. Decryption of Text")
        print(Fore.RED + "3. Exit ")

        choice = input("Enter your choice :")
        if choice == '1':
             plain_text = input("Enter the Plain text : ")
             encrypt_key = input("Enter the key for encryption : ")
             Encryption(plain_text,encrypt_key)
        elif choice == '2':
            cipher_text = input("Enter the Cipher Text :")
            decrypt_key = input("Enter the key for decryption : ")
            Decryption(cipher_text , decrypt_key)

        elif choice == '3':
            print(fore.RED + "Program Over")
            exit()
        else:
            print("Invalid Input")

main()








         



    
    
