from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from .form import SignUpForm, PostForm, LoginForm
from .models import CustomUser, Post

# Create your views here.

class home_view(View):

    def get(self, request):

        return render(request, "Home/profile.html")
    
class post_detail(View):

    def get(request, id):
        post = Post.objects.get(id=id)

        return render(request, 'post_detail.html', {'post': post})
    
class profile_view(View):

    def get(self, request):
        form = PostForm()
        user_posts = Post.objects.filter(author=request.user)
        total_posts = user_posts.count()
        
        return render(request, "Home/profile.html", {'form': form, 'posts': user_posts, 'total_posts': total_posts})

    def post(self, request):

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
           
            
            return redirect('profile')
        
        user_posts = Post.objects.filter(author=request.user)
        total_posts = user_posts.count()
        #needed to use the built in count to count the instances of post object, used autho=request.user to 
        #filter it to specific users. 
        return render(request, "Home/profile.html", {'form': form, 'post': user_posts, 'total_posts': total_posts})
    


    
class register_view(View):

    def get(self, request):

        form = SignUpForm()

        return render(request, "login/register.html", {"form": form})
    
    def post(self, request):
        
        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            # username = request.POST.get("username")

            # email = request.POST.get("email")

            # password = request.POST.get("password1")

            # user = CustomUser.objects.create_user(username=username, email=email, password=password)

                #no need to manually extract all the data since the form collects those 
            
            user.set_password(form.cleaned_data['password'])

            user.save()

        return redirect("login")    

class login_view(View):

    def get(self, request):

        form = LoginForm()

        return render(request, "login/login.html", {'form': form})
    
    
    def post(self, request):

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                form.add_error(None, "Invalid username or password")
        
        return render(request, 'login/login.html', {'form': form})
    
#make posts counter work

    #home_view - this shows posts from other users, home where you scroll and see other posts
    #shows users own profile and posts and details