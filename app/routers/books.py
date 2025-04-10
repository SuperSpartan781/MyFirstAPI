from fastapi import APIRouter
from models.book import Book
from data.books import books

router = APIRouter(prefix = "/books")

@router.get("/")
def get_all_books() -> list[Book]:
    return list(books.values())