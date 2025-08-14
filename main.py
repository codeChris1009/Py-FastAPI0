from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

from typing import List,  Optional
from uuid import UUID, uuid4
from datetime import date

app = FastAPI()


class Reflection(BaseModel):
    rate_star: Optional[int] = 1
    desc: Optional[str] = None

class Book(BaseModel):
    id: Optional[UUID] = None
    isbn: str
    author: Optional[str] = None
    title: Optional[str] = None
    lang: str
    isRead: bool = False
    reflection: Optional[Reflection] = None


bookshelf = []

# Welcome Message
@app.get("/")
def welcome_message():
    today = date.today()
    week = today.strftime("%A")
    return {"welcomeMessage": f"{week}, Happy Book, Code, Cookie With Padi~"}

# ================================================================================================================

# Create Post

# Create a new book
@app.post("/bookshelf", response_model=Book)
def create_book(book: Book):
    book.id = uuid4()
    bookshelf.append(book)
    return book

# Create a lots of books
@app.post("/bookshelf/bulk", response_model=List[Book])
def create_books(books: List[Book]):
    for book in books:
        book.id = uuid4()
        bookshelf.append(book)
    return books

# ================================================================================================================

# Read Books

# Get all bookshelf
@app.get("/bookshelf", response_model=List[Book])
def read_books():
    return bookshelf

# Get by ISBN
@app.get("/bookshelf/{isbn}", response_model=Book)
def read_bookByISBN(isbn: str):
    for book in bookshelf:
        if book.isbn == isbn:
            return book
    raise HTTPException(status_code=404, detail=f"Book not found, please check the ISBN：{isbn}")



# Get by Title
@app.get("/bookshelf/title/{title}", response_model=List[Book])
def read_booksByTitle(title: str):
    matched_books = [book for book in bookshelf if book.title == title]
    if matched_books:
        return matched_books
    raise HTTPException(status_code=404, detail=f"Book not found, please check the Title：{title}")

# Get by Author
@app.get("/bookshelf/author/{author}", response_model=List[Book])
def read_booksByAuthor(author: str):
    matched_books = [book for book in bookshelf if book.author == author]
    if matched_books:
        return matched_books
    raise HTTPException(status_code=404, detail=f"Book not found, please check the Author：{author}")

# ================================================================================================================

# Update Book

# Update a book With Demo Vid
@app.put("/bookshelf/{book_id}", response_model=Book)
def update_book_put(book_id: UUID, updated_book: Book):
    for index, book in enumerate(bookshelf):
        if book.id == book_id:
            bookshelf[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail=f"Book not found, please check the ID：{book_id}")

# Update a book By ISBN Use PUT
# PUT Will Completely Replace the Book CREATE OR UPDATE, ISBN would be unique Prime Key for Book
@app.put("/bookshelf/{isbn}", response_model=Book)
def update_book_put_ISBN(isbn: str, updated_book: Book):
    matched_indices = [i for i, book in enumerate(bookshelf) if book.isbn == isbn]
    if len(matched_indices) > 1:
        raise HTTPException(status_code=400, detail=f"Multiple books found with the same ISBN: {isbn}. Update aborted.")
    if len(matched_indices) == 1:
        index = matched_indices[0]
        updated_book.id = bookshelf[index].id
        bookshelf[index] = updated_book
        return updated_book
    raise HTTPException(status_code=404, detail=f"Book not found, please check the ISBN：{isbn}")

# Update a book By Title Use PATCH
@app.patch("/bookshelf/title/{title}", response_model=Book)
def update_book_patch_title(title: str, updated_book: Book):
    for index, book in enumerate(bookshelf):
        if book.title == title:
            bookshelf[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail=f"Book not found, please check the Title：{title}")

# ================================================================================================================

# Delete Book

@app.delete("/bookshelf/{book_id}", response_model=Book)
def delete_book(book_id: UUID):
    for index, book in enumerate(bookshelf):
        if book.id == book_id:
            return bookshelf.pop(index)
    raise HTTPException(status_code=404, detail=f"Book not found, please check the ID：{book_id}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)