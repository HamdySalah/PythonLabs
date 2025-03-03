import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def compose_email(to_email, receiver_name, subject, message_body, sender_name="Your Name"):
    message = MIMEMultipart()
    message['From'] = sender_name
    message['To'] = to_email
    message['Subject'] = subject

    email_body = f"""
    Dear {receiver_name},

    {message_body}

    Best regards,
    {sender_name}
    """
    message.attach(MIMEText(email_body, 'plain'))

    # Save email content to a file
    file_name = f"email_to_{to_email.replace('@', '_').replace('.', '_')}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"From: {sender_name}\n")
        file.write(f"To: {to_email}\n")
        file.write(f"Subject: {subject}\n\n")
        file.write(email_body)

    print(f"Email saved to {file_name}")


# Example usage
compose_email(
    to_email="recipient@example.com",
    receiver_name="John Doe",
    subject="Meeting Reminder",
    message_body="Just a reminder about our meeting tomorrow at 10 AM."
)
