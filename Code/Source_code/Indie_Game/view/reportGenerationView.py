from gpt4all import GPT4All
from django.shortcuts import get_object_or_404
from Indie_Game.model.Discussion import Discussion, Comment
import logging
from django.shortcuts import render

# Initialize the GPT4All model
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")

logger = logging.getLogger(__name__)

def generate_discussion_report(discussion_id):
    # Fetch the discussion and related comments
    discussion = get_object_or_404(Discussion, id=discussion_id)
    comments = Comment.objects.filter(discussion=discussion)
    
    # Aggregate comments into a single string
    comments_text = " ".join([comment.content for comment in comments])
    
    # Generate the report using GPT4All
    with model.chat_session():
        prompt = f"Generate a report summarizing the key points and tone of the following comments under the discussion titled '{discussion.title}':\n\n{comments_text}"
        report = model.generate(prompt, max_tokens=500)
    
    return report
