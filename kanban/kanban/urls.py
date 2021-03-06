from django.urls import path

from . import views

# アプリ名を設定
app_name = 'kanban'

urlpatterns = [
    # path()関数
    # route  必須 URLパターン文字列
    # view   必須 ビュー関数 画面応答のアクションを指定する
    # name   任意 URL名称を定義
    # kwargs 任意 追加引数を辞書でビューに渡す時に指定する
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    # ユーザ
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='users_detail'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='users_update'),
    # リスト
    path('lists/', views.ListListView.as_view(), name='lists_list'),
    path('lists/create/', views.ListCreateView.as_view(), name='lists_create'),
    path('lists/<int:pk>/', views.ListDetailView.as_view(), name='lists_detail'),
    path('lists/<int:pk>/update/', views.ListUpdateView.as_view(), name='lists_update'),
    path('lists/<int:pk>/delete/', views.ListDeleteView.as_view(), name='lists_delete'),
    # カード
    path('cards/', views.CardListView.as_view(), name='cards_list'),
    path('cards/create/', views.CardCreateView.as_view(), name='cards_create'),
    path('cards/<int:pk>/', views.CardDetailView.as_view(), name='cards_detail'),
    path('cards/<int:pk>/update/', views.CardUpdateView.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDeleteView.as_view(), name='cards_delete'),
]
