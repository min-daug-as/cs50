import tic_tac_toe


def test_if_column_is_marked():
    assert not tic_tac_toe.is_winner([["", "", ""], ["", "", ""], ["", "", ""]], "X")
    assert tic_tac_toe.is_winner([["X", "", ""], ["X", "", ""], ["X", "", ""]], "X")
    assert tic_tac_toe.is_winner([["", "Y", ""], ["", "Y", ""], ["", "Y", ""]], "Y")


def test_if_row_is_marked():
    assert tic_tac_toe.is_winner([["X", "X", "X"], ["", "", ""], ["", "", ""]], "X")
    assert tic_tac_toe.is_winner([["", "X", "X"], ["Y", "Y", "Y"], ["X", "Y", "X"]], "Y")


def test_if_diagonals_are_marked():
    assert tic_tac_toe.is_winner([["X", "", ""], ["", "X", ""], ["", "", "X"]], "X")
    assert tic_tac_toe.is_winner([["", "", "X"], ["", "X", ""], ["X", "", ""]], "X")
