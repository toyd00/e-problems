from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:pk>/', views.user, name='user'),
    path('subject/<int:pk>/', views.subject, name='subject'),
    path('problem/<int:pk>/', views.miniTest, name='problem'),
    path('like/<int:pk>/', views.like, name='like'),
    path('make_problem/<int:pk>/', views.make_problem, name='make_problem'),
    path('edit_problem/', views.edit_problem, name='edit_problem'),
    path('test_result/<int:problem_count>/', views.score_test, name='test_result'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contact/', views.contact, name='contact'),
    path('thank/', views.thank, name='thank'),
]
