"""kredit_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quiz import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/',views.Questions.as_view()),
    path('result/',views.Answers.as_view()),
    path('quiz/',views.Quiz.as_view()),
    path('quiz/<int:qid>',views.Quiz.as_view()),
    path('user/<int:id>',views.Users.as_view()),
    path('user/<int:id>/paymentdetails/',views.PaymentDetail.as_view()),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)