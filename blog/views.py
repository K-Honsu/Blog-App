from django.shortcuts import render
from .models import Post
from django.contrib.auth import authenticate, login, logout

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
    post = Post.objects.all()
    context = {'post':post}
    return render(request, 'blog/home.html', context)

def aboutPage(request):
    return render(request, 'blog/about.html')


def blogPage(request,pk):
    blog = Post.objects.get(id=pk)
    context = {'blog':blog}
    return render(request, 'blog/update_blog.html', context)


