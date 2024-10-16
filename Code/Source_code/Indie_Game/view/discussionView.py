from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..model.Discussion import Game, Discussion, Comment
from ..forms import DiscussionForm, CommentForm

# List of discussions for a specific game
def game_discussions(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    discussions = game.discussions.all()
    return render(request, 'discussions/game_discussions.html', {'game': game, 'discussions': discussions})

# Create a new discussion for a game
@login_required
def create_discussion(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.author = request.user
            discussion.game = game
            discussion.save()
            return redirect('game_discussions', game_id=game.id)
    else:
        form = DiscussionForm()
    return render(request, 'discussions/create_discussion.html', {'form': form})

# View a specific discussion and its comments
def discussion_detail(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    comments = discussion.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.discussion = discussion
            comment.save()
            return redirect('discussion_detail', discussion_id=discussion.id)
    else:
        comment_form = CommentForm()
    return render(request, 'discussions/discussion_detail.html', {'discussion': discussion, 'comments': comments, 'comment_form': comment_form})

# Delete a discussion (optional, add authorization)
@login_required
def delete_discussion(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    if discussion.author == request.user:
        discussion.delete()
    return redirect('discussions/game_discussions', game_id=discussion.game.id)
