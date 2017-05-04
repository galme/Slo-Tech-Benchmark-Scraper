class Order():
    ASCENDING = 0  # lower is better
    DESCENDING = 1  # higher is better

class Format():
    ANONYMOUS = 0b0001
    NAMED = 0b0010
    LEADERBOARD = 0b0100
    LIST = 0b1000

delim = '|'
keyScorePosition = -1  # indeks v rezultatu, po katerem sortiramo
expectedNicknamePosition = 10000  # indeks nickname-a v rezultatu
Labels = []
FileName = "LEADERBOARDS.txt"
OutputFormat = Format.LEADERBOARD | Format.NAMED
OutputOrder = Order.DESCENDING

