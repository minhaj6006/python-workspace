from pathlib import Path # for checking file exist or not

master_file = "available_courses.txt"
print('**************************************')
print('*         Welcome to the CMS         *')
print('**************************************')
user_name = input('Register your self by your name: ')
data=[user_name]
X=[] # initialize list to store registered courses

if Path('{0}.txt'.format(data[0])).is_file(): # checking file exist
    file = open('{0}.txt'.format(data[0]),"r") #{0} using for read file name by username
    X = [line.rstrip('\n') for line in open(data[0] + ".txt" )] # this point text file convert into list
    print('\n--------------------')
    print('Already Registered')
    print('Welcome Back ' + user_name)
else:
    file = open('{0}.txt'.format(data[0]),"w") #{0} using for write file name by username
    print('\n---------------')
    print('Welcome  ' + user_name)

b=True
while (b):
    print('\n************ Main Menu ************')
    print('-----------------------------------')
    print('1. Register Courses. \n2. Drop Courses. \n3. List Registered Courses.\n4. Exit Registration Program.')
    print('-----------------------------------')
    option1 = '1'
    option2 = '2'
    option3 = '3'
    option4 = '4'
    user_input = input('Select your option: ')

    if user_input == option1: # Register Courses
        z = [line.rstrip('\n') for line in open(master_file)] # this point text file convert into list line by line

        x=True
        while (x):
            if Path(master_file).is_file(): # checking file exist
                open(master_file, "r")
                print('\nPlease select the following course:')
                print('{:30s} {}'.format("Offered Courses","Regeistered Courses"))
                print('{:30s} {}'.format('---------------','-------------------'))

                j=0
                c = 0
                for i in z: # this loop using for add numbering
                    c += 1
                    print('{}. {:27s} '.format(c,i), end="") # end=''means after the print statement
                    if j == len(X):
                        print()
                        continue #The continue statement in Python returns the control to the beginning of the while loop or for loop
                    else:
                        print('', end="") # end=''means after the print statement
                        print('{}. {} '.format(c,X[j]))
                        j += 1

                sel_c = input("Please Enter The course No. OR type y to Main Menu: ")
                #file = open('{0}.txt'.format(data[0]),"a") # this point text file open to append the values

                if(sel_c == 'y'):
                    break

                if(bool(sel_c) == False):
                    print('\n------------------------------')
                    print("Please Select between 1 to 6")
                    print('------------------------------')
                    continue #The continue statement in Python returns the control to the beginning of the while loop or for loop

                if(int(sel_c)):
                    sel_c = int(sel_c)
                    file = open('{0}.txt'.format(data[0]),"a") # this point username text file open to append the values

                    if(len(X) == 5):
                        print('\n--------------------------------------')
                        print('Only 5 courses are allowed to register')
                        print('--------------------------------------')
                        break

                    if(sel_c < 0 or sel_c > 6 ):
                        print("Please Select between 1 to 6")

                    if (sel_c == 1 and z[0] not in X):
                        file.write(str("%s\n" % z[0]))
                        X.append(z[0])
                        print('Registered Successfully In ' + z[0])
                    elif (sel_c == 1 and z[0] in X):
                        print(''.join(z[0]), end=": Already registered \n" ) #end=''means after the print statement
                    if (sel_c == 2 and z[1] not in X):
                        file.write(str("%s\n" % z[1]))
                        X.append(z[1])
                        print('Registered Successfully In ' + z[1])
                    elif (sel_c == 2 and z[1] in X):
                        print(''.join(z[1]), end=": Already registered \n" ) #end=''means after the print statement
                    if (sel_c == 3 and z[2] not in X):
                        file.write(str("%s\n" % z[2]))
                        X.append(z[2])
                        print('Registered Successfully In ' + z[2])
                    elif (sel_c == 3 and z[2] in X):
                        print(''.join(z[2]), end=": Already registered \n" ) #end=''means after the print statement
                    if (sel_c == 4 and z[3] not in X):
                        file.write(str("%s\n" % z[3]))
                        X.append(z[3])
                        print('Registered Successfully In ' + z[3])
                    elif (sel_c == 4 and z[3] in X):
                        print(''.join(z[3]), end=": Already registered \n" ) #end=''means after the print statement
                    if (sel_c == 5 and z[4] not in X):
                        file.write(str("%s\n" % z[4]))
                        X.append(z[4])
                        print('Registered Successfully In ' + z[4])
                    elif (sel_c == 5 and z[4] in X):
                        print(''.join(z[4]), end=": Already registered \n" ) #end=''means after the print statement
                    if (sel_c == 6 and z[5] not in X):
                        file.write(str("%s\n" % z[5]))
                        X.append(z[5])
                        print('Register Successfully In ' + z[5])
                    elif (sel_c == 6 and z[5] in X):
                        print(''.join(z[5]), end=": Already registered \n" ) #end=''means after the print statement

                a = int(input('Press 1 for Add more course & press 2 for Main Menu: '))
                if (a == 1):
                    x = True
                else:
                    break

    if user_input == option2: # this point remove/drop courses
        if not X:
            print('-----------------------------------------------')
            print('Registered in any course before select option 2')
            print('-----------------------------------------------')
        else:
            file = open('{0}.txt'.format(data[0]),'r')
            print('\nYou are registered in these courses:')
            print('------------------------------------')
            j = 0
            for i in X: # this loop using for add numbering
                j += 1
                print(' '.join([str(j),i]) )
            sel_c = (input("\nPlease select the course to unregistered OR Press y to Main Menu: "))
            file = open('{0}.txt'.format(data[0]),'a')
            if(sel_c == 'y'):
                continue #The continue statement in Python returns the control to the beginning of the while loop or for loop

            elif(int(sel_c)): # reinitialize variable string to integer
                sel_c = int(sel_c)

            if (sel_c == 1):
                print('\nSuccessfully Unregistered ' + X[0])
                del X[0]
            elif (sel_c == 2):
                print('\nSuccessfully Unregistered ' + X[1])
                del X[1]
            elif (sel_c == 3):
                print('\nSuccessfully Unregistered ' + X[2])
                del X[2]
            elif (sel_c == 4):
                print('\nSuccessfully Unregistered ' + X[3])
                del X[3]
            elif (sel_c == 5):
                print('\nSuccessfully Unregistered ' + X[4])
                del X[4]
            file = open('{0}.txt'.format(data[0]),"w")
            if(len(X) == 1):
                file.write(str("%s\n" %X[0]))
            elif(len(X) == 2):
                file.write(str("%s\n" %X[0]))
                file.write(str("%s\n" %X[1]))
            elif(len(X) == 3):
                file.write(str("%s\n" %X[0]))
                file.write(str("%s\n" %X[1]))
                file.write(str("%s\n" %X[2]))
            elif(len(X) == 4):
                file.write(str("%s\n" %X[0]))
                file.write(str("%s\n" %X[1]))
                file.write(str("%s\n" %X[2]))
                file.write(str("%s\n" %X[3]))
            file.close()

    elif user_input == option3: # View registered courses
        if not X:
            print('-----------------------------------------------')
            print('Registered in any course before select option 3')
            print('-----------------------------------------------')
        else:
            print('\nYou are registered in these courses:')
            print('------------------------------------')
            j = 0
            for i in X: # this loop using for add numbering
                j += 1
                print(' '.join([str(j),i]) )
            print('------------------------------------\n')
            a=int(input('Press 1 for Main Menu: '))
            if (a==()):
                continue #The continue statement in Python returns the control to the beginning of the while loop or for loop

    elif user_input == option4: # this point exit program
        print('----------------------------')
        print('Thank you for using our CMS\n')
        break