from django.views.generic import TemplateView #for class bases views
from home.forms import HomeForm
from django.shortcuts import render, redirect
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = HomeForm(request.POST)  #with the data
        if form.is_valid():
            text = form.cleaned_data['post']   #cleaned_data 쓰게 되면 sql인젝션 같은 걸 거를 수 있다. 위에 있는 post는 forms.py에 정의한 form이다.
            form = HomeForm() #submit 하면 editbox의 데이터가 사라진다.
            return redirect('home:home') #이렇게 하면 페이지 초기화. 데이터 전송 같은거 하고 난 후 쓰면 됨.
        args = {'form': form, 'text':text}
        return render(request, self.template_name, args)