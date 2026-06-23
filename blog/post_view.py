from django.http import HttpResponse
from django.views.generic import ListView, DetailView

class PostView(ListView):
    template_name = "index.html"

    def get_queryset(self):
        from .models import Post  # Importação segura dentro do método
        return Post.objects.filter(status=1).order_by('-created_on')

class PostDetail(DetailView):
    template_name = "post_detail.html"

    def get_queryset(self):
        from .models import Post  # Importação segura aqui também
        return Post.objects.all()