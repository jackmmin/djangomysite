from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice, Etc_data, Feedback_Choice, Fb_Choice_Data, Feedback_Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    fb_c_list = Feedback_Choice.objects.all()
    feedback_question = Feedback_Question.objects.all()
    context = {'latest_question_list': latest_question_list, 'fb_c_list': fb_c_list}

    # if request.POST.get('fb', False):
    #     fb_text = Feedback(feedback_text=request.POST.get('fb', False))
    #     fb_text.save()

    # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    try:
        if request.POST.get('fb_c', False):
            q = Feedback_Question.objects.get(pk=1)
            fb_choice = q.feedback_choice_set.get(pk=request.POST['fb_c'])
            fb_choice.votes += 1
            fb_choice.save()

        if request.POST.get('fb_choice_text'):
            pk = 2
            fb_text = Fb_Choice_Data(fb_etc_text=request.POST.get('fb_choice_text'), feedback_c_id=pk)
            fb_text.save()

    except():
        return render(request, 'polls/index.html')
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    votes_orderby = Choice.objects.filter(question_id=question_id).order_by('-votes')

    # etc_data = get_object_or_404(Etc_data, question_id=question_id)
    # etc_data = get_object_or_404(Etc_data, pk=question_id)

    # return render(request, 'polls/results.html', {'question2': question}, {'etc_data': etc_data})
    return render(request, 'polls/results.html', {'question2': question, 'votes_orderby': votes_orderby})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        if request.POST['etc']:
            etc_data_temp = Etc_data(etc_text=request.POST['etc'], question_id=question_id)
            etc_data_temp.save()

        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # selected_choice = question.choice_set.filter(pk=selected_choice_list)
        # selected_choice.votes += 1
        # selected_choice.save()

        selected_choice_list = request.POST.getlist('choice')
        for choice in selected_choice_list:
            selected_choice = question.choice_set.get(pk=choice)
            selected_choice.votes += 1
            selected_choice.save()

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    except(KeyError, Etc_data.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't text.",
        })

    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()

    # messages.info(request, choice_text_temp)

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
