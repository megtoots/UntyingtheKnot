from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login_view, name='login'),
    #path('home/', user_views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('main-page/', user_views.main_page, name='main_page'),
    path('main-page/aboutus.html', user_views.about_us, name='about_us'),
    path('main-page/educational_materials.html', user_views.educational_materials, name='educational_materials'),
    path('main-page/childhood.html', user_views.childhood, name='childhood'),
    path('main-page/pastexp.html', user_views.past_exp, name='past_exp'),
    path('main-page/currentc.html', user_views.currentc, name='currentc'),
    path('main-page/healthandwell.html', user_views.healthandwell, name='healthandwell'),
    path('main-page/rewards.html', user_views.rewards, name='rewards'),
    path('main-page/relaxation_techniques1.html', user_views.reltech1, name='relaxation_techniques1'),
    path('main-page/relaxation_techniques.html', user_views.reltech2, name='relaxation_techniques'),
    path('main-page/relaxation_techniques2.html', user_views.reltech3, name='relaxation_techniques2'),
]
