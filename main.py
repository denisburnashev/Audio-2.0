class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = int(duration)

    def show(self):
        print(f'{self.name} - {self.duration} min.')

    def __str__(self):
        return f'{self.name} - {self.duration} min.'

    def __lt__(self, other):
        return self.duration < other.duration




class Album:
    def __init__(self, album_name, group, track_list):
        self.album_name = album_name
        self.group = group
        self.track_list = track_list

    def get_tracks(self, album):
        for tracks in album:
            tracks.show()

    def get_add(self, album, track):
        album.append(track)

    def get_duration(self, albom, total_duration=0):
        for tracks in albom:
            total_duration += tracks.duration
        print(f'Общая длительность альбома: {total_duration} min.')

    def __str__(self):
        return f"Name group: {self.album_name} \n" \
               f"Name album: {self.group} \n" \
               f"Tracks: {''.join(str(self.track_list))}"





numb = Track('Numb', 3)
in_the_end = Track('In The End', 3)
faint = Track('Faint', 2)

believer = Track('Believer', 3)
deep = Track('Deep Water', 3)
best_day = Track('Best Day of my Life', 3)

print(numb)
print(in_the_end)
print(faint)
print(believer)
print(deep)
print(best_day)

linkin = []
american = []

album1 = Album('linkin', 'Linkin Park', linkin)
album2 = Album('american', 'American author', american)

album1.get_add(linkin, numb)
album1.get_add(linkin, in_the_end)
album1.get_add(linkin, faint)
album2.get_add(american, believer)
album2.get_add(american, deep)
album2.get_add(american, best_day)

print(album1)
print(album2)
print(numb > faint)