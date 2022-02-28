# JJ Small
# manga_model.py
# This class is a representation of what a manga series has/does

class Manga:
    def __init__(self, title: str, volume_count: int) -> None:
        self.local_title = title
        self.site_title = None
        self.site_id = None
        self.my_volumes = volume_count
        self.is_licensed: bool = False
        self.eng_volumes = None
        self.eng_status = None
        self.source_volumes = None
        self.source_status = None
        self.has_match: bool = False
        self.year: int = -1
        self.cover = None

    def print_has_match(self):
        temp = vars(self)
        for attribute in temp:
            print(f"\t{attribute} -> {temp[attribute]}")
        print()

    def print_no_match(self) -> None:
        print(f"\t{self.local_title}")