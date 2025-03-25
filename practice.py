import math
import random
import re
from captcha import captcha
from captcha import cap1
from captcha import cap2
from captcha import cap3
from captcha import cap4
from captcha import cap5
from elements import *
from roman import *
from leap import *
from hex import *
special_characters = "!@#$%^&*()_+-=[]|;:'\",.<>?/"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit="1234567890"
month="January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December","january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"
reset=input("you ready? Y or N")
print()
print()
print()
while reset=="Y":
 cap1=random.randint(1,35)
 cap2=random.randint(1,35)
 cap3=random.randint(1,35)
 cap4=random.randint(1,35)
 cap5=random.randint(1,35)
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
                wordle="baste","Baste"
                pas=input("You must have todays wordle answer:")
                print()
                print()
                has_special= any(c in special_characters for c in pas)
                has_upper= any(c in upper for c in pas)
                has_digit= any(c in digit for c in pas)
                digits = [int(c) for c in pas if c.isdigit()]
                total = sum(digits)
                has_month = any(m in pas for m in month)
                has_captcha = all(m in pas for m in captcha)
                has_wordle = any(m in pas for m in wordle)
                if total==25 and has_special and has_upper and has_digit and has_month and has_captcha and has_wordle:
                 print()
                 pas = input("Enter element symbols that add up to 200:")
                 pattern = r'(' + '|'.join(sorted(elements.keys(), key=len, reverse=True)) + r')'
                 matches = re.findall(pattern, pas)
                 total_atomic_number = sum(elements[element] for element in matches)
                 if total==25 and has_special and has_upper and has_digit and has_month and has_captcha and has_wordle and total_atomic_number == 200:
                  print()
                  print()
                  pas = input("Add roman numerals that multiply to 35: ")
                  pattern = r'(' + '|'.join(sorted(roman.keys(), key=len, reverse=True)) + r')'
                  matches = re.findall(pattern, pas)
                  if not matches:
                   print("you have no numerals in your password.")
                   reset=input("do you want to restart? Y or N")
                  else:
                   total_product = 1
                  for numeral in matches:
                   total_product *= roman[numeral]
                  if total==25 and has_special and has_upper and has_digit and has_month and has_captcha and has_wordle and total_atomic_number == 200 and total_product == 35:
                     print()
                     print()                  
                     def find_leap_years_in_string(text):
                      numbers = re.findall(r'\d+', text)  # Extracts all numbers from the input text
                      found_leap_years = [int(num) for num in numbers if int(num) in leap_years]  # Checks if extracted numbers are in the leap_years list
                      return found_leap_years
                     pas=input("include a leap year:")
                     found_leaps = find_leap_years_in_string(pas)
                     has_leap = bool(found_leaps)
                     if total==25 and has_special and has_upper and has_digit and has_month and has_captcha and has_wordle and total_atomic_number == 200 and total_product == 35 and has_leap:
                       random_choice = random.choice(colors)                     
                       pas=input(f"what is the hex code of this color?{random_choice[1]}(include it in your password, duh):")
                       correct_hex = f"#{random_choice[2]:06X}"
                       if total==25 and has_special and has_upper and has_digit and has_month and has_captcha and has_wordle and total_atomic_number == 200 and total_product == 35 and has_leap and re.search(rf"{correct_hex}", pas, re.IGNORECASE):
                        print("True")
                       else:
                        print()
                        print("you messed up")
                        cap1=random.randint(1,35)
                        cap2=random.randint(1,35)
                        cap3=random.randint(1,35)
                        cap4=random.randint(1,35)
                        cap5=random.randint(1,35)
                        if has_special!=True:
                         print("There were no special characters")
                        if has_upper!=True:
                         print("There were no uppercase letters")
                        if has_digit!=True:
                         print("There were no numbers")
                        if total!=25:
                         print("Your sum did not equal 25")
                        if has_month!=True:
                         print("You did not include a month of the year")
                        if has_captcha!=True:
                         print("You did not include the captcha")
                        if has_wordle!=True:
                         print("You did not include the worlde answer")
                        if total_atomic_number !=200:
                         print("You did not have the atomic numbers add up to 200")
                        if total_product != 35:
                         print("You did not have roman numerals that multiply up to 35")
                         print(total_product)
                        if has_leap!=True:
                         print("You did not have a leap year")
                        if pas and not re.search(rf"{correct_hex}", pas, re.IGNORECASE):
                          print("Your hex code was wrong, stupid.")
                        reset=input("do you want to restart? Y or N")
                     else:
                        print()
                        print("you messed up")
                        cap1=random.randint(1,35)
                        cap2=random.randint(1,35)
                        cap3=random.randint(1,35)
                        cap4=random.randint(1,35)
                        cap5=random.randint(1,35)
                        if has_special!=True:
                         print("There were no special characters")
                        if has_upper!=True:
                         print("There were no uppercase letters")
                        if has_digit!=True:
                         print("There were no numbers")
                        if total!=25:
                         print("Your sum did not equal 25")
                        if has_month!=True:
                         print("You did not include a month of the year")
                        if has_captcha!=True:
                         print("You did not include the captcha")
                        if has_wordle!=True:
                         print("You did not include the worlde answer")
                        if total_atomic_number !=200:
                         print("You did not have the atomic numbers add up to 200")
                        if total_product != 35:
                         print("You did not have roman numerals that multiply up to 35")
                         print(total_product)
                        if has_leap!=True:
                         print("You did not have a leap year")
                        reset=input("do you want to restart? Y or N")
                  else:
                     print()
                     print("you messed up")
                     cap1=random.randint(1,35)
                     cap2=random.randint(1,35)
                     cap3=random.randint(1,35)
                     cap4=random.randint(1,35)
                     cap5=random.randint(1,35)
                     if has_special!=True:
                      print("There were no special characters")
                     if has_upper!=True:
                      print("There were no uppercase letters")
                     if has_digit!=True:
                      print("There were no numbers")
                     if total!=25:
                      print("Your sum did not equal 25")
                     if has_month!=True:
                      print("You did not include a month of the year")
                     if has_captcha!=True:
                      print("You did not include the captcha")
                     if has_wordle!=True:
                      print("You did not include the worlde answer")
                     if total_atomic_number !=200:
                      print("You did not have the atomic numbers add up to 200")
                     if total_product != 35:
                      print("You did not have roman numerals that added up to 35")
                      print(total_product)
                     reset=input("do you want to restart? Y or N")
                 else:
                  print()
                  print("you messed up")
                  cap1=random.randint(1,35)
                  cap2=random.randint(1,35)
                  cap3=random.randint(1,35)
                  cap4=random.randint(1,35)
                  cap5=random.randint(1,35)
                  if has_special!=True:
                    print("There were no special characters")
                  if has_upper!=True:
                    print("There were no uppercase letters")
                  if has_digit!=True:
                    print("There were no numbers")
                  if total!=25:
                    print("Your sum did not equal 25")
                  if has_month!=True:
                    print("You did not include a month of the year")
                  if has_captcha!=True:
                    print("You did not include the captcha")
                  if has_wordle!=True:
                    print("You did not include the worlde answer")
                  if total_atomic_number !=200:
                    print("You did not have the atomic numbers add up to 200")
                  reset=input("do you want to restart? Y or N")
                else:
                  print()
                  print("you messed up")
                  cap1=random.randint(1,35)
                  cap2=random.randint(1,35)
                  cap3=random.randint(1,35)
                  cap4=random.randint(1,35)
                  cap5=random.randint(1,35)
                  if has_special!=True:
                    print("There were no special characters")
                  if has_upper!=True:
                    print("There were no uppercase letters")
                  if has_digit!=True:
                    print("There were no numbers")
                  if total!=25:
                    print("Your sum did not equal 25")
                  if has_month!=True:
                    print("You did not include a month of the year")
                  if has_captcha!=True:
                    print("You did not include the captcha")
                  if has_wordle!=True:
                    print("You did not include the worlde answer")
                  reset=input("do you want to restart? Y or N")
              else:
                print()
                print("you messed up")
                cap1=random.randint(1,35)
                cap2=random.randint(1,35)
                cap3=random.randint(1,35)
                cap4=random.randint(1,35)
                cap5=random.randint(1,35)
                if has_special!=True:
                  print("There were no special characters")
                if has_upper!=True:
                  print("There were no uppercase letters")
                if has_digit!=True:
                  print("There were no numbers")
                if total!=25:
                  print("Your sum did not equal 25")
                if has_month!=True:
                  print("You did not include a month of the year")
                if has_captcha!=True:
                  print("You did not include the captcha")
                reset=input("do you want to restart? Y or N")
            else:
              print()
              print("you messed up")
              cap1=random.randint(1,35)
              cap2=random.randint(1,35)
              cap3=random.randint(1,35)
              cap4=random.randint(1,35)
              cap5=random.randint(1,35)
              if has_special!=True:
                print("There were no special characters")
              if has_upper!=True:
                print("There were no uppercase letters")
              if has_digit!=True:
                print("There were no numbers")
              if total!=25:
                print("Your sum did not equal 25")
              if has_month!=True:
                print("You did not include a month of the year")
              reset=input("do you want to restart? Y or N")
          else:
           print()
           print("you messed up")
           if has_special!=True:
              print("There were no special characters")
           if has_upper!=True:
              print("There were no uppercase letters")
           if has_digit!=True:
              print("There were no numbers")
           if total!=25:
              print("Your sum did not equal 25")
           reset=input("do you want to restart? Y or N")
       else:
         print()
         print("you messed up")
         if has_special!=True:
            print("There were no special characters")
         if has_upper!=True:
            print("There were no uppercase letters")
         if has_digit!=True:
            print("There were no numbers")
         reset=input("do you want to restart? Y or N")
     else:
      print()
      print("you messed up")
      if has_digit!=True:
        print("There were no numbers")
      if has_upper!=True:
        print("There were no uppercase letters")
      reset=input("do you want to restart? Y or N")
   else:
    print()
    print("you messed up")
    if has_digit!=True:
      print("There were no numbers")
    reset=input("do you want to restart? Y or N")
 else:
  print()
  print("you messed up")
  reset=input("do you want to restart? Y or N")
else:
 print()
 print("you messed up")
 reset=input("do you want to restart? Y or N")