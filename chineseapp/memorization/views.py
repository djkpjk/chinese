from django.shortcuts import render, get_object_or_404
from .models import ChineseSentence

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lesson_base(request, lesson):
    sentences = ChineseSentence.objects.filter(lesson=lesson)
    length = len(sentences)
    return render(request, 'lesson_base.html', {'sentences': sentences, 'length': length, 'lesson': lesson})

def quiz(request, lesson):
    sentences = ChineseSentence.objects.filter(lesson=lesson)
    length = len(sentences)
    return render(request, 'quiz.html', {'sentences': sentences, 'length': length, 'lesson': lesson})

