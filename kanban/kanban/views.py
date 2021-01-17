from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from django.http import HttpResponse


def index(request):
    """
    トップページの初期表示アクション
    indexというビューを定義
    """
    # テンプレートを指定せずに文字列を直接指定 文字列をレスポンスとして返すときはHttpResponse()関数を使用する
    # return HttpResponse('仮のトップページ')

    # テンプレートを指定するときはrender()関数で
    return render(request, 'kanban/index.html')

@login_required
def home(request):
    """
    ホーム画面の初期表示アクション
    """
    return render(request, 'kanban/home.html')

def signup(request):
    """
    サインアップ画面のアクション
    """
    if request.method == 'POST':
        # 入力値を取得
        form = UserCreationForm(request.POST)
        # 入力値のバリデーション実行
        if form.is_valid():
            # データの永続化・モデルのインスタンスを取得
            user_instance = form.save()
            login(request, user_instance)
            return redirect('kanban:home')
    else:
        # フォームクラスのインスタンスを作成
        # →サインアップに必要な情報を入力するフォームを表示するため
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'kanban/signup.html', context)

# classで定義すると再利用可能な汎用クラスビューを継承して実装できる
# pythonではあまりオブジェクト指向的なクラスのイメージを持って書かない方がいいかもしれない、別物感がある
class UserDetailView(DetailView):
    model = User
    template_name = 'kanban/users/detail.html'