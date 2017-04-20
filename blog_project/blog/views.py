from django.shortcuts import render
from .models import Blog, UserForm, UserProfile, UserProfileForm, BlogForm,User
# Create your views here.
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .models import UserForm, UserProfileForm
from django.http import HttpResponseRedirect,Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Index Page / Login Verfication
def index(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username = username, password = password)

        if user:
            login(request,user)
            return HttpResponseRedirect('posts')
        else:
            return render(request,'blog/fail.html',{})

    else:
        return render(request,'blog/index.html',{})

#Register View
def register(request):
    registered= False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            #Save the User's Form in our database
            user = user_form.save()
            # Hashes the Password and Saves to our database
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'blog/register.html',{'user_form': user_form, 'registered':registered})


@login_required(login_url="/blog/")
def show_all_posts(request):
    objects= Blog.objects.all()
    context={"blog": objects}
    return render(request,'blog/post.html',context)



@login_required(login_url="/blog/")
# Specific Blog Post Display
def blog_post(request,blog_id):
    try:
        objects= Blog.objects.get(id = blog_id)
        context={"entry": objects}
    except:
        raise Http404("Post Does not exists.")

    return render(request, 'blog/single_post.html', context)

@login_required(login_url='/blog/')
#Adds a post to the blog and redirects to homepage
def add_post(request):
    #A HTTP POST?
    if request.method == 'POST':
        form = BlogForm(request.POST)

        #Have we provided witha valid form
        if form.is_valid():
            #Savae the new category to the database
            entry = form.save(commit=False)
            current_user = request.user
            user_instance = UserProfile.objects.get(user=current_user)
            entry.user = user_instance
            entry.save()


            #Now Call the index() view
            #The user will be show the homepage.
            return HttpResponseRedirect(reverse('posts'))
        else:
            print(form.errors)

    else:
        #If the request was not a POST, display the form to enter details
        form = BlogForm()

    return render(request,'blog/add_blog.html',{'form':form})

@login_required(login_url='/blog/')
#Logs out an User
def user_logout(request):
    logout(request)
    messages.success(request,"You have been successfully logged out!")
    return HttpResponseRedirect('/blog/')



@login_required(login_url='login')
#Deletes a post selected
def delete_post(request,blog_id):
    """Deletes a post upon its id/primary_key"""
    object = Blog.objects.get(pk=blog_id)
    object.delete()
    return HttpResponseRedirect(reverse('posts'))