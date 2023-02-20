#Caesar Cipher based symetric encoder
#DSC prg.
#FEB2023
# ref : https://www.geeksforgeeks.org/python-convert-string-to-unicode-characters/


def csrCiphyer(str_input='', digit_shift=0):
    encrypted = ''
    list_encrypted= []
    if(isinstance(str_input,str)):
        # encrypted = ''.join(r'\u{:04X}'.format(ord(char)+digit_shift) for char in str_input)
        encrypted = ''.join(r''.format(ord(char) + digit_shift) for char in str_input)
        for char in str_input:
            list_encrypted.append(ord(char) + digit_shift)

        encrypted = ''.join(r'{}'.format(chr(char)) for char in list_encrypted)


    else:
        print('Input is not a valid string')
        print(' Your input is : ', str(str_input))
        encrypted = 'Input is not a valid string'

    return encrypted

if __name__ == "__main__":
    print("########################### INPUT ################################")
    print("This is a sample cipher run using an input string and a digit for shift.")
    in_str = input("Type in your input string :" )
    in_digit = input("Type in your input digit for cipher :" )
    print("########################### OUTPUT ################################")
    print("You entered a string   : ", in_str)
    print("You entered a digit of : ", in_digit)


    print("Your encrypted string is : " , csrCiphyer(in_str ,int(in_digit)))