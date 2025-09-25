from django.shortcuts import render, redirect, get_object_or_404
from book.models import Book
from book.forms import BookForm, ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book-create')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})


def book_list(request):
    genre = request.GET.get('genre', '')   # default = ''
    query = request.GET.get('q', '')       # default = ''

    books = Book.objects.all().order_by('-created_at')

    if genre:
        books = books.filter(genre=genre)
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book/book_list.html', {
        'page_obj': page_obj,
        'genre': genre,
        'query': query
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    review_form = ReviewForm()

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.book = book
            review.save()
            book.update_average_rating()
            messages.success(request, "Review added successfully!")
            return redirect('book-detail', pk=book.pk)

    return render(request, 'book/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'review_form': review_form
    })


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form, 'book': book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book-list')
    return render(request, 'book/book_confirm_delete.html', {'book': book})
