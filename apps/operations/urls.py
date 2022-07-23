from django.conf.urls import url

from apps.operations.views import UserFavView

urlpatterns = [
    url(r'^fav/$', UserFavView.as_view(), name="fav"),
]
