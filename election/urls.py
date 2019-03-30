from django.urls import path
from election.views import GetListParties, GetDetailParty

urlpatterns = [
    path('', GetListParties.as_view()),
    path('<int:pk>/', GetDetailParty.as_view())
]