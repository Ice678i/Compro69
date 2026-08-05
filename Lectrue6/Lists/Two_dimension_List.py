import random
ROWS = 3
COLS = 4
def main():
    value = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    for r in range(ROWS):
        for c in range(COLS):
            value[r][c] = random.randint(1, 100)
    print(value)

main()
