from library_system import Book, Library

def run_checks():
    print("Running basic assertions...")
    
    # Check Book functionality
    b = Book("Test Title", "Test Author", 1)
    assert b.title == "Test Title"
    assert b.get_copies() == 1
    
    # Check Library functionality
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    lib.add_book("Dune", "Frank Herbert") # Duplicate addition
    assert lib.inventory["Dune"].get_copies() == 2
    
    # Check Borrowing and Returning
    assert lib.borrow_book("Dune") == True
    assert lib.inventory["Dune"].get_copies() == 1
    assert lib.return_book("Dune") == True
    
    print("All basic assertions passed successfully.")

if __name__ == "__main__":
    run_checks()
