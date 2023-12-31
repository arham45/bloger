from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.shortcuts import render, get_object_or_404
from .models import Newpage




# Create your views here.
def home(request): 
    newpages = Newpage.objects.all()
    return render(request,'home/home.html',{'newpages': newpages})

def about(request): 
    return render(request,'home/about.html')

from home.models import Contact

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name) <2 or len(email) <3 or len(phone) <10 or len(content) <4:
         messages.error(request,"plz fill the form correctly")
        else:
         contact=Contact(name=name, email=email, phone=phone, content=content)
         contact.save()
         messages.success(request,"your form have been suucessfully submitted!!")

    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        username2=request.POST['username2']
        Password2=request.POST['Password2']

        user=authenticate(username= username2, password= Password2)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

  # You should create a form for creating new pages
  # 

def page_detail(request, newpage_slug):
    newpage = get_object_or_404(Newpage, slug=newpage_slug)
    return render(request, 'home/page_detail.html', {'newpage': newpage, 'active_slug': newpage_slug })










  
