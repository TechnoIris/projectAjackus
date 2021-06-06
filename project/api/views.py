from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from form import UserRegister, UploadBook
from api import Author, Contitem, Admin


# Create your views here.
def UserRegview(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Record is Saved.')
        else:
            form = UserRegister()
            context = {
                    'form':form,
                    }
            return render(request, 'api/your_page.html')

#design for admin login only
def IndexAdmin(generic.ListView):
    context_object_name = 'index_file'
    template_name = 'api/admin.html'

    def get_queryset(self):
        return Admin.objects.all()


class IndexAuthor(generic.ListView):
    context_object_name = 'reg_file'
    template_name = 'api/author.html'

    def get_queryset(self):
        return Author.objects.all()

class IndexBook(generic.ListView):
    context_object_name = "create_book"
    template_name = 'book.html'

    def get_queryset(self):
        return Contitem.objects.all()

#for form of Author registration
class AuthorEntry(CreateView):
    model = Author
    fields = ['email', 'password', 'fullname', 'phone', 'city', 'state', 'country', 'pincode']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('api:author')

class CreateBook(CreateView):
    model = Contitem
    fields = ['title', 'body', 'summary', 'pdf']

class DeleteBook(DeleteView):
    model = Contitem
    success_url = reverse_lazy('api:book')

class SearchBook(generic.ListView):
    q = Q()
    model = Contitem
    template_name = 'searchBook'
    if title:
        q |= Q(title__contains==search_text):
            result = document.objects.filter(q)
    elif body:
        q |= Q(body__contains==search_text):
            result = document.objects.filter(q)
    return result
