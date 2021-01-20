from django.contrib.auth.mixins import UserPassesTestMixin

class OnlyYouMixin(UserPassesTestMixin):
  """
  ユーザの権限管理を行うクラス
  """
  # 制限に引っかかったら例外投げるための設定
  raise_exception = True

  def test_func(self):
    """
    ページのPKとユーザのPKを比較した結果を返却する
    """
    # ユーザのインスタンスを取得
    user = self.request.user
    return user.pk == self.kwargs['pk']
