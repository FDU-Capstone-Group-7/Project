from django.core.mail import send_mail
from django.shortcuts import render, redirect
from datetime import date
from Indie_Game.view.reportGenerationView import generate_discussion_report
from django.conf import settings

def send_email(request, discussion_id):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect unauthenticated users to login

    # Generate the report for the specified discussion
    report = generate_discussion_report(discussion_id)
    current_date = date.today().strftime("%B %d, %Y")

    # Get the registered user's email address
    user_email = request.user.email

    # Email subject and message
    subject = f"Discussion Report - {current_date}"
    message = f"Hello {request.user.get_full_name() or request.user.username},\n\nHere is the summary report for the discussion:\n\n{report}\n\nThank you for using our service."

    # Check the arguments being passed to send_mail
    print("Sending email with subject:", subject)
    print("Message:", message)
    print("From email:", settings.DEFAULT_FROM_EMAIL)
    print("Recipient list:", [user_email])

    # Send the email to the user's registered email
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=False,
    )

    # Prepare context for the confirmation page
    context = {
        'report': report,
        'current_date': current_date,
    }
    return render(request, 'discussions/discussion_report.html', context)
