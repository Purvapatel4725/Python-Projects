import random
def choose_rand():
    wordList = ["Purva", "Purvam", "Niya"]
    word = random.choice(wordList)
    return word

def shuffle_letters():
    original_word = choose_rand()
    shuffleList = random.sample(original_word, k = len(original_word))
    shuffleWord = ""
    for i in shuffleList:
        shuffleWord += i
    return original_word,shuffleWord

def play_game():
    user1 = input("Player1 enter your name:")
    if user1.lower() == "stop" or user1.lower() == "exit":
        return "none","none"    #used to return two values as when function is called it needs 2 values assigned
    user2 = input("Player2 enter your name:")
    if user2.lower() == "stop" or user2.lower() == "exit":
        return "none","none"
    return user1,user2

def guess(guess):
    count = 0
    temp = guess.lower()
    word = list(temp)
    alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in word:
        if i in alpha_list:
            count += 1
    if count != len(word):
        return True
    else:
        return False

def choose_turn(turn,user1,user2):
    if turn % 2 == 0:
        print(user1, "your turn")
        word = input(f'{user1} your answer is:')
        while guess(word):
            print("Incorrect format! Please enter the correct format (only alphabets)")
            word = input(f'{user1} your answer is:')
        return word
    else:
        print(user2, "your turn")
        word1 = input(f'{user2} your answer is:')
        while guess(word1):
            print("Incorrect format! Please enter the correct format (only alphabets)")
            word1 = input(f'{user2} your answer is:')
        return word1

def print_score(turn,score1,score2):
    print(f'Your score:{score1}') if turn % 2 == 0 else print(f'Your score:{score2}')


score1,score2 = 0,0
print("Welcome to Two-Player-Jumbled-Words Game")
while True:
    user1, user2 = play_game()
    if user1 == "none" or user2 == "none": #Used to break when user enters stop or break
        print("Game Ends!")
        break
    turn = 0
    while True:
        original_word , jumbled_word = shuffle_letters()
        print("Jumbled word is:", jumbled_word)
        word = choose_turn(turn,user1,user2)
        if original_word == guess:
            print("Right Answer!")
            if turn % 2 == 0:
                score1 += 1
            else:
                score2 += 1
            print_score(turn,score1,score2)
            turn += 1
        elif guess.lower() == "stop" or guess.lower() == "exit":
            print("Game Ends!")

        else:
            print("You are wrong!")
            print_score(turn, score1, score2)
            turn += 1







