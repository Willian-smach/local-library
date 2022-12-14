from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):

	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()

	num_instances_available = BookInstance.objects.filter(status__exact='a').count()

	num_authors = Author.objects.count()

	context = {
	    'num_books': num_books,
	    'num_instances': num_instances,
	    'num_instances_available': num_instances_available,
	    'num_authors': num_authors,
	}

	return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
	model = Book
	template_name = 'catalog/bookList.html'
	paginate_by = 5

class BookDetailView(generic.DetailView):
	model = Book
	template_name = 'catalog/bookDetail.html'
