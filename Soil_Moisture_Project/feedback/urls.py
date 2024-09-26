from django.urls import path

from .views import FeedbackViewSet, feedback_list, mark_as_read


urlpatterns = [
    path('feedback/',
         FeedbackViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('feedback/<int:pk>/', FeedbackViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('admin/list/', feedback_list),
    path('admin/markread/<feedback_id>/', mark_as_read, name="read-feedback"),


]
