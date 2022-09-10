from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


@login_required()
def my_profile_view(request):
    profile_ = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_)
    confirm = False

    if form.is_valid():
        form.save()
        confirm = True

    context = {
        "profile": profile_,
        "form": form,
        "confirm": confirm,
    }
    return render(request, "profiles/main.html", context=context)
