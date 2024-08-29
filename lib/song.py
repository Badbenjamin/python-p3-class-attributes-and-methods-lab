class Song:
    
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_artist_to_list(self.artist)
        self.add_genre_to_list(self.genre)
        self.update_genre_count(genre)
        self.update_artist_count(artist)


    @classmethod
    def add_song_to_count(cls, incriment = 1):
        cls.count += incriment

    @classmethod
    def add_artist_to_list(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_genre_to_list(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def update_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1  

    @classmethod
    def update_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
        

thong_song = Song("thong song", "cisco", "rap")
wrong_song = Song("bong", "dong", "harsh noise")
song_song = Song("da_song", "da_artist", "harsh noise")
pizza_pie = Song("thats amore", "italian man", "italian")
spaghetti = Song("spaghetti song", "italian man", "italian")
party_and_bullshit = Song("p&b", "biggie", "rap")
real_big = Song("real big", "big tymers", "rap")

print(Song.genre_count)

    # @classmethod
    # def genre_count(cls):
       
    #     sorted_genres = sorted(cls.genres)
    #     genre_and_count = []
    #     for current_genre in sorted_genres:
    #         genre_count = 0
    #         the_genre = []
    #         for genre in cls.genres:
    #             if current_genre == genre:
    #                 genre_count += 1
    #                 if genre not in the_genre:
    #                     the_genre.append(current_genre)
    #         # print(the_genre)
    #         genre_and_count.append({the_genre[0] : genre_count})

    #     # print(genre_and_count)
    #     g_c_reduced = []
    #     for g_c_pair in genre_and_count:
    #         if g_c_pair not in g_c_reduced or g_c_reduced == []:
    #             g_c_reduced.append(g_c_pair)
    #     print(g_c_reduced)
    #     return g_c_reduced
    #     # print(genre_list)

    


# # print(thong_song.artist)

# Song.genre_count()