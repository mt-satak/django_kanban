from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from .forms import UserForm, ListForm, CardForm
from .mixins import OnlyYouMixin
from .models import List, Card

def index(request):
    """
    トップページの初期表示
    indexというビューを定義
    """
    # テンプレートを指定せずに文字列を直接指定 文字列をレスポンスとして返すときはHttpResponse()関数を使用する
    # return HttpResponse('仮のトップページ')

    # テンプレートを指定するときはrender()関数で
    return render(request, 'kanban/index.html')


@login_required
def home(request):
    """
    ホーム画面の初期表示
    """
    return render(request, 'kanban/home.html')


def signup(request):
    """
    サインアップ画面
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
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'kanban/users/detail.html'


class UserUpdateView(OnlyYouMixin, UpdateView):
    model = User
    template_name = 'kanban/users/update.html'
    form_class = UserForm

    # メソッド関数の宣言では、オブジェクト自体を表す第一引数を明示しなければなりません。
    # 第一引数のオブジェクトはメソッド呼び出しの際に暗黙の引数として渡されます。
    # https://docs.python.org/ja/3.8/tutorial/classes.html
    def get_success_url(self):
        return resolve_url('kanban:users_detail', pk=self.kwargs['pk'])


class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = 'kanban/lists/create.html'
    form_class = ListForm
    success_url = reverse_lazy('kanban:lists_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListListView(LoginRequiredMixin, ListView):
    model = List
    template_name = 'kanban/lists/list.html'


class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = 'kanban/lists/detail.html'


class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    template_name = 'kanban/lists/update.html'
    form_class = ListForm

    def get_success_url(self):
        return resolve_url('kanban:lists_detail', pk=self.kwargs['pk'])


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = 'kanban/lists/delete.html'
    form_class = ListForm
    success_url = reverse_lazy('kanban:lists_list')


class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = 'kanban/cards/create.html'
    form_class = CardForm
    success_url = reverse_lazy('kanban:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
