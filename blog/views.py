from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import authenticate, login, logout
from .forms import BlogForm

# post = [
#     {
#         'author':'CoreyMS',
#         'title':'Blog Post 1',
#         'content':'First post content',
#         'date_posted':'August 27, 2018'
#     },
#         {
#         'author':'Jane Doe',
#         'title':'Blog Post 2',
#         'content':'Second post content',
#         'date_posted':'August 28, 2018'
#     }
# ]

# Create your views here.
def homePage(request):
    post = Post.objects.all().order_by('-date_posted')
    context = {'post':post}
    return render(request, 'blog/home.html', context)

def aboutPage(request):
    return render(request, 'blog/about.html')


def updatePage(request, pk):
    page = Post.objects.get(id=pk)
    context = {'page':page}
    return render(request, 'blog/update.html', context)

def editBlog(request, pk):
    page = Post.objects.get(id=pk)
    form = BlogForm(instance=page)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'blog/edit-blog.html', context)



def deleteBlog(request, pk):
    delp = Post.objects.get(id=pk)
    if request.method == 'POST':
        delp.delete()
        return redirect('/')
    context = {'delp':delp}
    return render(request, 'blog/delete.html', context)


