from gpt4all import GPT4All
from django.db import transaction
from Indie_Game.model.Discussion import Comment, Comment_temp
import logging
import re

logger = logging.getLogger(__name__)

# Initialize the GPT4All model
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")

def process_comments():
    with transaction.atomic():
        temp_comments = Comment_temp.objects.select_for_update().all()
        
        if not temp_comments.exists():
            return
        
        for comment in temp_comments:
            result = perform_operation(comment.content)
            
            try:
                    if result:
                        comment.delete()
                    else:
                        Comment.objects.create(
                            discussion=comment.discussion,
                            author=comment.author,
                            content=comment.content,
                            created_at=comment.created_at
                        )
                        logger.info(f"Created new comment: {comment.content}")
                        
                    comment.delete()
            except Exception as e:
                logger.error(f"Error processing comment {comment.id}: {e}")

def perform_operation(content):
    with model.chat_session():
        model_answer = model.generate(
            f"Is this message potentially offensive based on its words alone (without context)? Answer with one word, yes or no:\n\n{content}",
            max_tokens=50
        )
        return 'yes' in model_answer.lower() 
