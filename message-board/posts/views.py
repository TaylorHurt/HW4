from multiprocessing.util import is_abstract_socket_namespace
from django.views.generic import ListView
from . models import Post


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = "posts/home.html"
