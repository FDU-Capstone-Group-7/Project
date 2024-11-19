from django.shortcuts import render, get_object_or_404
from django.db.models.functions import TruncDate
from django.utils.dateparse import parse_date
from ..model.Discussion import Discussion, Comment
from ..view.reportGenerationView import generate_discussion_report

def discussion_report_view(request, discussion_id):
    # Get the discussion object
    discussion = get_object_or_404(Discussion, id=discussion_id)

    # Retrieve selected dates from GET request
    selected_dates = request.GET.getlist('selected_dates')
    selected_dates = [parse_date(date) for date in selected_dates if parse_date(date)]
      # Extract selected dates from GET parameters
    print(f"Selected Dates: {selected_dates}")  # Debugging: Print selected dates in the console

    # Filter comments based on selected dates
    filtered_comments = discussion.comments.all()
    if selected_dates:
        # Parse dates and filter comments
        try:
            selected_dates = [parse_date(date) for date in selected_dates if parse_date(date)]
            print(f"Parsed Dates: {selected_dates}")  # Debugging: Print parsed dates in the console
            filtered_comments = Comment.objects.filter(
                discussion=discussion,
                created_at__date__in=selected_dates
            )
        except Exception as e:
            print(f"Error parsing dates: {e}")

    # Generate the report
    report = generate_discussion_report(discussion.title, filtered_comments)

    return render(request, 'discussions/report_page.html', {
        'discussion': discussion,
        'report': report,
        'filtered_comments': filtered_comments,
        'selected_dates': selected_dates,
    })



