from django.shortcuts import render, redirect, get_object_or_404

from notice.forms import NoticeForm
from notice.models import Notice


def notice_list(request):
    object_list = Notice.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save()
            return redirect(notice.get_absolute_url())
    else:
        form = NoticeForm()
    return render(request, 'form.html', {'form': form})


def notice_update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            notice = form.save()
            return redirect(notice.get_absolute_url())
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'form.html', {'form': form})


def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'detail.html', {'notice': notice})


def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        notice.delete()
        return redirect('')
    return render(request, 'delete.html')