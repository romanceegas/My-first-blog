from django.shortcuts import render

# Create ydef post_list(request):
def post_list(request):
    return render(request, 'blog/post_list.html', {})
    
