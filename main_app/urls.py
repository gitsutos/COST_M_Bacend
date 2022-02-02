from django.urls import path

from .views import LatestCosts, add_costs

urlpatterns = [
    path("latest-costs/", LatestCosts.as_view()),
    path("add_costs/", add_costs,),
]
