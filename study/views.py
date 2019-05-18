from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, DailyNote
from .forms import DailyNoteForm
from datetime import datetime


# Create your views here.
def first_page(request):
    students = Student.objects.filter(status = True)

    return render(request, 'study/first_page.html', {'students':students,})


def daily_new(request, name, date):
    if request.method == 'POST':
        form = DailyNoteForm(request.POST)
        student = Student.objects.get(name = name)
        print(student.id)
        if form.is_valid():
            dailynote = form.save(commit=False)
            dailynote.name_id = student.id
            dailynote.study_day = date
            dailynote = form.save()
            return redirect('study:daily_detail', dailynote.id)
    else:
        form = DailyNoteForm()
    return render(request, 'study/daily_form.html', {'form':form, 'name': name, 'date': date,})


def daily_list(request):
    startday = datetime.strptime(request.GET['startday'], '%Y-%m-%d')
    endday = datetime.strptime(request.GET['endday'], '%Y-%m-%d')

    if (request.GET['name'] != ''):
        name = request.GET['name']
        student = Student.objects.get(name=name)
        daily_list = DailyNote.objects.filter(study_day__range=[startday, endday]).filter(name=student.id)
        return render(request, 'study/daily_list.html', {'daily_list': daily_list,})
        print (name)

    daily_list = DailyNote.objects.filter(study_day__range=[startday, endday])
    return render(request, 'study/daily_list.html', {'daily_list': daily_list,})


def daily_detail(request, id):
    detail = get_object_or_404(DailyNote ,id=id)
    return render(request, 'study/detail.html', {'detail': detail, })

def daily_update(request, id, name, date):
    post = get_object_or_404(DailyNote, id=id) #수정하고자 하는 글의 Post모델 인스턴스를 가져온다. 원하는 글은 pk를 이용해 찾는다.
    if request.method == "POST":
        form = DailyNoteForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('study:daily_detail', id=id)
    else:
        form = DailyNoteForm(instance=post)
    return render(request, 'study/daily_form.html', {'form':form, 'name': name, 'date': date,});

def daily_delete(request, id):
    post = DailyNote.objects.get(id=id)
    post.delete()
    return redirect('study:first_page')
