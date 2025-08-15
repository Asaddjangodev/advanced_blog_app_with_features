from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:profile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def edit(request):
    return render(request, 'accounts/edit.html')