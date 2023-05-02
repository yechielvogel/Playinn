
def Opening_Page():
    print("\n")
    print("Welcome to Playinn, please choose from the following options.\n")
    print("Login")
    print("Create Account\n")
    selection = input("").strip().title()
    if selection == "Login":
        Login()
    elif selection == "Create Account":
        Create_Account()    
    else:
        print("\nSorry I didnt get that please try again") 
        Opening_Page()

# fix bug where if you enter wrong username it crashes. try add the try and exept method to tihs see if it will work.
# try make that fitst it searches the directry (playinn) then it opens the file

def Login():
    import os
    print("Please log into your account\n")
    global usen
    directory = '/Users/macbookpro/Playinn'
    usen = ('@') + input("Username @")
    pasw = input("Password ")
    if usen + ".py" in os.listdir(directory):
        while pasw == "":
            print('The Username or Password is incorrect. Please try again.\n')
            Login()
        with open(f'/Users/macbookpro/Playinn/{usen}.py', 'r') as file: 
            content = file.read()
            while pasw in content:
                print('Welcome\n')
                exec(open(f'/Users/macbookpro/Playinn/{usen}.py').read())
            else:
                print('The Username or Password is incorrect. Please try again.\n')
                Login()
    else:
        print('The Username or Password is incorrect. Please try again.\n')
        Login()



def Create_Account():
   global name
   global filename
   name = input("Welcome to Playinn please enter your name to begin ")
   email = input("email ")
   username = ('@') + input("Please choose a username @")
   phone_number = input("Phone number ")
   password = input("Please choose a password ")
   filename = username

# Eventually change this to creat a class in the new file so user could eisily change their name passsword ect...
# and load all data into a json file.  

   with open(f'/Users/macbookpro/Playinn/{filename}.py','w', encoding='utf-8') as f:
    f.write(f'#Avalible' + '\n')
    f.write(f'#{email}' + '\n')
    f.write(f'#{username}' + '\n')
    f.write(f'#{name}' + '\n')
    f.write(f'#{phone_number}' + '\n')
    f.write(f'#{password}' + '\n')
    f.write(f'#test' + '\n')
    f.write(f'########' + '\n')
    f.write(f'' + '\n')
    f.write(f'from Playinn import Home' + '\n')
    f.write(f'Home()' + '\n')
    f.close()
    print("Account sucsesfully created Please open the app again to login\n")
    Login()
        
# fix bug where it automaticly brings you back to the Home()

def Home():   
    f = open(f'/Users/macbookpro/Playinn/{usen}.py')
    lines = f.readlines()
    print("Hello " + lines[3][1:100])
    print("Account: " + "Profile: " + "Settings: " + "Avalible: " + "Log Out:" + "\n")
    AvalibleAlg()
    selection = input("").strip().title()
    if selection == "Account":
        Account()
    elif selection == "Profile":
        Profile()
    elif selection == "Settings":
        Settings()
    elif selection == "Logout":
        Log_Out()
    elif selection == "Avalible":
        Avalible()
    else:
        print('Sorry I didnt get that please try again.') 
              
# clean out all none functional functions

def Account(): 
    print("This page has not been built yet please come back soon\n")
    print("Setup Account:\n")
    selection = input("").strip().title()
    if selection == "Setup Account":
        Account_Setup()

def Account_Setup():
    Address = input("Post code_")
    with open(f'/Users/macbookpro/Playinn/{filename}.py','w', encoding='utf-8') as f:
        f.write(f'#{Address}' + '\n')    


def Settings():
    print(' ')
    print('Location\n')
    selection = input("")
    if selection == "location":
        with open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+') as file:
            content = file.readlines()
            print(content[7][1:100])
            selection2 = input('Change Location\n')
            while len(selection) < 7:
                print('Please enter a valid postcode')
            if selection2 == 'change location':
                with open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+') as file2:
                    lines = file2.readlines()
                    lines[7] = '#' + input("").upper() + "\n"
                    with open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+') as file2:
                        file2.writelines(lines)
                        print("sucsessfully updated")
            else:
                print("Sorry I didnt get that please try again")
    else:
        selection == "back"
        Home() 

def Log_Out():
    print('You have loged out sucsessfuly')
    Opening_Page()           

def Profile():    
    print("This page has not been built yet please come back soon\n")

# eventually change this to show games in the area which you could then join 

def AvalibleAlg():
    import os 
    directory = '/Users/macbookpro/Playinn'
    search_word = '#Avalible'
    f = open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+')
    line = f.readlines()
    address1 = line[7]
    exclude_file1 = (f'{usen}.py')
    exclude_file2 = ('/Users/macbookpro/Playinn/Playinnn_Opening_Page.py')
    exclude_file3 = ('/Users/macbookpro/Playinn/test.py')
    exclude_file4 = ('/Users/macbookpro/Playinn/Playinn.py')
    exclude_file5 = ('/Users/macbookpro/Playinn/games.json')
    for filename in os.listdir('/Users/macbookpro/Playinn'):
        if filename.endswith('.py') and filename != exclude_file1 != exclude_file2 != exclude_file3 != exclude_file4 != exclude_file5:
            with open(os.path.join(directory, filename), 'r') as file,  open(os.path.join(directory, filename), 'r') as file2, open(os.path.join(directory, filename), 'r') as file3:
                first_line = file2.readline().strip()
                line2 = file.readlines()
                address2 = line2[7]
                if address1 == address2 and search_word in first_line:
                    lines = file2.readlines()
                    line3 = file3.readlines()
                    print(lines[1][1:100] + 'is avalible contact him at ' + line3[4][1:100] + '\n')
                    
def Avalible():
    print(' ')
    print('On:')
    print('Off:')
    selection = input("")
    if selection == "on":
        with open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+') as file:
            content = file.read()
            print("You are now avalible")
        if '#Avalible' in content:    
            print("Avalible is already on\n")
        else:
            with open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+') as file:     
                file.write('#Avalible')    
                print("You are now avalible\n")
    elif selection == "off":
        with open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+') as file:
            content = file.read()
        if '#########' in content:
            print("Avalible is already off")    
        else:
            with open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+') as file:
                file.write('#########')
                print("You are not Avalible anymore")
             
def No_One_Online():
    print('No one is online')       

# make date and time real somehow.

def open_game():
    game_name = ("#") + input("Choose a name ")
    game_date = input("Choose a date ")
    game_time = input("Choose a time ")
    game_area = input("Choose a area ")
#    players = usen
    file_name = game_name
    with open(f'/Users/macbookpro/Playinn/open_games/{file_name}.py','w', encoding='utf-8') as f:
        f.write(f'#...................' + '\n')
        f.write(f'#{game_name}' + '\n')
        f.write(f'#{game_date}' + '\n')
        f.write(f'#{game_time}' + '\n')
        f.write(f'#{game_area}' + '\n')
#       f.write(f'#{players}' + '\n')

# fix: when you enter the game it should write your username in the last line of the file.
# add: alg that only desplayes games happening today, eventually it should know what day is is.
def game_alg():
    today = "thursday"
    import os 
    directory = '/Users/macbookpro/Playinn/open_games'
    #search_word = today
    f = open(f'/Users/macbookpro/Playinn/{usen}.py', 'r+')
    line = f.readlines()
    address1 = line[7]
    for filename in os.listdir('/Users/macbookpro/Playinn/open_games'):
        if filename.endswith('.py'):
            with open(os.path.join(directory, filename), 'r') as file,  open(os.path.join(directory, filename), 'r') as file2, open(os.path.join(directory, filename), 'r') as file3:
                #first_line = file2.readline().strip()
                line2 = file.readlines()
                address2 = line2[4]
                if address1 == address2:
                    lines = file2.readlines()
                    line3 = file3.readlines()
                    print("Type the game name to enter\n")
                    print(lines[0][2:100] + '\n' 'game at ' + line3[3][1:100] + '\n')
                    for filename in os.listdir('/Users/macbookpro/Playinn/open_games'):
                        enter_game = '#' + input("") + '.py'
                        if enter_game in filename:
                            with open(f'/Users/macbookpro/Playinn/open_games/{enter_game}','r+', encoding='utf-8') as f:
                                # check if the file has 10 username writen if yes print full if not continue.
                               f.write(f'#{usen}' + '\n') 
                               
                               print("you are now in the game")
                        else:
                            print("no")    
                else:
                    print('There are no games in your area please check back soon')



