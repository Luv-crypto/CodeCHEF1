#! python3
#pw.py - An insecure password locker program

PASSWORDS = {'email': 'scmlofbruhhowfoejgo',
             'facebook': 'ffihfekcdlocj',
             'luggage': '23527'      }
import sys,pyperclip
print(sys.argv)
 

account = input(' enter acc name ')

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(' Password for ' + account +' copied to the clipboard ' ) 
else:
    print('There is no account named ' + account)        

