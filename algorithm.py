T = int(input())

Puzzle = []
N = []
K = [] 
for test_cnt in range(T):
    N.append(0)
    K.append(0)
    N[test_cnt], K[test_cnt] = map(int, input().split())
    Puzzle.append([])
    for matrix_length in range(N[test_cnt]):
        Puzzle[test_cnt].append(list(map(int, input().split())))
    
for test_cnt in range(T):
    cnt = 0
    test_list = [0, 0]
    for k in range(K[test_cnt]):
        test_list.insert(1, 1)
    for mat_row in range(N[test_cnt]):
        for slice_num in range(N[test_cnt]-K[test_cnt]+1):
            if slice_num == N[test_cnt]-K[test_cnt]:
                if Puzzle[test_cnt][mat_row][slice_num-1:slice_num+K[test_cnt]] == test_list[:-1]:
                    cnt += 1
            elif slice_num == 0:
                if Puzzle[test_cnt][mat_row][slice_num:slice_num+K[test_cnt]+1] == test_list[1:]:
                    cnt += 1
            else:
                if Puzzle[test_cnt][mat_row][slice_num-1:slice_num+K[test_cnt]+1] == test_list:
                    cnt += 1
    Puzzle_flip = list(map(list, zip(*Puzzle[test_cnt])))
    for mat_row in range(N[test_cnt]):
        for slice_num in range(N[test_cnt]-K[test_cnt]+1):
            if slice_num == N[test_cnt]-K[test_cnt]:
                if sum(Puzzle[test_cnt][mat_row][slice_num-1:slice_num+K[test_cnt]]) == test_list[:-1]:
                    cnt += 1
            elif slice_num == 0:
                if sum(Puzzle[test_cnt][mat_row][slice_num:slice_num+K[test_cnt]+1]) == test_list[1:]:
                    cnt += 1
            else:
                if sum(Puzzle[test_cnt][mat_row][slice_num-1:slice_num+K[test_cnt]+1]) == test_list:
                    cnt += 1
    
    print(f'#{test_cnt+1} {cnt}')