from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Obtiene todas las publicaciones
    return render(request, 'blog/post_list.html', {'posts': posts})  # Renderiza la plantilla
