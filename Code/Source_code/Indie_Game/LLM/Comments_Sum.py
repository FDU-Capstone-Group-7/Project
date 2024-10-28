from datetime import datetime
from django.utils import timezone
from Indie_Game.model.Discussion import Comment

def fetch_comments(discussion_id=None, start_date=None, end_date=None):
    # Create a base query
    query = Comment.objects.all()

    # Filter by discussion_id if provided
    if discussion_id:
        query = query.filter(discussion_id=discussion_id)
    
    # Filter by date range if provided
    if start_date:
        query = query.filter(created_at__gte=start_date)
    if end_date:
        query = query.filter(created_at__lte=end_date)
    
    # Retrieve only specific fields
    comments = query.values('id', 'content', 'author_id')

    # Convert the queryset into plain text format
    plain_text = ""
    for comment in comments:
        line = f"ID: {comment['id']}, Content: {comment['content']}, Author ID: {comment['author_id']}\n"
        plain_text += line
    
    return plain_text
