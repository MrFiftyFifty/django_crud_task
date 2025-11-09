import json
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Book, Author
from .forms import BookForm


# Book Views (HTML-based CRUD)
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('book_list')


class BookEditView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(instance=book)
        return render(request, 'library/book_edit.html', {'form': form, 'book': book})


class BookDetailUpdateDeleteView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'library/book_detail.html', {'book': book})
    
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'library/book_edit.html', {'form': form, 'book': book})
    
    def delete(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect('book_list')


# Author API Views (JSON REST API)
@method_decorator(csrf_exempt, name='dispatch')
class AuthorListCreateView(View):
    def get(self, request):
        authors = Author.objects.all()
        data = [{
            'id': author.id,
            'first_name': author.first_name,
            'last_name': author.last_name,
            'bio': author.bio,
            'birth_date': author.birth_date.isoformat() if author.birth_date else None
        } for author in authors]
        return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            author = Author.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                bio=data.get('bio', ''),
                birth_date=data.get('birth_date')
            )
            return JsonResponse({
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'bio': author.bio,
                'birth_date': author.birth_date.isoformat() if author.birth_date else None
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class AuthorDetailView(View):
    def get(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        data = {
            'id': author.id,
            'first_name': author.first_name,
            'last_name': author.last_name,
            'bio': author.bio,
            'birth_date': author.birth_date.isoformat() if author.birth_date else None
        }
        return JsonResponse(data)

    def put(self, request, author_id):
        try:
            author = get_object_or_404(Author, id=author_id)
            data = json.loads(request.body)
            author.first_name = data.get('first_name', author.first_name)
            author.last_name = data.get('last_name', author.last_name)
            author.bio = data.get('bio', author.bio)
            author.birth_date = data.get('birth_date', author.birth_date)
            author.save()
            return JsonResponse({
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'bio': author.bio,
                'birth_date': author.birth_date.isoformat() if author.birth_date else None
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    def delete(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        author.delete()
        return JsonResponse({'message': 'Author deleted successfully'}, status=204)
