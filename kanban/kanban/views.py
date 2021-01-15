from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    """
    トップページの初期表示アクション
    indexというビューを定義
    """
    # テンプレートを指定せずに文字列を直接指定 文字列をレスポンスとして返すときはHttpResponseを使用する
    return HttpResponse('仮のトップページ')