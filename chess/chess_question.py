FILES = "abcdefgh"


def main():

    white_piece, white_pos = input_white_piece()
    black_pieces = input_black_pieces(white_pos)
    white_can_take = get_pieces_white_can_take(white_piece, white_pos, black_pieces)
    print_result(white_piece, white_pos, black_pieces, white_can_take)


def get_pieces_white_can_take(piece, pos, black_pieces):
    """Determine which black pieces the white piece can capture."""
    white_piece_paths = get_piece_paths(piece, pos)
    pieces_white_can_take = []

    for path in white_piece_paths:
        
        break_loop = False
        for square in path:
            if break_loop:
                break

            for piece in black_pieces:
                if square == piece:
                    pieces_white_can_take.append(piece)
                    break_loop = True
                    break

    return pieces_white_can_take


def get_piece_paths(piece, pos):
    """Get all possible paths for a given piece from its position."""
    match piece:
        case "queen":
            return get_queen_paths(pos)
        case "knight":
            return get_knight_paths(pos)
        case _:
            return []


def get_knight_paths(pos):
    """Get all possible moves for a knight from its position."""
    paths = []
    paths.append(path(move_piece(pos, 2, 1)))
    paths.append(path(move_piece(pos, 2, -1)))
    paths.append(path(move_piece(pos, -2, 1)))
    paths.append(path(move_piece(pos, -2, -1)))
    paths.append(path(move_piece(pos, 1, -2)))
    paths.append(path(move_piece(pos, -1, -2)))
    paths.append(path(move_piece(pos, 1, 2)))
    paths.append(path(move_piece(pos, -1, 2)))
    return paths


def path(pos):
    """Return a path list with the position if valid, else an empty list."""
    if pos is None:
        return []

    return [pos]


def move_piece(pos, file_increment, rank_increment):
    """Move a piece from its position by the specified increments."""
    rank = int(pos[1]) + rank_increment
    file_index = FILES.index(pos[0]) + file_increment

    if file_index < 0 or file_index > 7 or rank > 8 or rank < 1:
        return None

    return f"{FILES[file_index]}{rank}"


def get_queen_paths(pos):
    """Get all possible moves for a queen from its position."""
    paths = []
    paths.append(queen_move_up(pos))
    paths.append(queen_move_up_right(pos))
    paths.append(queen_move_right(pos))
    paths.append(queen_move_down_right(pos))
    paths.append(queen_move_down(pos))
    paths.append(queen_move_down_left(pos))
    paths.append(queen_move_left(pos))
    paths.append(queen_move_top_left(pos))
    return paths


def queen_move_up(pos):
    return [f"{pos[0]}{r}" for r in range(int(pos[1]) + 1, 9)]


def queen_move_up_right(pos):
    files = FILES[FILES.index(pos[0]) + 1 :]
    ranks = list(range(int(pos[1]) + 1, 9))
    return [f"{f}{r}" for f, r in zip(files, ranks)]


def queen_move_right(pos):
    return [f"{f}{pos[1]}" for f in FILES[FILES.index(pos[0]) + 1 :]]


def queen_move_down_right(pos):
    files = FILES[FILES.index(pos[0]) + 1 :]
    ranks = sorted(range(1, int(pos[1])), reverse=True)
    return [f"{f}{r}" for f, r in zip(files, ranks)]


def queen_move_down(pos):
    return [f"{pos[0]}{n}" for n in sorted(range(1, int(pos[1])), reverse=True)]


def queen_move_down_left(pos):
    files = sorted(FILES[: FILES.index(pos[0])], reverse=True)
    ranks = sorted(range(1, int(pos[1])), reverse=True)
    return [f"{f}{r}" for f, r in zip(files, ranks)]


def queen_move_left(pos):
    return [f"{n}{pos[1]}" for n in sorted(FILES[: FILES.index(pos[0])], reverse=True)]


def queen_move_top_left(pos):
    files = sorted(FILES[: FILES.index(pos[0])], reverse=True)
    ranks = range(int(pos[1]) + 1, 9)
    return [f"{f}{r}" for f, r in zip(files, ranks)]


def print_result(white_piece_name, white_piece_pos, black_pieces, pieces_white_can_take):
    """Print the result of the moves."""
    print()
    print(f"White piece: {white_piece_name} {white_piece_pos}")
    print(f"Black pieces: {', '.join(black_pieces)}")
    print(f"Pieces white can take: {', '.join(pieces_white_can_take)}")


def input_white_piece():
    """Input and validate the white piece and its position."""
    while True:
        try:
            piece_str = input(
                "Input white piece name (queen or knight) and its position i.e. knigth a5: "
            )
            piece, pos = piece_str.strip().lower().split(" ")

            if piece not in ["queen", "knight"]:
                print("Only queen or knight can be proveded")
                continue

            if not are_coordinates_valid(pos):
                print(
                    "Position should be a coordinates of the peace in xy format, where is x represents a columns labeled a trough g, and y represents rows numbered 1 to 8 i.e. a5"
                )
                continue

            return piece, pos
        except ValueError:
            print("Invlaid input")
        except EOFError:
            exit("Program aborted")


def input_black_pieces(white_piece_pos):
    """Input and validate positions of black pieces."""
    pieces = []
    while True:
        try:
            if len(pieces) >= 16:
                print("You've entered maximum number of 16 black pieces")
                break

            pos = input("Input black piece position: ")
            pos = pos.strip().lower()

            if pos == "done":
                if len(pieces) == 0:
                    print("At least one black piece is required")
                    continue
                else:
                    break

            if not are_coordinates_valid(pos):
                print("Invalid position format")
            
            if pos in pieces:
                print("This square is already occupied by black piece")
            elif pos == white_piece_pos:
                print("This square is already occupied by white piece")
            else:
                pieces.append(pos)
            
        except ValueError:
            print("Invalid input")
        except EOFError:
            exit("Program aborted")

    return pieces


def are_coordinates_valid(c):
    """Validate the coordinates."""
    try:
        return len(c) == 2 and c[0] in FILES and 1 <= int(c[1]) <= 8
    except ValueError:
        return False


if __name__ == "__main__":
    main()
