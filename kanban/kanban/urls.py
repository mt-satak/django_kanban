from django.urls import path

from . import views

# アプリ名を設定
app_name = "kanban"

urlpatterns = [
    # path()関数
    # route  必須 URLパターン文字列
    # view   必須 ビュー関数 画面応答のアクションを指定する
    # name   任意 URL名称を定義
    # kwargs 任意 追加引数を辞書でビューに渡す時に指定する
    path('', views.index, name='index'),
]
