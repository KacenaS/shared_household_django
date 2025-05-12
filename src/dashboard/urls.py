from django.urls import path
from dashboard.views import HomepageView, FeedCatView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('cat/feed/', FeedCatView.as_view(), name='feed_cat'),
]