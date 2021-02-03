from Song import Song

class Playlist:
    def __init__(self):
        self.__first_song = None



    # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

    def add_song(self, title):
        newSong = Song(title)
        newSong.set_next_song(self.__first_song)

        self.__first_song = newSong


    def find_song(self, title):
        i = 0

        current = self.__first_song
        while current != str(title).title():
            if current.get_next_song() == None:
                return False
            
            current = current.get_next_song()
            i += 1
        return i


    def remove_song(self, title):
        
        current_song = self.__first_song

        if current_song.get_title() == str(title).title():
            self.__first_song = current_song.get_next_song()
            return True

        while current_song.get_next_song().get_title() != str(title).title():
            if current_song.get_next_song() == None:
                return False

        current_song = current_song.get_next_song()
        
        target = current_song.get_next_song()
        current_song.set_next_song(target.get_next_song())

        print("Song has been removed!")




    def length(self):
        count = 0
        current_song = self.__first_song
        while current_song != None:
            count += 1
            current_song = current_song.get_next_song()
        return count


    def print_songs(self):

        count = 0
        current_song = self.__first_song

        while current_song != None:
            count += 1
            print(f"{count}. {current_song.get_title()}")
            current_song = current_song.get_next_song()

        if count == 0:
            return False