from django.views.generic import TemplateView #for class bases views

class HomeView(TemplateView):
    template_name = 'home/home.html'
    
