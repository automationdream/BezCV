from django.urls import path

from . import views

urlpatterns = [
  path('candidate/add', views.CandidateAddView.as_view()),
  path('candidate/filters', views.FiltersView.as_view()),
  path('oferty', views.OffersView.as_view()),
  path('oferty/search', views.SearchCandidateView.as_view()),
  path('oferty/purchase', views.PurchaseOfferView.as_view()),
  path('oferty/<slug>-<pk>', views.CandidateView.as_view()),
  path('profile/candidates', views.PurchasedOffersListView.as_view()),
]