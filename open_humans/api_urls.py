from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .api_views import MemberDetailAPIView

urlpatterns = [
    url(r'^member/$', MemberDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
