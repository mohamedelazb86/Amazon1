from django.shortcuts import render,redirect
from .forms import UserForm,Activate_Codeform
from django.core.mail import send_mail
from .models import Profile
from django.contrib.auth.models import User


def signup(request):
    
    if request.method =='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            user=form.save(commit=False)
            user.is_active=False

            form.save()  # trigger singanls and create profile
            # send email
            profile=Profile.objects.get(user__username=username)

            send_mail(
                " Activate  code  ",
                f" welcome {username}\n use this code {profile.code}",
                "r_mido99@yahoo.com",
                [email],
                fail_silently=False,
                )
            return redirect(f'/accounts/{username}/activate')
    else:
        form = UserForm()
    

    
        
    return render(request,'accounts/signup.html',{'form':form})


def activate_code(request,username):
    profile=Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form=Activate_Codeform(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''

                user=User.objects.get(username=username)
                user.is_active=True

                user.save()
                profile.save()

                return redirect('/accounts/login')
    else:
        form=Activate_Codeform()

        
            
            

    return render(request,'accounts/activate.html',{'form':form})


