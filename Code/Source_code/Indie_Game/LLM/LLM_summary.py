from gpt4all import GPT4All
import Comments_Sum
from datetime import datetime
from django.utils import timezone
# retrive all messages from the Comment table in one DF: UserID,CommentID,Comment 

########## need to provide User Input from an Interface #######
start_date = datetime(2023, 1, 1, tzinfo=timezone.utc)  # Need to be replaced by variables from the interface
end_date = datetime(2023, 12, 31, tzinfo=timezone.utc)  # Need to be replaced by variables from the interface
discussion_id = 42  # Need to be replaced by variables from the interface
################################################################

# Call the function to retrieve the comments as plain text
plain_text_comments = Comments_Sum.fetch_comments(discussion_id=discussion_id, start_date=start_date, end_date=end_date)

#1 create model
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")
#2 start session
with model.chat_session():
    # Pass the plain text directly to the prompt for summary generation
    result = model.generate(f"Make a summary. Structure your answer in specific categories listed in bullet points:\n\n{plain_text_comments}", max_tokens=500)
    # method to send the model result to the email

    
