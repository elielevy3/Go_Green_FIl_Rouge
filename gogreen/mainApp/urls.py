from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import UserViewset, ChallengeViewset, CategorieViewset, QuestionViewset, ScoreList, AcceptedChallengesList, AcceptedChallengeDetail, ScoreDetail, CalculateGrade

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.include_format_suffixes = False
router.register(r'users', views.UserViewset)
router.register(r'challenges', views.ChallengeViewset)
router.register(r'categories', views.CategorieViewset)
router.register(r'questions', views.QuestionViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('scores/', views.ScoreList.as_view()),
	path('accepted_challenges/', views.AcceptedChallengesList.as_view()),
    path('scores/<int:pk>', views.ScoreDetail.as_view()),
    path('accepted_challenges/<int:pk>', views.AcceptedChallengeDetail.as_view()),
    path('calculate_grade/', views.CalculateGrade)
]

urlpatterns = format_suffix_patterns(urlpatterns)
