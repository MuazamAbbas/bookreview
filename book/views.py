from django.shortcuts import render, redirect
from book.models import Book
from book.forms import BookForm
from django.contrib import messages

# Create your views here.
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            # Redirect to a new URL:
            return redirect('book-create')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})

def book_list(request):
    # Example of filtering by genre if needed
    genre = request.GET.get('genre')
    if genre:
        books = Book.objects.filter(genre=genre).order_by('-created_at')
    else:
        # Get all books from the database
        books = Book.objects.all().order_by('-created_at')
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            # Redirect to a new URL:
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form, 'book': book})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        # Redirect to a new URL:
        return redirect('book-list')
    return render(request, 'book/book_confirm_delete.html', {'book': book})