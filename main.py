import Running_Through_Space as Run

def game_runner():
    board = Run.build_board()
    output = ''
    for spot in board:
        output += '{} {}->  '.format(spot[0]['space_name'], spot[0]['board_pos'])
    print(output)

    Run.the_game(board)
    #5 tests
    #writing/drawing portion

def main():
    game_runner()

if __name__ == '__main__':
    main()