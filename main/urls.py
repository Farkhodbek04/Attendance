from . import views

from django.urls import path

urlpatterns = [
    path('staff-list', views.staff_list ),
    path('staff-create', views.create_staff ),
    path('attendance-create/<int:id>', views.create_attendance ),
    path('daily-attendance', views.daily_attendance)
]