from django.urls import path

from . import views



urlpatterns = [
     
        path('', views.landing_page, name='landing_page'),
        path('register', views.register, name='register'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
        path('home/', views.home, name='home'),
        path('main/', views.main, name='main'),
        path('predict/', views.predict, name='predict'),
        path('current_predictions/', views.current_predictions, name='current_predictions'),
        path('current_predictions/user/', views.user_current_predictions, name='user_current_predictions'),
        path('notifications/mark_as_read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
        path('prediction_history/', views.prediction_history, name='prediction_history'),
        path('chart/', views.chart, name='chart'),
        path('users/', views.users, name='users'),
        path('prediction_history/', views.prediction_history, name='prediction_history'),

        
   ]