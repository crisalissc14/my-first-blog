from django.shortcuts import render

#create
def post_list(request):
    return render(request, 'blog/post_list.html', {})

