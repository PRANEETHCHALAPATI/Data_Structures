def find_winner(piles):
    turns = ["Asta" ,"Yuno"]
    turn = 0
    game_over = False
    while not game_over:
        new_piles = list(filter(lambda x:x>=1,piles))
        if len(new_piles) == len(piles):
            for i in range(len(piles)):
                piles[i] -= 1 
            if turn == 0:
                turn = 1 
            else:
                turn = 0
        else:
            for i in range(len(piles)):
                if piles[i] >= 1:
                    piles[i] -= 1 
                    if turn == 0:
                        turn = 1 
                    else:
                        turn = 0 
                    break
        new_piles = list(filter(lambda x:x>=1,piles)) 
        if len(new_piles) == 0:
            if turn == 0:
                print(turns[1])
            else:
                print(turns[0]) 
            return 
def main():
    piles = list(map(int,input().split()))
    find_winner(piles) 
main()