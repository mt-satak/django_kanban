from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
  """
  リストのModelクラス
  """
  # タイトル
  title = models.CharField(max_length=200)
  # 作成ユーザ
  # ForeignKey()で１リスト：多ユーザを表現
  # models.CASCADEで紐づいたユーザが削除された時の挙動を指定 -> ユーザが削除されたらリストも削除される
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


class Card(models.Model):
  """
  カードのModelクラス
  """
  # タイトル
  title = models.CharField(max_length=200)
  # 説明文(テキスト型・文字数制限なし)
  description = models.TextField()
  # 作成ユーザ
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # 紐づくリスト
  list = models.ForeignKey(List, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
