#!/usr/bin/python3
from sys import argv

def solve_queen_problem():
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    size = int(argv[1])
    chess_board = [["$" for j in range(size)] for k in range(size)]
    print ( chess_board )
    print("{:d}".format(int(argv[1])))

if __name__ == "__main__":
    solve_queen_problem()
