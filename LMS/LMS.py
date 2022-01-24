from pathlib import Path
import smtplib
import time
import datetime

available_books = ["Harry Potter",
                   'The Twilight Saga',
                   "The Lord of the Rings",
                   "The Hobbit","The Top Ten",
                   "The Great Gatsby",
                   "Steve Jobs",
                   "Long Walk to Freedom",]

a_books = [line.rstrip('\n') for line in (available_books)]
# msg = 'Please return the book as soon as posible and '
username = 'librarykarachi@gmail.com'
password = '0000Qwerty'
# server = smtplib.SMTP('smtp.gmail.com: 587')
# server.starttls()
# server.login(username , password)

print('*************************************')
print('*     Library Management System     *')
print('*************************************')
ask_name = input('\nRegister your self by name: ')
ask_email = input('enter your email: ')
name_data = [ask_name] # store user naem
email_data = [ask_email] # store user email
fromaddr = 'librarykarachi@gmail.com'
toaddrs  = ('{0}'.format(email_data[0]))
msg = 'Please return the book as soon as posibale and your fine is Rupees 10'
store_time = []
select_books = []

if Path('{0}.txt'.format(name_data[0])).is_file(): # checking file exist
    file = open('{0}.txt'.format(name_data[0]),"r")
    i = 1
    print('\n--------------------')
    print('Welcome Back ' + ask_name)
    print('--------------------\n')
    for line in file.readlines():
        if i % 2 == 0:
            store_time.append(line.rstrip('\n'))
        else:
            select_books.append(line.rstrip('\n'))
        i += 1

else:
    file = open('{0}.txt'.format(name_data[0]),"w")
    print('\n---------------')
    print('Welcome  ' + ask_name)
    print('---------------\n')

b=True
while (b):

    for i in store_time:
        if float(i) + 60*60 > time.time():
            timeexceed = False
        else:
            # print('return books. Your rent time is over')
            timeexceed = True
            # server.sendmail(fromaddr, toaddrs, msg)
            continue

    print('************ Main Menu ************')
    print('-----------------------------------')
    print('1. Checkout Book. \n2. Return Book. \n3. Show Rented Books. \n4. Exit Program.')
    print('-----------------------------------')
    option1 = '1'
    option2 = '2'
    option3 = '3'
    option4 = '4'
    choose_option = input('Select your option: ')

# option 1 Checkout Book
    if choose_option == option1:
        if(len(select_books) == 3):
            print('\n----------------------------')
            print('Only 3 books allowed to pick')
            print('----------------------------')
            continue
        # elif timeexceed == True:
        #     continue #The continue statement in Python returns the control to the beginning of the while loop or for loop
        else:
            file = open('{0}.txt'.format(name_data[0]),"a")
            count = 0
            print('\n    Available Books ')
            print('-----------------------')
            for i in a_books: # this loop using for add numbering
                count += 1
                print(' '.join([str(count),i]) )
            print('-----------------------\n')

            b_select = int(input('Select the book: '))

            if (b_select == 1 and a_books[0] not in select_books):
                file.write(str("%s\n" % a_books[0]))
                select_books.append(a_books[0])
                print(a_books[0] +' Checkout')
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% '{0}'.format(rent)))
            elif (b_select == 1 and a_books[0] in select_books):
                print('\nYou are already rented this book')

            if (b_select == 2 and a_books[1] not in select_books):
                file.write(str("%s\n" % a_books[1]))
                select_books.append(a_books[1])
                print(a_books[1] +' Checkout')
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% '{0}'.format(rent)))
            elif (b_select == 2 and a_books[1] in select_books):
                print('\nYou are already rented this book')

            if (b_select == 3 and a_books[2] not in select_books):
                file.write(str("%s\n" % a_books[2]))
                select_books.append(a_books[2])
                print(a_books[2] +' Checkout')
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% '{0}'.format(rent)))
            elif (b_select == 3 and a_books[2] in select_books):
                print('\nYou are already rented this book')

            if (b_select == 4 and a_books[3] not in select_books):
                file.write(str("%s\n" % a_books[3]))
                select_books.append(a_books[3])
                print('rent' + a_books[3])
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% '{0}'.format(rent)))
            elif (b_select == 4 and a_books[3] in select_books):
                print('\nYou are already rented this book')

            if (b_select == 5 and a_books[4] not in select_books):
                file.write(str("%s\n" % a_books[4]))
                select_books.append(a_books[4])
                print('rent' + a_books[4])
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% '{0}'.format(rent)))
            elif (b_select == 5 and a_books[4] in select_books):
                print('\nYou are already rented this book')

            if (b_select == 6 and a_books[5] not in select_books):
                file.write(str("%s\n" % a_books[5]))
                select_books.append(a_books[5])
                print('rent' + a_books[5])
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% '{0}'.format(rent)))
            elif (b_select == 6 and a_books[5] in select_books):
                print('\nYou are already rented this book')

            if (b_select == 7 and a_books[6] not in select_books):
                file.write(str("%s\n" % a_books[6]))
                select_books.append(a_books[6])
                print('rent' + a_books[6])
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% '{0}'.format(rent)))
            elif (b_select == 7 and a_books[6] in select_books):
                print('\nYou are already rented this book')

            if (b_select == 8 and a_books[7] not in select_books):
                file.write(str("%s\n" % a_books[7]))
                select_books.append(a_books[7])
                print('rent' + a_books[7])
                rent = time.time()
                store_time.append('{0}'.format(rent))
                file.write(str('%s\n'% '{0}'.format(rent)))
            elif (b_select == 8 and a_books[7] in select_books):
                print('\nYou are already rented this book')

# option 2 Return Book
    elif choose_option == option2:
        if not select_books:
            print('---------------------------------------')
            print('Checkout the book before select option 2')
            print('---------------------------------------')
        else:
            print('\nYou Rented these Books:')
            print('-----------------------')
            j = 0
            for i in select_books:
                j += 1
                print(' '.join([str(j),i]) )
            ask_to_r = (int(input("\nSelect the book to return AND Press 0 to Return all books: ")))
            now = datetime.datetime.now()
            if ask_to_r == 0:
                select_books = []
                store_time = []
                file = open('{0}.txt'.format(name_data[0]),'w')
            elif (ask_to_r == 1):
                print('\n',select_books[0],end=" return at ")
                print (now.strftime("%d-%m %H:%M"))
                del select_books[0]
                del store_time[0]
            elif (ask_to_r == 2):
                print(select_books[1],end=" return at ")
                print (now.strftime("%d-%m- %H:%M"))
                del select_books[1]
                del store_time[1]
            elif (ask_to_r == 3):
                print(select_books[2],end=" return at ")
                print (now.strftime("%d-%m %H:%M"))
                del select_books[2]
                del store_time[2]
        if(len(select_books) == 1):
            file.write(str("%s\n" %select_books[0]))
            file.write(str('%s\n' %store_time[0]))
        elif(len(select_books) == 2):
            file.write(str("%s\n" %select_books[0]))
            file.write(str('%s\n' %store_time[0]))
            file.write(str("%s\n" %select_books[1]))
            file.write(str('%s\n' %store_time[1]))


# option3 Show rent book
    elif choose_option == option3:
        if not select_books:
            print('----------------------------------------')
            print('Checkout the Book before select option 3')
            print('----------------------------------------')
        else:
            print('\n')
            s_books = [line.rstrip('\n') for line in (select_books)]
            count = 0
            print('{:29s} {:26s} {}'.format('   Your Rented Books','Book Checkout Time','Book Return Time'))
            print('{:28s} {:25s} {}'.format('-----------------------','--------------------','--------------------'))
            for i in s_books: # this loop using for add numbering
                print('{}. {:25s} '.format(count+1,i), end="")
                print('{:25s} '.format(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(float(store_time[count])))), end="")
                print('{:20s} '.format(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(float(store_time[count])+ 60*60)) ))
                count += 1

            r = (int(input("\npress 1 to return Main Menu and press 0 to exit: ")))
            if r == 1:
                continue
            elif r == 0:
                break

# option 4 exit
    elif choose_option == option4: # this point exit program
        print('\n---------------------------')
        print('Thank you for using our LMS\n')
        file.close()
        server.quit()
        break