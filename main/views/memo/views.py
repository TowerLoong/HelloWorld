from datetime import datetime

from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.utils import timezone

from main.models import Memo
from main.forms.memo.forms import MemoForm


# メモ一覧画面
class MemoListView(generic.ListView):
    model = Memo
    queryset = Memo.objects.order_by('-created_at')
    # 1ページあたりの表示件数
    paginate_by = 10

    template_name = "main/memo/list_memo.html"
    success_url = reverse_lazy('home')


# メモ登録画面
class MemoCreateView(generic.CreateView):
    model = Memo
    form_class = MemoForm
    template_name = "main/memo/memo_form.html"
    success_url = reverse_lazy('main:list_memo')
    object = None

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_at = timezone.now()
        self.object.save()

        return redirect('main:list_memo')


# メモの更新画面
class MemoUpdateView(generic.UpdateView):
    model = Memo
    form_class = MemoForm
    template_name = "main/memo/memo_form.html"
    success_url = reverse_lazy('main:list_memo')
    object = None

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return redirect('main:list_memo')


# メモの削除画面
class MemoDeleteView(generic.DeleteView):
    model = Memo
    success_url = reverse_lazy('main:list_memo')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Memo.objects.get(pk=kwargs['pk'])
        self.object.delete()
        return redirect('main:list_memo')
