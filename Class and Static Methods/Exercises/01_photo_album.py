class PhotoAlbum:
    MAX_PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):  # pages = math.ceil(photos_count / 4)
        if photos_count % cls.MAX_PHOTOS_ON_PAGE == 0:
            pages = photos_count // cls.MAX_PHOTOS_ON_PAGE
        else:
            pages = photos_count // cls.MAX_PHOTOS_ON_PAGE + 1

        return cls(pages)

    def add_photo(self, label: str) -> str:
        for page in range(self.pages):
            for photo in range(PhotoAlbum.MAX_PHOTOS_ON_PAGE):
                if len(self.photos[page]) < PhotoAlbum.MAX_PHOTOS_ON_PAGE:
                    self.photos[page].append(label)
                    return f"{label} photo added successfully on page {page + 1} slot {photo + 1}"

        return "No more free slots"

    def display(self):
        photos = [["[]" for ph in page if ph] for page in self.photos]
        result = "-----------\n"
        for page in photos:
            result += f"{' '.join(page)}\n-----------\n"
        return result[:-1]


# line 11: forgot not to add 1 page, when result from dividing is a whole number

album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())




