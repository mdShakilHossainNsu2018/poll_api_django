from django.urls import path
# from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSets, ChoiceViewSets, VoteViewSets, \
    CreateUser, LoginView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('polls', PollViewSets, basename='polls')
router.register('choices', ChoiceViewSets, basename='choices')
router.register('votes', VoteViewSets, basename='votes')

urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    path("users/", CreateUser.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    # path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
]

urlpatterns = urlpatterns + router.urls
