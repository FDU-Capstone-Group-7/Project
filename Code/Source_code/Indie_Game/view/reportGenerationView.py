from gpt4all import GPT4All
import logging

# Initialize the GPT4All model
model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")

logger = logging.getLogger(__name__)

def generate_discussion_report(discussion_title, filtered_comments):
    """
    Generate a report summarizing the key points and tone of comments under a discussion.

    Args:
        discussion_title (str): Title of the discussion.
        filtered_comments (QuerySet): QuerySet of comments to include in the report.

    Returns:
        str: The generated report as a string.
    """
    # Aggregate comments into a single string
    comments_text = " ".join([comment.content for comment in filtered_comments])

    if not comments_text.strip():
        logger.warning(f"No comments available to generate the report for '{discussion_title}'")
        return f"No comments available for the discussion titled '{discussion_title}'."

    # Generate the report using GPT4All
    try:
        with model.chat_session():
            prompt = (
                f"Generate a report summarizing the key points and tone of the following comments "
                f"under the discussion titled '{discussion_title}':\n\n{comments_text}"
            )
            report = model.generate(prompt, max_tokens=500)
            logger.info(f"Report successfully generated for discussion '{discussion_title}'")
            return report
    except Exception as e:
        logger.error(f"Error generating report for discussion '{discussion_title}': {e}")
        return f"An error occurred while generating the report for '{discussion_title}'."
