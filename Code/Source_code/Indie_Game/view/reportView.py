# reportGenerationView.py
from django.shortcuts import render
from Indie_Game.view.reportGenerationView import generate_discussion_report

def discussion_report_view(request, discussion_id):
    # Call generate_discussion_report with only the discussion_id argument
    report = generate_discussion_report(discussion_id)
    return render(request, 'discussions/discussion_report.html', {'report': report})

