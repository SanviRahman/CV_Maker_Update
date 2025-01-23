from .forms import CustomUserCreationForm, FormMakerForm
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FormMaker
from django.http import HttpResponse





#I want to write here home page
def home(request):
    tasks = FormMaker.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def registers(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please login.")
            return redirect('logins')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registers.html', {'form': form})



def logins(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('cvmaker')  
        else:
            messages.error(request, "Invalid email or password. Please try again.")
    return render(request, 'logins.html')




#I want to write here cv details

def cv_details(request,pk):
    try:
        tasks = FormMaker.objects.get(pk=pk)
        return render(request, 'cv_details.html', {'tasks': tasks}) 
    except FormMaker.DoesNotExist:
        return HttpResponse("No such CV exists")




#CRUD STARTS HERE

@login_required
def cvmaker(request):
    if request.method == "POST":
        form = FormMakerForm(request.POST, request.FILES)  # Ensure you handle file uploads as well
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.customuser = request.user  # Associate with the current logged-in user
            form_instance.save()
            return redirect('approved', pk=form_instance.pk)  # Redirect to the approved page with the correct pk
    else:
        form = FormMakerForm()
    return render(request, 'cvmaker.html', {'form': form})






def cv_update(request, pk):
    task = get_object_or_404(FormMaker, pk=pk)
    
   
    if request.method == 'POST':
        form = FormMakerForm(request.POST, instance=task)  
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = FormMakerForm(instance=task)
    
    return render(request, 'cv_update.html', {'form': form})




#I want to write here cv_delete
def cv_delete(request, pk):
    try:
        tasks = FormMaker.objects.get(pk=pk)
        tasks.delete()
        return redirect('home')
    except FormMaker.DoesNotExist:
        return HttpResponse('Task not found',status=404)
#CRUD ENDS HERE


#I want to write here approved
def approved(request, pk):
    try:
        form_instance = FormMaker.objects.get(pk=pk)
        return render(request, 'approved.html', {'form_instance': form_instance})
    except FormMaker.DoesNotExist:
        return HttpResponse("No such CV exists", status=404)


# I want to write here logout
def logout(request):
    auth_logout(request)  
    return redirect('home') 

    




