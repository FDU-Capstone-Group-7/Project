from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
from datetime import date
from django.shortcuts import render


def send_email(request, discussion_id):
    if request.method == 'POST':
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect unauthenticated users to login

        current_date = date.today().strftime("%B %d, %Y")

        # Get the report content from the POST data
        report = request.POST.get('report_content')

        if not report:  # If no report content is provided
            return redirect('discussion_report', discussion_id=discussion_id)

        # Get the registered user's email address
        user_email = request.user.email

        # Email subject and message
        subject = f"Discussion Report - {current_date}"
        message = f"Hello {request.user.get_full_name() or request.user.username},\n\nHere is the summary report for the discussion:\n\n{report}\n\nThank you for using our service."

        # Send the email to the user's registered email
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=False,
        )

        # Redirect to a success confirmation page
        return render(request, 'discussions/email_success.html', {'discussion_id': discussion_id})

    # If not POST, redirect to the discussion report page
    return redirect('discussion_report', discussion_id=discussion_id)

