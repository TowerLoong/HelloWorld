from django.urls import path

from main.views import views
from main.views.memo.views import MemoListView, MemoUpdateView, MemoCreateView, MemoDeleteView

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),

    #  Memo Projects
    path('memos', MemoListView.as_view(), name='list_memo'),
    path('memos_edit/<int:pk>', MemoUpdateView.as_view(), name='edit_memo'),
    path('memos_new', MemoCreateView.as_view(), name='create_memo'),
    path('memos_delete/<int:pk>', MemoDeleteView.as_view(), name='delete_memo'),
]
