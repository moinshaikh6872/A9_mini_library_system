import json
import csv
import os

class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        # Private copy count
        self.__copies = copies

    def get_copies(self):
        return self.__copies

    def add_copy(self):
        self.__copies += 1

    def remove_copy(self):
        if self.__copies > 0:
            self.__copies -= 1
            return True
        return False

    def to_dict(self):
        return {"title": self.title, "author": self.author, "copies": self.__copies}

class Library:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title, author):
        # Adds books without duplicating a title by increasing copies instead
        if title in self.inventory:
            self.inventory[title].add_copy()
        else:
            self.inventory[title] = Book(title, author)

    def borrow_book(self, title):
        if title in self.inventory and self.inventory[title].remove_copy():
            return True
        return False

    def return_book(self, title):
        if title in self.inventory:
            self.inventory[title].add_copy()
            return True
        return False

    def save_to_json(self, filename="library_data.json"):
        data = {title: book.to_dict() for title, book in self.inventory.items()}
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename="library_data.json"):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                for title, info in data.items():
                    self.inventory[title] = Book(info["title"], info["author"], info["copies"])

    def export_csv(self, filename="library_export.csv"):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Copies"])
            writer.writeheader()
            for book in self.inventory.values():
                writer.writerow({
                    "Title": book.title, 
                    "Author": book.author, 
                    "Copies": book.get_copies()
                })

    def read_from_text(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) >= 2:
                        self.add_book(parts[0].strip(), parts[1].strip())
