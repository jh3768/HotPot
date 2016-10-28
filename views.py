from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from polls.models import Product
# Create your views here.

'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
'''

def homepage(request):
    product = Product.objects.all()
    context = {}
    context['product'] = product
    return render(request, 'polls/homepage.html', context)

def login(request):
    return render(request, 'polls/login.html')

def signup(request):
    return render(request, 'polls/signup.html')

def auth_and_login(request, onsuccess='/polls/profile', onfail='/polls/login'):
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)

def auth_and_signup(request, onsuccess='/polls/profile', onfail='/polls/signup'):
    username = request.POST.get('email')
    password = request.POST.get('password')
    if not user_exists(username): 
        user = User(username=username, email=username)
        user.set_password(password)
        user.save()
        auth_login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)    

def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def profile(request):
    if request.user.username:
        context = {}
        context['username'] = request.user.username
        product = Product.objects.filter(username=request.user.username)
        context['product'] = product
        return render(request, "polls/profile.html", context)
    else:
        return redirect('/polls/login')

def post(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    description = request.POST.get('description')
    username = "rondogency@gmail.com"
    product = Product(name=name, username=username, price=price, description=description)
    product.save()
    return redirect('/polls/profile')

def delete(request):
    return redirect('/polls/login')  