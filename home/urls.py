from django.urls import path
from . import views

urlpatterns = [
    # Page views
    path('', views.index, name='index'),
    path('about', views.about_us, name='about'),
    path('solved_cases', views.solved_cases_list, name='solved_cases'),
    path('solved_cases/<int:pk>', views.solved_case_detail, name='solved_case_detail'),
]