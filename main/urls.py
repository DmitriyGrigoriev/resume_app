from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('resume/', views.IndexView.as_view(), name="home"),
	path('resume/contact/', views.ContactView.as_view(), name="contact"),
	path('resume/portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('resume/portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('resume/blog/', views.BlogView.as_view(), name="blogs"),
	path('resume/blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	]