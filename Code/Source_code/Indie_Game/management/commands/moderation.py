from gpt4all import GPT4All
from django.db import transaction
from Indie_Game.model.Discussion import Comment, Comment_temp 
import logging
import re

logger = logging.getLogger(__name__)

# Create model
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")

def normalize_content(content):
    # Remove extra spaces and punctuation, convert to lowercase
    return re.sub(r'\W+', '', content).lower().strip()

def process_comments():
    temp_comments = Comment_temp.objects.all()

    if not temp_comments.exists():
        return

    for comment in temp_comments:
        result = perform_operation(comment.content)

        try:
            with transaction.atomic():
                if result:
                    comment.delete()
                else:
                    # Use get_or_create to avoid duplicates
                    _, created = Comment.objects.get_or_create(
                        discussion=comment.discussion,
                        author=comment.author,
                        content=comment.content,
                        defaults={
                            'created_at': comment.created_at,
                        }
                    )

                    if created:
                        logger.info(f"Created new comment: {comment.content}")
                    else:
                        logger.info(f"Duplicate comment found: {comment.content}")

                    comment.delete()
        except Exception as e:
            logger.error(f"Error processing comment {comment.id}: {e}")

def perform_operation(content):
    with model.chat_session():
        model_answer = model.generate(f"Is this message could potentially be considered offensive based on its words alone (without context)?:\n\n{content}. Answer with an one word, yes or no", max_tokens=50)
        return 'yes' in model_answer.lower()    