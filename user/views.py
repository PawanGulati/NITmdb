from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import messages


def register(req):
    form = UserCreationForm()
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}')
            form.save()
            return redirect('movie_list')
    return render(req, 'user/register.html', {'form': form})
