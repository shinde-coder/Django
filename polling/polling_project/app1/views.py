from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import *
from django.http import Http404
from django.urls import reverse
from .forms import QuestionForm

# Create your views here.
def index(request):
    q_list = Question.objects.order_by("-pub_text")
    return render(request,"index.html",{"q_list":q_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist: 
        raise Http404("Question Does Not Exist")
    
    return render(request, "detail.html",{"question": question})

def results(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist: 
        raise Http404("Question Does Not Exist")
    
    return render(request, "results.html",{"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.voters+= 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def data_form(request):
    if request.method=="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question=form.save()
            print(question.id)
        return redirect("index")
    else:
        form = QuestionForm()
        return render(request, "data_form.html", {"form":form})
    

def delete(request, id):
    try:
        question = Question.objects.get(id=id)
        question.delete()
    except Question.DoesNotExist:
        pass

    return redirect("index")  

def data_edit(request, id):
    employee = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = QuestionForm(instance=employee)
    return render(request, "data_form.html", {"form":form})