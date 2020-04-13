from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
# Create your views here.
from django.contrib import messages

# Registration view
def register(req):
    form = UserRegistrationForm()
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}')
            form.save()
            return redirect('login')
    return render(req, 'user/register.html', {'form': form})

# for login and logout views I am using build-in LoginView and LogoutView 