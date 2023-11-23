# urls.py
from django.urls import path
from .views import NoticePostListView, NoticePostCreateView, NoticePostDetailView, NoticePostUpdateView

urlpatterns = [
    path('notice/', NoticePostListView.as_view(), name='notice-list'),
    path('notice/create/', NoticePostCreateView.as_view(), name='notice-create'),
    path('notice/<int:pk>/', NoticePostDetailView.as_view(), name='notice-detail'),
    path('notice/<int:pk>/update/', NoticePostUpdateView.as_view(), name='notice-update'),

]
