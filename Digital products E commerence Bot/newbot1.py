import imaplib
import email

def email_check(nm):
    try:
        imap_server = 'imap.gmail.com'
        username = 'Markfelix1495@gmail.com'
        password = 'jbwhrtxxqovnmzrp'

        # Connect to the Gmail IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)

        # Login to the Gmail account
        mail.login(username, password)

        # Select the mailbox you want to search emails in (e.g., 'INBOX')
        mailbox = 'INBOX'
        mail.select(mailbox)

        # Search for emails containing specific keywords in the body
        search_criteria = '(BODY "{}")'.format(nm)
        status, data = mail.search(None, search_criteria)

        # Get the list of matching email IDs
        email_ids = data[0].split()
        if email_ids:
            # Fetch the most recent email from the search results
            latest_email_id = email_ids[-1]
            status, data = mail.fetch(latest_email_id, '(RFC822)')
            raw_email = data[0][1]

            # Parse the raw email
            email_message = email.message_from_bytes(raw_email)

            # Print the email body
            if email_message.is_multipart():
                for part in email_message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        a=part.get_payload(decode=True).decode('utf-8')
            else:
                a=email_message.get_payload(decode=True).decode('utf-8')

        # Close the connection
        mail.logout()
        return a
    except:
        return None
c=3366242675
b=email_check(c)
print(b)
