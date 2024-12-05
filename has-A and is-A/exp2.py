class SportsNews:
    def sportsInfo(self):
        print("Sports News:")
class MoviesNews:
    def MoviesInfo(self):
        print("Movies News:")
class PoliticsNews:
    def PoliticsInfo(self):
        print("Politics News:")
class DurgaNews:
    def __init__(self):
        self.sports = SportsNews()
        self.movies = MoviesNews()
        self.politics = PoliticsNews()
    def getTotalNews(self):
        self.sports.sportsInfo()
        self.movies.MoviesInfo()
        self.politics.PoliticsInfo()
durga = DurgaNews()

class DurgaNews:
    def __init__(self,sports,movies,politics):
        self.sports = sports
        self.movies = movies
        self.politics = politics
    def getTotalNews(self):
        self.sports.sportsInfo()
        self.movies.MoviesInfo()
        self.politics.PoliticsInfo()
sports=SportsNews()
movies=MoviesNews
politics=PoliticsNews()
durga = DurgaNews(sports,movies,politics)