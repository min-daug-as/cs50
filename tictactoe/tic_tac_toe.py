from tabulate import tabulate
import random


def main():
    state = init_state(3)
    print_state(state)

    while move_exists(state):
        x, y = user_input(state)
        update_state(state, "X", x, y)
        print_state(state)

        if is_winner(state, "X"):
            print("You won the game!")
            break

        if not move_exists(state):
            break

        x, y = computer_input(state)
        update_state(state, "O", x, y)
        print(f"Computer turn: {x},{y}")
        print_state(state)

        if is_winner(state, "O"):
            print("Computer won the game!")
            break

    print("Game over!")


def init_state(table_size):
    return [["" for _ in range(table_size)] for _ in range(table_size)]


def print_state(state):
    print(tabulate(state, tablefmt="simple_grid"))


def update_state(state, player, x, y):
    state[y][x] = player


def move_exists(state):
    for row in state:
        for cell in row:
            if cell == "":
                return True

    return False


def is_move_valid(state, x, y):
    try:
        return state[y][x] == ""
    except:
        return False


def is_winner_cols(state, player):
    table_size = len(state)

    for col_index in range(table_size):
        for row_index in range(table_size):
            if state[row_index][col_index] != player:
                break
            if row_index == table_size - 1:
                return True

    return False


def is_winner_rows(state, player):
    for row in state:
        for col_index, cell in enumerate(row):
            if cell != player:
                break
            if col_index == len(state) - 1:
                return True

    return False


def is_winner_diag(state, player):
    for i in range(len(state)):
        if state[i][i] != player:
            return False

    return True


def is_winner_rdia(state, player):
    for i in range(len(state)):
        if state[i][len(state) - 1 - i] != player:
            return False

    return True


def is_winner(state, player):
    if is_winner_rows(state, player):
        return True
    if is_winner_cols(state, player):
        return True
    if is_winner_diag(state, player):
        return True
    if is_winner_rdia(state, player):
        return True
    return False


def user_input(state):
    while True:
        try:
            move = input("Your turn: ")
            if len(move) != 3:
                print(
                    'The format of for input is "x,y" where x is the horizontal axis and y is the vertical axis. Upper left spot is 0, 0.'
                )
            else:
                x, y = map(int, move.strip().split(","))
                if is_move_valid(state, x, y):
                    return x, y
                else:
                    print("Your move is not valid")
        except ValueError:
            print("Invalid input")
        except EOFError:
            exit("Game aborted")


def computer_input(state):
    while True:
        x = random.randrange(0, len(state), 1)
        y = random.randrange(0, len(state), 1)

        if is_move_valid(state, x, y):
            return x, y


if __name__ == "__main__":
    main()
