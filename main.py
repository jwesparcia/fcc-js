def game_score(player1, player2):
    score1 = 0
    score2 = 0

    for p1, p2 in zip(player1, player2):
        if p1 == "C" and p2 == "C":
            score1 += 3
            score2 += 3
        elif p1 == "D" and p2 == "D":
            score1 += 1
            score2 += 1
        elif p1 == "D" and p2 == "C":
            score1 += 5
        else:  # p1 == "C" and p2 == "D"
            score2 += 5

    return [score1, score2]