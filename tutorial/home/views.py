from django.views.generic import TemplateView #for class bases views
from home.forms import HomeForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Post

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created') #Post.objects.all()
        #users = User.objects.all()
        users = User.objects.exclude(id=request.user.id) # 디비에 있는 모든 데이터 얻어오고 인자에 있는 건 필터링한다. 

        args = {'form':form, 'posts':posts, 'users':users}
        return render(request, self.template_name,args)

    def post(self, request):
        form = HomeForm(request.POST)  #with the data
        if form.is_valid():
            post =form.save(commit=False) #post데이터를 전부 저장한다.
            post.user = request.user
            post.save() #django shell로 데이터 확인할 수 있다.

            text = form.cleaned_data['post']   #cleaned_data 쓰게 되면 sql인젝션 같은 걸 거를 수 있다. 위에 있는 post는 forms.py에 정의한 form이다.
            form = HomeForm() #submit 하면 editbox의 데이터가 사라진다.
            return redirect('home:home') #이렇게 하면 페이지 초기화. 데이터 전송 같은거 하고 난 후 쓰면 됨.
        args = {'form': form, 'text':text}
        return render(request, self.template_name, args)
