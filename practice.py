import math
import random
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
while reset=="Y":
 print("Welcome to the password game!")
 pas=input("Create a password:")
 if pas:
   pas=input("Add a number:")
   has_digit= any(c in digit for c in pas)
   if has_digit:
     pas=input("Include an Uppercase letter:")
     has_upper= any(c in upper for c in pas)
     has_digit= any(c in digit for c in pas)
     if has_upper and has_digit:
       pas=input("Include a special character:")
       has_special= any(c in special_characters for c in pas)
       has_upper= any(c in upper for c in pas)
       has_digit= any(c in digit for c in pas)
       if has_special and has_upper and has_digit:
          pas=input("Numbers must add up to 25:")
          has_special= any(c in special_characters for c in pas)
          has_upper= any(c in upper for c in pas)
          has_digit= any(c in digit for c in pas)
          digits = [int(c) for c in pas if c.isdigit()]
          total = sum(digits)
          if total==25 and has_special and has_upper and has_digit:
            pas=input("Must include a month of the year:")
            has_special= any(c in special_characters for c in pas)
            has_upper= any(c in upper for c in pas)
            has_digit= any(c in digit for c in pas)
            digits = [int(c) for c in pas if c.isdigit()]
            total = sum(digits)
            has_month = any(m in pas for m in month)
            if total==25 and has_special and has_upper and has_digit and has_month:
              print(captcha)
              pas=input("This captcha must be in your password:")
              has_special= any(c in special_characters for c in pas)
              has_upper= any(c in upper for c in pas)
              has_digit= any(c in digit for c in pas)
              digits = [int(c) for c in pas if c.isdigit()]
              total = sum(digits)
              has_month = any(m in pas for m in month)
              has_captcha = all(m in password for m in captcha)
              if total==25 and has_special and has_upper and has_digit and has_month and all(m in password for m in captcha):
                print("Yes")
              else:
                print("you messed up")
                reset=input("do you want to restart? Y or N")
            else:
              print("you messed up")
              reset=input("do you want to restart? Y or N")
          else:
           print("you messed up")
           reset=input("do you want to restart? Y or N")
       else:
         print("you messed up")
         reset=input("do you want to restart? Y or N")
     else:
      print("you messed up")
      reset=input("do you want to restart? Y or N")
   else:
    print("you messed up")
    reset=input("do you want to restart? Y or N")
 else:
  print("you messed up")
  reset=input("do you want to restart? Y or N")
else:
 print("you messed up")
 reset=input("do you want to restart? Y or N")
