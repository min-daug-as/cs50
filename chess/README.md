# Chess Piece Capture Checker

This Python script determines which black pieces can be captured by a specified white piece on a chessboard. The script currently supports the queen and knight as white pieces.

## Usage
To use this script, follow these steps:

1. Run the Script:

```
> python chess_question.py
```

2. Input the white piece:

The script will prompt you to input the white piece (queen or knight) and its position. For example:

```
> Input white piece name (queen, knight) and its position i.e. knight a5: queen d4
```

3. Input the black pieces:
The script will then prompt you to input the positions of the black pieces one by one. For example:

```
> Input black piece position: e5
> Input black piece position: f6
> Input black piece position: g7
> Input black piece position: h8
> Input black piece position: done

```

When you have finished entering all black pieces, type ```done``` to proceed.

4. View the Result:
The script will output which black pieces the white piece can capture. For example:

```
> White piece: queen d4
> Black pieces: e5, f6, g7, h8
> Pieces white can take: e5
```

