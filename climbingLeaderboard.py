
def climbingLeaderboard_optimized(ranked, player):
    # Remove duplicates and sort descending
    ranked_unique = sorted(set(ranked), reverse=True)
    n = len(ranked_unique)
    result = []
    i = n - 1  # Start from the end of ranked_unique

    for score in player:
        # Move up the leaderboard as long as the player's score is >= ranked score
        while i >= 0 and score >= ranked_unique[i]:
            i -= 1
        result.append(i + 2)  # +2 because rank is index+1, and we stopped at the first less-than
    return result

print(3500*12)