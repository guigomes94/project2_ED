class Music:

    def __init__(self, name, author, album, year):

        self.name = name
        self.author = author
        self.album = album
        self.year = year

    def __str__(self):
        return f'Name: {self.name}\nAuthor: {self.author}\nAlbum: {self.album}\nYear: {self.year}'
