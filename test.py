# import json

# usen = '@yechiel'
# def Open_Game():
#     class Game:
#         def __init__(self, name, date, time, players):
#             self.name = name
#             self.date = date
#             self.time = time
#             self.players = players
            
    
#         def to_dict(self):
#             return {
#                 "name": self.name,
#                 "date": self.date,
#                 "time": self.time,
#                 "players": self.players,
#             }
       
#     name = input("please choose a name ")
#     date = input("please choose a date ")
#     time = input("please choose a time ")
#     players = usen
#     new_game = Game(name, date, time, players,)
#     try:
#         with open("games.json", "r") as f:
#             data = f.read()
#             if len(data) > 0:
#                 games = json.loads(data)
#             else:
#                 games = []
#     except FileNotFoundError:
#         games = []
#     games.append(new_game.to_dict())
#     with open("games.json", "w") as f:
#         json.dump(games, f, indent=4)



# with open('games.json') as f:
#     data = json.load(f)
# for obj in data: 
#     if obj['date'] == "thursday":
#         print(obj['name'])


#    if ['date'] == "thursday":
#        print(obj["name"])
# print(obj['name'])


# fix: when you enter the game it should write your username in the last line of the file.
usen = "@yechiel"


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
                with open(os.path.join(directory, filename), 'r') as file5:
                    for line in file5:
                        x = len(file5.readlines())
                #first_line = file2.readline().strip()
                        line2 = file.readlines()
                        address2 = line2[4]
                        if address1 == address2 and x < 10:
                            lines = file2.readlines()
                            line3 = file3.readlines()
                            print("Type the game name to join\n")
                            print(lines[1][2:100] + '\n' 'game at ' + line3[3][1:100] + '\n')
                            for filename in os.listdir('/Users/macbookpro/Playinn/open_games'):
                                enter_game = '#' + input("") + '.py'
                                if enter_game in filename:
                                    with open(f'/Users/macbookpro/Playinn/open_games/{enter_game}','a', encoding='utf-8') as f:
                                        # check if the file has 10 username writen if yes print full if not continue.
                                        f.write(f'#{usen}' + '\n') 
                                        
                                        print("you are now in the game")
                                else:
                                    print("no")    
                        else:
                            print('There are no games in your area please check back soon')

game_alg()

                        # with open(os.path.join(directory, filename), 'r') as file:
                        #     x = len(file.readlines())
                        #     if x < 10:
                        #         print("works")

print("hello")                        