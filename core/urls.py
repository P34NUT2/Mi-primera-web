from django.urls import path
from .views import HomePageView, SamplePageView, HowItWorksView, FAQView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('how-it-works/', HowItWorksView.as_view(), name='how_it_works'),
    path('faq/', FAQView.as_view(), name='faq'),
] 