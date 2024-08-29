class Song:
    
    count = 0

    artists = []

    genres = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_artist_to_list(self.artist)
        self.add_genre_to_list(self.genre)

    @classmethod
    def add_song_to_count(cls, incriment = 1):
        cls.count += incriment

    @classmethod
    def add_artist_to_list(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_genre_to_list(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def get_genre_count(cls):
        genre_and_count = []
        for current_genre in cls.genres:
            genre_count = 0
            the_genre = []
            for genre in cls.genres:
                if current_genre == genre:
                    genre_count += 1
                    the_genre.append(current_genre)
        genre_and_count.append(f"{the_genre[0]} : {genre_count}")
                    
        print(genre_and_count)
        # print(genre_list)

    
thong_song = Song("thong song", "cisco", "rap")
wrong_song = Song("bong", "dong", "harsh noise")
song_song = Song("da_song", "da_artist", "harsh noise")

# print(thong_song.artist)

Song.get_genre_count()