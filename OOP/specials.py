class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie")
    def __str__(self):
        return f"{self.title}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print("movie silindi")


m=Movie("film","yönetmen","süre")
print(str(m))
del m