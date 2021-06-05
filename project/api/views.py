from django.shortcuts import render

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
