from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice, Etc_data, Feedback


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    if request.POST.get('fb', False):
        fb_text = Feedback(feedback_text=request.POST.get('fb', False))
        fb_text.save()

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
