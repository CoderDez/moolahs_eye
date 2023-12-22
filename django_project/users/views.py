from typing import Any
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        username = user.username
        messages.success(self.request, message=f"Your account has been created for {username}! You can now login!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    
class ProfileView(LoginRequiredMixin, FormView):

    template_name = 'users/profile.html'
    form_class = UserUpdateForm
    profile_form_class = ProfileUpdateForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["title"] = "Profile"
        return context

    def get(self, request, *args, **kwargs):
        u_form = self.form_class(instance=request.user)
        p_form = self.profile_form_class(instance=request.user.profile)

        return self.render_to_response(
            self.get_context_data(u_form=u_form, p_form=p_form)
        )

    def post(self, request, *args, **kwargs):
        u_form = self.form_class(
            request.POST, 
            instance=request.user
        )

        p_form = self.profile_form_class(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect(self.success_url)
        
        else:
            return self.form_invalid(u_form=u_form, p_form=p_form)

    def form_invalid(self, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))