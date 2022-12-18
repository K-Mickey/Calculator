from django.shortcuts import render
from .forms import *
from .utils import solve_problem


def index(request):
    context = {
        'form': MatchForm(),
        'result': 0,
    }
    if request.method == 'POST':
        form = MatchForm(request.POST)

        if form.is_valid():
            problem = form.cleaned_data.get('problem')
            try:
                result = solve_problem(problem)
            except:
                result = 'Incorrect input'
            context = {'result': result}
    return render(request, 'calculate/index.html', context)
