from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from . import forms, models


@login_required
def home(request):
    followed_users = []
    followings = models.UserFollows.objects.filter(user=request.user)
    for following in followings:
        followed_users.append(following.followed_user)

    tickets = models.Ticket.objects.filter(
        Q(user__in=followed_users) |
        Q(user=request.user)
    )
    tickets_reviewed = models.Ticket.objects.exclude(review=None)
    reviews = models.Review.objects.filter(
        Q(user__in=followed_users) |
        Q(user=request.user) |
        Q(ticket__in=tickets)
    )

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'review/home.html', context={'posts': posts,
                                                        'tickets_reviewed': tickets_reviewed
                                                        }
                  )


@login_required
def own_posts(request):
    tickets = models.Ticket.objects.filter(user=request.user)
    reviews = models.Review.objects.filter(user=request.user)

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    return render(request, 'review/own_posts.html', context={'posts': posts})


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'review/create_ticket.html', context={'form': form})


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'review/view_ticket.html', {'ticket': ticket})


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        edit_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    context = {
        'ticket': ticket,
        'edit_form': edit_form,
    }
    return render(request, 'review/edit_ticket.html', context=context)


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        delete_form = forms.DeleteTicketForm(request.POST)
        if delete_form.is_valid():
            ticket.delete()
            return redirect('home')
    context = {
        'ticket': ticket,
        'delete_form': delete_form,
    }
    return render(request, 'review/delete_ticket.html', context=context)


@login_required
def create_ticket_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'review/create_review_post.html', context=context)


@login_required
def create_review_from_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'review/create_review_from_ticket.html', context=context)


@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'review/view_review.html', {'review': review})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    if request.method == 'POST':
        edit_form = forms.ReviewForm(request.POST, instance=review)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    context = {
        'review': review,
        'edit_form': edit_form,
    }
    return render(request, 'review/edit_review.html', context=context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        delete_form = forms.DeleteReviewForm(request.POST)
        if delete_form.is_valid():
            review.delete()
            return redirect('home')
    context = {
        'review': review,
        'delete_form': delete_form,
    }
    return render(request, 'review/delete_review.html', context=context)


@login_required
def follow_user(request):
    followings = models.UserFollows.objects.filter(user=request.user)
    followed_by = models.UserFollows.objects.filter(followed_user=request.user)
    follow_form = forms.FollowForm()
    message = ''
    if request.method == 'POST':
        follow_form = forms.FollowForm(request.POST)
        try:
            followed_user = User.objects.get(username=request.POST['followed_username'])
        except User.DoesNotExist:
            followed_user = None

        if followed_user and follow_form.is_valid():
            models.UserFollows.objects.create(user=request.user, followed_user=followed_user)
            return redirect('abonnements')
        else:
            message = "l'utilisateur saisie n'existe pas !"
    context = {
        'follow_form': follow_form,
        'followings': followings,
        'followed_by': followed_by,
        'message': message,
    }
    return render(request, 'review/follows.html', context=context)


@login_required
def unfollow_user(request, following_id):
    following = get_object_or_404(models.UserFollows, id=following_id)
    delete_form = forms.UnfollowForm()
    if request.method == 'POST':
        delete_form = forms.UnfollowForm(request.POST)
        if delete_form.is_valid():
            following.delete()
            return redirect('abonnements')
    context = {
        'following': following,
        'delete_form': delete_form,
    }
    return render(request, 'review/delete_user_following.html', context=context)

