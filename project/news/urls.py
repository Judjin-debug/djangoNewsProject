from django.urls import path
from .views import NewsList, NewsSearchView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetailView.as_view(), name='news_contents'),
    path('search', NewsSearchView.as_view(), name='news_search'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('create/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete')
]

