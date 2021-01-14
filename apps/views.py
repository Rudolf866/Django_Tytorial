# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from apps.forms import UserForm, PersonUserForm
from apps.models import Person, Post


def index(request):
    people = Person.objects.all()
    userform = UserForm(request.POST)
    list = (12, 678, 999, 'Ferrum')
    data = {"name": "Rudik", "age": 33, "list": list, "form": userform, "people": people}
    if request.method == "POST":
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")
    else:
        return TemplateResponse(request, "apps/index.html", data)


def about(request):
    return TemplateResponse(request, "apps/about.html")


def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect('/')


# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        form = PersonUserForm(initial={'age': person.age, 'name': person.name})
        # form = PersonUserForm()

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return TemplateResponse(request, "apps/edit.html", {"person": person, "form": form})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def post_list(request):
    posts = Post.published.all()
    return TemplateResponse(request, 'apps/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    return TemplateResponse(request, 'apps/detail.html', {'post': post})
