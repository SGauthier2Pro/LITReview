"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
from authentication.forms import UserLoginForm
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        authentication_form=UserLoginForm,
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', review.views.home, name='home'),
    path('flux/', review.views.home, name='flux'),
    path('posts/', review.views.own_posts, name='own_posts'),
    path('abonnements/', review.views.follow_user, name='abonnements'),
    path('abonnements/<int:following_id>/delete', review.views.unfollow_user,
         name='unfollow_user'),
    path('ticket/create/', review.views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/edit', review.views.edit_ticket,
         name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete', review.views.delete_ticket,
         name='delete_ticket'),
    path('ticket/<int:ticket_id>/create_review',
         review.views.create_review_from_ticket,
         name='create_review_from_ticket'),
    path('review/create/', review.views.create_ticket_review,
         name='create_ticket_review'),
    path('review/<int:review_id>/edit', review.views.edit_review,
         name='edit_review'),
    path('review/<int:review_id>/delete', review.views.delete_review,
         name='delete_review'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
