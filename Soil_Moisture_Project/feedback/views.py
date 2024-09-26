from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404

from Soil_Moisture_App.decorators import login_required_custom
from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer

from Soil_Moisture_App.views import *


class FeedbackViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer




# Mark Notifications as read
def mark_as_read(request, feedback_id):
    # Fetch the notification by ID and mark it as read
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.mark_read()
    
    # Redirect back to the notifications page or wherever appropriate
    return redirect('home')


@login_required_custom
def feedback_list(request):
    feedback = Feedback.objects.filter(is_read=False)

    dashboard_context = get_dashboard_data()

    # Weather
    city = 'Kampala'
    weather_data = get_weather_forecast(city)

    # Notifications
    notifications = Notification.objects.filter(user=request.user, is_read=False)

    count = Notification.objects.filter(user=request.user, is_read=False).count()

    context = {
        'feedback': feedback,
        'dashboard_context': dashboard_context, 
        'weather_data': weather_data,
        'notifications': notifications,
    }
    return render(request, 'feedback/admin.html', context)
