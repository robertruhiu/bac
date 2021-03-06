from django.contrib import messages
from django.db import transaction
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import ProfileEditForm, UserEditForm, DeveloperProfileEditForm, RecruiterProfileEditForm
from django.shortcuts import render, redirect
from accounts.models import Profile


# Create your views here.

@login_required
def profile(request, username=None):
    if username:
        u = User.objects.get(username=username)
        user = u
    else:
        user = request.user
    return render(request, 'accounts/profile.html', {'user': user})


@login_required
def update_profile(request):
    if request.user.profile.user_type == 'developer':

        if request.method == 'POST':
            user_form = UserEditForm(request.POST, instance=request.user)
            profile_form = DeveloperProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                # messages.success(request, ('Your profile was successfully saved'))
                return redirect('frontend:index')
            else:
                print('Failed')
                # messages.error(request, ('Please correct the error below.'))
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = DeveloperProfileEditForm(instance=request.user.profile)
            return render(request, 'frontend/profile_edit_form.html',
                          {'user_form': user_form, 'profile_form': profile_form})
    elif request.user.profile.user_type == 'recruiter':
        if request.method == 'POST':
            user_form = UserEditForm(request.POST, instance=request.user)
            profile_form = RecruiterProfileEditForm(request.POST, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                # messages.success(request, ('Your profile was successfully saved'))
                return redirect('frontend:index')
            else:
                print('Failed')
                # messages.error(request, ('Please correct the error below.'))
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = RecruiterProfileEditForm(instance=request.user.profile)
            return render(request, 'frontend/profile_edit_form.html',
                          {'user_form': user_form, 'profile_form': profile_form})
