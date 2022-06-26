board = [" " for _ in range(9)]
win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def print_board(board):
    for i, v in enumerate(board):
        if (i + 1) % 3 == 0:
            print(f"{v}")
        else:
            print(f"{v}", end="|")


def check_winner(board, combinations):
    for (x, y, z) in combinations:
        if board[x] == board[y] and board[y] == board[z] and (board[x] == "X" or board[x] == "O"):
            return board[x]
    return ""


def check_tie(board):
    counter = 0
    for i in board:
        if i == " ":
            counter += 1
    if counter == 0:
        return f"Ничья!"
    return ""


def play_game(board):
    current_sign = "X"
    current_player = "Игрок 1"
    print_board(board)
    while not check_winner(board, win_combinations) and not check_tie(board):
        try:
            index = int(input(f"{current_player}. Куда поставить знак {current_sign}? от 1 до 9 : "))
            if board[index - 1] != " ":
                print("А так нельзя, друг. Выбери другое поле! ( ╯°□°)╯ ┻━━┻ ")
                continue
            elif index == 0:
                raise IndexError
        except (ValueError, IndexError):
            print("Нужно ввести число от 1 до 9!")
            continue
        board[index - 1] = current_sign
        print_board(board)
        winner_sign = check_winner(board, win_combinations)
        tie_game = check_tie(board)
        if winner_sign:
            print(f"Победитель у нас {current_player} со знаком {winner_sign} ! ＼(＾∀＾)メ(＾∀＾)ノ\nЗавершение программы...")
        elif tie_game:
            print("Ничья. Победила дружба! ＼(＾∀＾)メ(＾∀＾)ノ\nЗавершение программы...")
        current_sign = "X" if current_sign == "O" else "O"
        current_player = "Игрок 1" if current_sign == "X" else "Игрок 2"


if __name__ == "__main__":
    play_game(board)
