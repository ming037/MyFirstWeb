from django.views.generic import TemplateView #for class bases views
from home.forms import HomeForm
from django.shortcuts import render
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})
