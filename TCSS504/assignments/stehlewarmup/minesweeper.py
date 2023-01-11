"""
Sample Input

4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0

Sample Output

Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100
"""
input_file = open('test_input.txt', 'r')
# input_file = open('mines.txt', 'r')
lines_to_read = input_file.readline().split()
rows = int(lines_to_read[0])
field = 1


while rows != 0:
    board_array = []
    print(f"Field #{field}:")

    for i in range(rows): # fill out the 2d Array
        line = list(input_file.readline().strip('\n'))
        # print('line: ', line)
        board_array.append(line)
        # print(board_array)

    for i in range(len(board_array)): # for each row (i) in board array...
        for j in range(len(board_array[i])): # for each item (j) in each board array row (i)...
            mine_tracker = 0

            if board_array[i][j] == '*':
                print('*', end='')
            else:
                try:
                    if board_array[i-1][j] == '*': #North
                        # print(f'mine North at {i-1},{j}')
                        mine_tracker += 1
                except IndexError:
                    pass

                try:
                    if board_array[i+1][j] == '*': #South
                        # print(f'mine South at {i+1},{j}')
                        mine_tracker += 1
                except IndexError:
                    pass

                try:
                    if board_array[i][j-1] == '*': #West
                        # print(f'mine West at {i},{j-1}')
                        mine_tracker += 1
                except IndexError:
                    pass

                try:
                    if board_array[i][j+1] == '*': #East
                        # print(f'mine East at {i},{j+1}')
                        mine_tracker += 1
                except IndexError:
                    pass

                try:
                    if board_array[i-1][j+1] == '*': #NE
                        # print(f'mine NE at {i-1},{j+1}')
                        mine_tracker += 1
                except IndexError:
                    pass

                try:
                    if board_array[i-1][j-1] == '*': #NW
                        # print(f'mine NW at {i-1},{j-1}')
                        mine_tracker += 1
                except IndexError:
                    pass

                try:
                    if board_array[i+1][j+1] == '*': #SE
                        # print(f'mine SE at {i+1},{j+1}')
                        mine_tracker += 1
                except IndexError:
                    pass

                try:
                    if board_array[i+1][j-1] == '*':
                        # print(f'mine SW at {i+1},{j-1}')
                        mine_tracker += 1
                except IndexError:
                    pass

                print(mine_tracker, end='')

            if j == len(board_array[i]) - 1:
                print()


    # ====== Reset for the next group ======
    lines_to_read = input_file.readline().split()
    rows = int(lines_to_read[0])
    field += 1
    print()

input_file.close()

