from fastapi import FastAPI
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


# Create Post
@app.post("/bookshelf", response_model=Book)
def create_book(book: Book):
    book.id = uuid4()
    bookshelf.append(book)
    return book

# Read Books
@app.get("/bookshelf", response_model=List[Book])
def read_books():
    return bookshelf

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)