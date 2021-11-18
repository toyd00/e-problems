from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:pk>/', views.user, name='user'),
    path('subject/', views.subject, name='subject'),
    path('test/<int:pk>/', views.miniTest, name='test'),
    path('like/<int:pk>/', views.like, name='like'),
    path('make_problem/', views.make_problem, name='make_problem'),
    path('edit_problem/<int:pk>/', views.edit_problem, name='edit_problem'),
    path('get_title/', views.get_title, name='get_title'),
    #path('delete_problem/<int:pk>/', views.delete_problem, name='delete_problem'),
    path('my_problem/', views.show_myProblem, name='my_problem'),
    path('test_result/<int:problem_count>/', views.score_test, name='test_result'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contact/', views.contact, name='contact'),
    path('thank/', views.thank, name='thank'),
]
