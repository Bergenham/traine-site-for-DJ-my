from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (set_cookie_view,
                    get_cookie_view,
                    get_session_view,
                    set_session_view,
                    logout_view,
                    Auth_check_View,
                    Register_user_View,
                    Foo_Bar_View, AboutMeView,
                    )

app_name = 'myauth'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="myauth/login.html",
                                     redirect_authenticated_user=True),
         name='login'),
    path('logout/', logout_view, name='logout'),
    path('cookie/get/', get_cookie_view, name='get-cookie'),
    path('cookie/set/', set_cookie_view, name='set-cookie'),
    path('session/get/', get_session_view, name='get-session'),
    path('session/set/', set_session_view, name='set-session'),
    path('check/', Auth_check_View.as_view(), name='check'),
    path('register/', Register_user_View.as_view(), name='regi'),
    path('foo/', Foo_Bar_View.as_view(), name='json'),
    path('am/', AboutMeView.as_view(), name='am')
]
