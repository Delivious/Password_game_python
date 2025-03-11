import math
import random
from captcha import captcha
special_characters = "!@#$%^&*()_+-=[]|;:'\",.<>?/"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit="1234567890"
month="January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December","january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"
I=1
V=5
X=10
L=50
C=100
D=500
M=1000
roman=I,V,X,L,C,D,M
reset=input("you ready? Y or N")
print()
print()
print()
while reset=="Y":
 print("Welcome to the password game!")
 print()
 pas=input("Create a password:")
 print()
 print()
 if pas:
   pas=input("Add a number:")
   print()
   print()
   has_digit= any(c in digit for c in pas)
   if has_digit:
     pas=input("Include an Uppercase letter:")
     print()
     print()
     has_upper= any(c in upper for c in pas)
     has_digit= any(c in digit for c in pas)
     if has_upper and has_digit:
       pas=input("Include a special character:")
       print()
       print()
       has_special= any(c in special_characters for c in pas)
       has_upper= any(c in upper for c in pas)
       has_digit= any(c in digit for c in pas)
       if has_special and has_upper and has_digit:
          pas=input("Numbers must add up to 25:")
          print()
          print()
          has_special= any(c in special_characters for c in pas)
          has_upper= any(c in upper for c in pas)
          has_digit= any(c in digit for c in pas)
          digits = [int(c) for c in pas if c.isdigit()]
          total = sum(digits)
          if total==25 and has_special and has_upper and has_digit:
            pas=input("Must include a month of the year:")
            print()
            print()
            has_special= any(c in special_characters for c in pas)
            has_upper= any(c in upper for c in pas)
            has_digit= any(c in digit for c in pas)
            digits = [int(c) for c in pas if c.isdigit()]
            total = sum(digits)
            has_month = any(m in pas for m in month)
            if total==25 and has_special and has_upper and has_digit and has_month:
              print(captcha)
              pas=input("This captcha must be in your password:")
              print()
              print()
              has_special= any(c in special_characters for c in pas)
              has_upper= any(c in upper for c in pas)
              has_digit= any(c in digit for c in pas)
              digits = [int(c) for c in pas if c.isdigit()]
              total = sum(digits)
              has_month = any(m in pas for m in month)
              has_captcha = all(m in pas for m in captcha)
              if total==25 and has_special and has_upper and has_digit and has_month and has_captcha:
                print("yes")
              else:
                print()
                print("you messed up")
                reset=input("do you want to restart? Y or N")
            else:
              print()
              print("you messed up")
              reset=input("do you want to restart? Y or N")
          else:
           print()
           print("you messed up")
           reset=input("do you want to restart? Y or N")
       else:
         print()
         print("you messed up")
         reset=input("do you want to restart? Y or N")
     else:
      print()
      print("you messed up")
      reset=input("do you want to restart? Y or N")
   else:
    print()
    print("you messed up")
    reset=input("do you want to restart? Y or N")
 else:
  print()
  print("you messed up")
  reset=input("do you want to restart? Y or N")
else:
 print()
 print("you messed up")
 reset=input("do you want to restart? Y or N")
