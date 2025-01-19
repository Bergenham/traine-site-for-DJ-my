from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import request
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView
from .models import Profile


# def login_view(request: HttpRequest):
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             return redirect('/admin/')
#         return render(request, 'myauth/login.html')
#
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#
#     if user:
#         login(request, user)
#         return redirect('/admin/')
#     else:
#         return render(request, 'myauth/login.html', context={'error_404': 'User not found'})

class AboutMeView(TemplateView):
    template_name = 'myauth/am.html'

def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('myauth:login'))


# class Login_View(View):
#     def get(self, request: HttpRequest):
#         if request.user.is_authenticated:
#             return redirect('/admin/')
#         return render(request, 'myauth/login.html')
#
#     def post(self, request: HttpRequest):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#
#         if user:
#             login(request, user)
#             return redirect('/admin/')
#         else:
#             return render(request, 'myauth/login.html',
#                           context={'error_404': "Sorry, Not Founded user, check is all OK"})
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    respounse = HttpResponse('Set cookie')
    respounse.set_cookie('foo', 'bzz', max_age=30600)
    return respounse


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('foo', 'None')
    return HttpResponse(f"Cookie value: {value!r}")

@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["test"] = "Is it test session"
    return HttpResponse('Session set!')

@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    sesion_get = request.session.get('test', 'None sesion yet')
    return HttpResponse(f'Session -> {sesion_get!r}')

class Auth_check_View(TemplateView):
    template_name = "myauth/check_aundeficated_user.html"

class Register_user_View(CreateView):
    form_class = UserCreationForm # узнать про кастом!
    success_url = reverse_lazy("myauth:check")
    template_name = 'myauth/register.html'
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        user_name = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request,
                            username=user_name,
                            password=password)
        login(self.request,user=user)
        return response


class Foo_Bar_View(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"foo": "bar", "spam": "ew"})