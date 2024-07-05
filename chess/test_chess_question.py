import chess_question


def main():
    chess_question.print_result("knight", "a5", ["b1", "b2"], ["b1"])


def test_queen_has_nothing_to_take():
    assert (
        chess_question.get_pieces_white_can_take(
            "queen", "d5", ["c3", "g3", "a7", "f6"]
        )
        == []
    )


def test_queen_takes_pieces_in_diagonals():
    assert chess_question.get_pieces_white_can_take(
        "queen", "d5", ["f7", "g8", "a2", "b3"]
    ) == ["f7", "b3"]


def test_queen_takes_pieces_in_files():
    assert chess_question.get_pieces_white_can_take(
        "queen", "d5", ["d1", "d2", "d3", "d4", "d6", "d7", "d8"]
    ) == ["d6", "d4"]


def test_queen_takes_pieces_in_ranks():
    assert chess_question.get_pieces_white_can_take(
        "queen", "d5", ["a5", "b5", "c5", "e5", "f5", "g5", "h5"]
    ) == ["e5", "c5"]


def test_queen_paths_when_queen_is_in_a_middle_of_a_board_d5():
    assert chess_question.get_queen_paths("d5") == [
        ["d6", "d7", "d8"],
        ["e6", "f7", "g8"],
        ["e5", "f5", "g5", "h5"],
        ["e4", "f3", "g2", "h1"],
        ["d4", "d3", "d2", "d1"],
        ["c4", "b3", "a2"],
        ["c5", "b5", "a5"],
        ["c6", "b7", "a8"],
    ]


def test_queen_path_when_queen_is_in_first_rank_f1():
    assert chess_question.get_queen_paths("f1") == [
        ["f2", "f3", "f4", "f5", "f6", "f7", "f8"],
        ["g2", "h3"],
        ["g1", "h1"],
        [],
        [],
        [],
        ["e1", "d1", "c1", "b1", "a1"],
        ["e2", "d3", "c4", "b5", "a6"],
    ]


def test_queen_paths_when_queen_is_in_first_file_a5():
    assert chess_question.get_queen_paths("a5") == [
        ["a6", "a7", "a8"],
        ["b6", "c7", "d8"],
        ["b5", "c5", "d5", "e5", "f5", "g5", "h5"],
        ["b4", "c3", "d2", "e1"],
        ["a4", "a3", "a2", "a1"],
        [],
        [],
        [],
    ]


def test_queen_paths_when_queen_is_in_corner_h8():
    assert chess_question.get_queen_paths("h8") == [
        [],
        [],
        [],
        [],
        ["h7", "h6", "h5", "h4", "h3", "h2", "h1"],
        ["g7", "f6", "e5", "d4", "c3", "b2", "a1"],
        ["g8", "f8", "e8", "d8", "c8", "b8", "a8"],
        [],
    ]


def test_knight_paths_when_knight_is_in_middle_d5():
    assert chess_question.get_knight_paths("d5") == [
        ["f6"],
        ["f4"],
        ["b6"],
        ["b4"],
        ["e3"],
        ["c3"],
        ["e7"],
        ["c7"],
    ]


def test_knight_paths_when_knight_is_corner_h8():
    assert chess_question.get_knight_paths("h8") == [
        [],
        [],
        [],
        ["f7"],
        [],
        ["g6"],
        [],
        [],
    ]


def test_knight_paths_when_knight_is_first_file_a5():
    assert chess_question.get_knight_paths("a5") == [
        ["c6"],
        ["c4"],
        [],
        [],
        ["b3"],
        [],
        ["b7"],
        [],
    ]


def test_knight_path_when_knight_is_in_first_rank_f1():
    assert chess_question.get_knight_paths("f1") == [
        ["h2"],
        [],
        ["d2"],
        [],
        [],
        [],
        ["g3"],
        ["e3"],
    ]


if __name__ == "__main__":
    main()
