import sys,threading
def main():
    si,sj,ei,ej = map(int,input().split())
    si -= 1
    sj -= 1
    ei -= 1
    ej -= 1
    rook = 0
    bishop = 0
    king = 0
    turn = True
    t = True
    grid = []
    for i in range(8):
        mat = []
        for j in range(8):
            if turn:
                mat.append("B")
                turn = False
            else:
                mat.append("W")
                turn = True
        if t:
            grid.append(mat)
            t = False
        else:
            mat.reverse()
            grid.append(mat)
            t = True

    if si == ei or sj == ej:
        rook = 1
    else:
        rook = 2
    if grid[si][sj] == grid[ei][ej]:
        if abs(si-ei) == abs(sj-ej):
            bishop = 1
        else:
            bishop = 2
    else:
        bishop = 0
    king = max(abs(si-ei),abs(sj-ej))
    ans = [rook,bishop,king]
    print(*ans)
sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()
    