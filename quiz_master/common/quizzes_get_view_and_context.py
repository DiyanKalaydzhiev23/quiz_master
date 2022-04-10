from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render
from quiz_master.accounts.models import Profile
from quiz_master.quiz_app.forms import SearchForm
from quiz_master.quiz_app.models import Quiz


UserModel = get_user_model()


def get_context_data(request, **kwargs):
    context = {}
    quiz_name = kwargs.get('quiz_name')
    pk = kwargs.get('pk')

    if quiz_name:
        quizzes = Quiz.objects.filter(name__icontains=quiz_name).order_by('-id')
    else:
        quizzes = Quiz.objects.all().order_by('-id')

    if pk:
        quizzes = quizzes.filter(author=pk).order_by('-id')
        context['user'] = UserModel.objects.get(id=pk)
        context['profile'] = Profile.objects.get(user_id=pk)

    paginator = Paginator(quizzes, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    context['search_form'] = SearchForm()

    return context


def get(request, pk, quiz_name, template_name):
    context = get_context_data(request, quiz_name=quiz_name, pk=pk)
    return render(request, template_name, context)
