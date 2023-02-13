from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name="register"),
    path('',TaskList.as_view(),name="tasks"),
    path("task/<int:pk>",TaskDetail.as_view(),name="task"),
    path('task-create/',TaskCreate.as_view(),name="task-create"), 
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="base/password_reset.html"), name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="base/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  


]
