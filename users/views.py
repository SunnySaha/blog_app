from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, UpdateForm, UpdateProfile
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration Successfully for {username}! Ready to LogIn')
            return redirect('login')
        else:
            messages.error(request, f'Error Registration')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'forms': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateForm(request.POST, instance=request.user)
        profile_form = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Information Updated')
            return redirect('profile')
    else:
        user_form = UpdateForm(instance=request.user)
        profile_form = UpdateProfile(instance=request.user.profile)

    context = {

        'u_form': user_form,
        'p_form': profile_form,
    }
    return render(request, 'users/profile.html', context)
