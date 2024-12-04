from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

class UserRegisterView(CreateView):
    form_class = UserCreationForm 
    template_name = 'users/register.html'
    success_url = reverse_lazy('login') 

    def form_valid(self, form):
        """ Log the user in after successful registration """
        user = form.save()
        login(self.request, user) 
        return redirect(self.success_url)
