import random
player1_pos = False
player2_pos = False

p1_win_counter = 0
p2_win_counter = 0

def load_scores():
    try:
        with open('Game_Counter.txt', 'r') as file:
            scores = file.readline().split()
            p1_score = int(scores[0])
            p2_score = int(scores[1])
            return p1_score, p2_score
    except FileNotFoundError:
        return 0, 0

def save_scores(p1_score, p2_score):
    with open('Game_Counter.txt', 'w') as file:
        file.write(f"{p1_score} {p2_score}")
    return p1_score + p2_score

def build_board():
    global planets
    with open("Planets.txt", "r") as planet_list:
        planets = [line.strip() for line in planet_list.readlines()]
    global stars
    with open("Stars.txt", "r") as star_list:
        stars = [line.strip() for line in star_list.readlines()]
    global nebulas
    with open("Nebulas.txt", "r") as nebula_list:
        nebulas = [line.strip() for line in nebula_list.readlines()]
    global wormholes
    with open("Wormholes.txt", "r") as wormhole_list:
        wormholes = [line.strip() for line in wormhole_list.readlines()]
    global x_spaces
    x_spaces = [
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
            'Empty Space',
]

    space_values = list(range(2, 50))
#create spaces
    #board = [[{'space_name': 'Start', 'board_pos': 1}], {'space_name': 'WH65', 'board_pos': 2}, {'space_name': 'WH43', 'board_pos': 3}]
    board = []
    for spot in planets + stars + nebulas + x_spaces + wormholes:
        space = []
        space_dic = {}
        space_dic['space_name'] = spot
        num = random.choice(space_values)
        space_values.pop(space_values.index(num))
        space_dic['board_pos'] = num
        space.append(space_dic)
        board.append(space)
    sspace = [
        {'space_name' : 'Start',
        'board_pos' : 1}
    ]
    espace = [
        {'space_name' : 'End',
        'board_pos' : 50}
    ]
    board.insert(0, sspace)
    board.append(espace)
#sort board
    n = len(board)
    for i in range(n):
        for j in range(0, n-i-1):
            if board[j][0]['board_pos'] > board[j+1][0]['board_pos']:
                # Swap the elements without using tuples
                temp = board[j]
                board[j] = board[j+1]
                board[j+1] = temp
    return board

def deck():
    deck = []
    card_move_1 = [{'spaces_to_move' : 1}, {'name' : 'Move 1 space'}]
    card_move_2 = [{'spaces_to_move' : 2}, {'name' : 'Move 2 space'}]
    card_move_3 = [{'spaces_to_move' : 3}, {'name' : 'Move 3 space'}]
    card_move_4 = [{'spaces_to_move' : 4}, {'name' : 'Move 4 space'}]
    card_move_5 = [{'spaces_to_move' : 5}, {'name' : 'Move 5 space'}]

    card_nxt_planet = [{'spaces_to_move' : -3}, {'name' : 'next planet'}]
    card_nxt_nebula = [{'spaces_to_move' : -4}, {'name' : 'next nebula'}]
    card_nxt_star = [{'spaces_to_move' : -5}, {'name' : 'next star'}]
    card_move_neg1 = [{'spaces_to_move' : -1}, {'name' : 'Move back 1 space'}]
    card_move_neg2 = [{'spaces_to_move' : -2}, {'name' : 'Move back 2 space'}]
    card_miss_turn = [{'spaces_to_move' : 0}, {'name' : 'Miss a turn'}]
    card_close_wh = [{'spaces_to_move' : -6}, {'name' : 'close WH'}]
    card_last_planet = [{'spaces_to_move' : -7}, {'name' : 'last planet'}]

    for i in range(1, 11):
        deck.append(card_move_1)
        deck.append(card_move_4)
        deck.append(card_move_5)

    for i in range(1, 16):
        deck.append(card_move_2)
        deck.append(card_move_3)

    for i in range(1,6):
        deck.append(card_nxt_planet)
        deck.append(card_nxt_nebula)
        deck.append(card_nxt_star)
        deck.append(card_move_neg1)
        deck.append(card_move_neg2)
        deck.append(card_miss_turn)
        deck.append(card_close_wh)
        deck.append(card_last_planet)
    
    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0, i - 1)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp

    return deck

def turn(deck):
    deck = deck
    print('Your first card is {} would you like to keep this or draw again'.format(deck[0][1]['name']))
    user_input = int(input('Enter (1) to Keep/Enter (2) to draw again '))
    spaces_t = 0
    while user_input != 1 and user_input != 2:
        print('Please enter 1 or 2')
        print('Your first card is {} would you like to keep this or draw again'.format(deck[0][1]['name']))
        user_input = int(input('Enter (1) to Keep/Enter (2) to draw again '))
    if user_input == 1:
        spaces_t = (deck[0][0]['spaces_to_move'])
        deck.pop(0)

    elif user_input == 2:
        print('Your card is {}'.format(deck[1][1]['name']))
        spaces_t = (deck[1][0]['spaces_to_move'])
        deck.pop(1)

    return spaces_t

def the_game(board):
    global p1_win_counter, p2_win_counter

    p1_win_counter, p2_win_counter = load_scores()


    play_again = 'yes'
    player1_pos = 0
    player2_pos = 0

    while play_again == 'yes':
        board = board
        #[[{'space_name': 'Start', 'board_pos': 1}], {'space_name': 'WH65', 'board_pos': 2}, {'space_name': 'WH43', 'board_pos': 3}]
        deck_current = deck()
        #move_1 = [{'spaces_to_move' : 1}, {'name' : 'Move 1 space'}]

        while player1_pos < 50 and player2_pos < 50:#player1_pos and not player2_pos
            print('Player 1 Turn')
            wormhole = False
            spaces = turn(deck_current)
            if spaces < -2:
                if spaces == -3:
                    for spot in range(player1_pos, len(board)):
                        if board[spot][0]['space_name'] in planets:
                            spaces = spot - player1_pos
                            break
                if spaces == -4:
                    for spot in range(player1_pos, len(board)):
                        if board[spot][0]['space_name'] in nebulas:
                            spaces = spot - player1_pos
                            break
                if spaces == -5:
                    for spot in range(player1_pos, len(board)):
                        if board[spot][0]['space_name'] in stars:
                            spaces = spot - player1_pos
                            break
                if spaces == -6:
                    wormhole = True
                    board1 = board[player1_pos + 1:]
                    board2 = board[:player1_pos]
                    for spot in range(1, len(board1)):
                        if board1[spot][0]['space_name'] in wormholes:
                                whspaces = board1[spot][0]['board_pos']
                                if player1_pos == 0:
                                    distance_r = whspaces - player1_pos - 1
                                else:
                                    distance_r = whspaces - player1_pos
                                break
                    if player1_pos > 0:
                        for spot in range(len(board2) - 1, 0, -1):
                            if board2[spot][0]['space_name'] in wormholes:
                                    whspaces = board2[spot][0]['board_pos']
                                    distance_l = whspaces - player1_pos
                                    break
                            else:
                                distance_l = len(board)
                    else:
                        spaces = distance_r
                    if player1_pos != 0:
                        if abs(distance_l) <= distance_r:
                            spaces = distance_l
                        else:
                            spaces = distance_r
                    else:
                            spaces = distance_r
                if spaces == -7:
                    board2 = board[:player1_pos]
                    len(board2) - 1, 0, -1
                    for spot in range(len(board2) - 1, 0, -1):
                        if board[spot][0]['space_name'] in planets:
                            spaces = spot - player1_pos
                            break
                        else:
                            spaces = 0

            print(board[player1_pos][0]['space_name'], board[player1_pos][0]['board_pos'])
            if wormhole and player1_pos > 0:
                player1_pos -= 1

            if wormhole:
                print('Teleporting...')
                worm_name = board[player1_pos + spaces][0]['space_name']
                for spot in range(len(board)):
                    if worm_name == board[spot][0]['space_name'] and board[player1_pos + spaces][0]['board_pos'] != board[spot][0]['board_pos']:
                        player1_pos = spot
                        spaces = 0
                        break


            if player1_pos + spaces >= len(board):
                break

            else:
                try:
                    print(board[player1_pos + spaces][0]['space_name'], board[player1_pos + spaces][0]['board_pos'])
                    player1_pos += spaces
                except:
                    print(board[0][0]['space_name'], board[0][0]['board_pos'])
                    player1_pos == 0



            print('Player 2 Turn')
            wormhole = False
            spaces = turn(deck_current)
            if spaces < -2:
                if spaces == -3:
                    for spot in range(player2_pos, len(board)):
                        if board[spot][0]['space_name'] in planets:
                            spaces = spot - player2_pos
                            break
                if spaces == -4:
                    for spot in range(player2_pos, len(board)):
                        if board[spot][0]['space_name'] in nebulas:
                            spaces = spot - player2_pos
                            break
                if spaces == -5:
                    for spot in range(player2_pos, len(board)):
                        if board[spot][0]['space_name'] in stars:
                            spaces = spot - player2_pos
                            break
                if spaces == -6:
                    wormhole = True
                    board1 = board[player2_pos + 1:]
                    board2 = board[:player2_pos]
                    for spot in range(1, len(board1)):
                        if board1[spot][0]['space_name'] in wormholes:
                                whspaces = board1[spot][0]['board_pos']
                                if player2_pos == 0:
                                    distance_r = whspaces - player2_pos - 1
                                else:
                                    distance_r = whspaces - player2_pos
                                break
                    if player2_pos > 0:
                        for spot in range(len(board2) - 1, 0, -1):
                            if board2[spot][0]['space_name'] in wormholes:
                                    whspaces = board2[spot][0]['board_pos']
                                    distance_l = whspaces - player2_pos
                                    break
                        else:
                            distance_l = len(board)
                    else:
                        spaces = distance_r
                    if player2_pos != 0:
                        if abs(distance_l) <= distance_r:
                            spaces = distance_l
                        else:
                            spaces = distance_r
                    else:
                            spaces = distance_r
                if spaces == -7:
                    board2 = board[:player_pos_i]
                    len(board2) - 1, 0, -1
                    for spot in range(len(board2) - 1, 0, -1):
                        if board[spot][0]['space_name'] in planets:
                            spaces = spot - player_pos_i
                            break
                        else:
                            spaces = 0

            print(board[player2_pos][0]['space_name'], board[player2_pos][0]['board_pos'])

            if wormhole and player2_pos > 0:
                player2_pos -= 1

            if wormhole:
                print('Teleporting...')
                worm_name = board[player2_pos + spaces][0]['space_name']
                for spot in range(len(board)):
                    if worm_name == board[spot][0]['space_name'] and board[player2_pos + spaces][0]['board_pos'] != board[spot][0]['board_pos']:
                        player2_pos = spot
                        spaces = 0
                        break


            if player2_pos + spaces >= len(board):
                break
            try:
                print(board[player2_pos + spaces][0]['space_name'], board[player2_pos + spaces][0]['board_pos'])
                player2_pos += spaces
            except:
                print(board[0][0]['space_name'], board[0][0]['board_pos'])
                player2_pos == 0


        if player1_pos >= 50:
            print('Player 1 has reached the end')
            print('Player 1 Wins')
            p1_win_counter += 1
        else:
            print('Player 2 has reached the end')
            print('Player 2 Wins')
            p2_win_counter += 1
        save_scores(p1_win_counter, p2_win_counter)
        print('Total score - Player 1 win(s): {}, Player 2 win(s) {}.'.format(p1_win_counter, p2_win_counter))

        play_again = (input('Would you like to play again(Yes/No) ')).lower()
        while play_again != 'yes' and play_again != 'no':
            print('Please Enter Yes/No')
            play_again = (input('Would you like to play again(Yes/No) ')).lower()
        if play_again == 'yes':
            player1_pos = 0
            player2_pos = 0
        else:
            break
        pass
    print('Game Done')
    print('Saving data and exiting.')





