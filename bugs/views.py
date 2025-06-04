from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from rest_framework import generics
from .models import Bug
from .forms import BugForm
from .serializers import BugSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# API Views
class BugListCreateView(generics.ListCreateAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

class BugDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

# Template Views
def home(request):
    return render(request, 'bugs/home.html')

def bug_list(request):
    bugs = Bug.objects.all().order_by('-created_at')
    paginator = Paginator(bugs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bugs/bug_list.html', {'page_obj': page_obj})

def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, 'bugs/bug_detail.html', {'bug': bug})

def bug_create(request):
    form = BugForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bug-list')
    return render(request, 'bugs/bug_form.html', {'form': form})

def bug_edit(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    form = BugForm(request.POST or None, instance=bug)
    if form.is_valid():
        form.save()
        return redirect('bug-detail', pk=pk)
    return render(request, 'bugs/bug_edit_form.html', {'form': form, 'bug': bug})
