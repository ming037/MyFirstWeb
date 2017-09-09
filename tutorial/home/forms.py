from django import forms
from home.models import Post
class HomeForm(forms.ModelForm): #forms.form 대신에 ModelForm을 쓰는 이유는. ModelForm은 models.py와 연결되어 있다. 이걸 bound라고 함.
    post = forms.CharField()  #html에서 할 수 있지만 form으로 이런식으로 하는게 더 안전하다.

    class Meta:
        model = Post
        fields = ('post',) #콤마 안하면 tutple이 아니기 때문에 주의하여야 한다.
