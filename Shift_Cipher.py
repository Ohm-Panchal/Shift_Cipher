x = 'a'
y = 'A'

#dictionary of small letters 
sd = dict()
sd['a'] = 0
for i in range(1,26):
    a = ord(x[0])
    a += 1
    x = chr(a)
    sd[x] = i
#dictionary of capital letters
cd = dict()
cd['A'] = 0
for j in range(1,26):
    b = ord(y[0])
    b += 1
    y = chr(b)
    cd[y] = j

#function to get key of values of small letters
def get_key_sd(val):
    for key, value in sd.items():
         if val == value:
             return key
 
    return "key doesn't exist"

#function to get key of values of capital letters
def get_key_cd(val):
    for key, value in cd.items():
         if val == value:
             return key
 
    return "key doesn't exist"

#------MENU------#
print("1.Encryption")
print("2.Decryption")
choice = input('Enter your choice: ')
choice = int(choice)

if(choice == 1):
    #-------------------ENCRYPTION-------------------#
    PT = input('Enter plain text: ')
    E_Key = input('Enter Encryption Key: ')
    E_Key = int(E_Key)
    Cipher = ''

    #Encrypting plain text using key
    for k in PT:
        if(k == ' '):
            Cipher += ' '

        if(k.isupper()):
            Z = (cd[k]+E_Key)%26  #logic of Shift Cipher Encryption
            Cipher += get_key_cd(Z)

        elif(k.islower()):
            Y = (sd[k]+E_Key)%26  #logic of Shift Cipher Encryption
            Cipher += get_key_sd(Y)

    print(Cipher)  #Printing the Cipher Text 

elif(choice == 2): 
    #-------------------DECRYPTION-------------------#

    CT = input('Enter cipher text: ')
    E_Key = input('Enter Encryption Key: ')
    E_Key = int(E_Key)
    Plain = ''

    #Decrypting plain text using key
    for l in CT:
        if(l == ' '):
            Plain += ' '

        if(l.isupper()):
            Z = cd[l]-E_Key #logic of Shift Cipher Decryption
            if(Z<0):
                Z += 26
            Z %= 26
            Plain += get_key_cd(Z)

        elif(l.islower()):
            Y = sd[l]-E_Key #logic of Shift Cipher Decryption
            if(Y<0):
                Y += 26
            Z %= 26
            Plain += get_key_sd(Y)

    print(Plain)

else:
    print("INVALID CHOICE!!")