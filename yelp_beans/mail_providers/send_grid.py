# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from jinja2 import Environment
from jinja2 import PackageLoader
from sendgrid import SendGridAPIClient
from sendgrid.helpers import mail
from sendgrid.helpers.mail import Content

from yelp_beans.mail_providers.mail_provider import MailProvider


class SendGrid(MailProvider):
    """ Send an email using the SendGrid API
        Args:
            - email :string => the user's work email (ie username@company.com)
            - subject :string => the subject line for the email
            - template :string => the template file, corresponding to the email sent.
            - template_arguments :dictionary => keyword arguments to specify to render_template
        Returns:
            - SendGrid response
    """

    config = [
        'SENDGRID_SENDER',
        'SENDGRID_API_KEY'
    ]

    def create_client(self):
        self.client = SendGridAPIClient(apikey=self.SENDGRID_API_KEY).client

    def send_mail(self, email, subject, template, template_arguments):
        env = Environment(loader=PackageLoader('yelp_beans', 'templates/email_templates'))
        template = env.get_template(template)
        rendered_template = template.render(template_arguments)

        message = mail.Mail(
            from_email=mail.Email(self.SENDGRID_SENDER),
            subject=subject,
            to_email=mail.Email(email),
            content=Content("text/html", rendered_template)
        )

        return self.client.mail.send.post(request_body=message.get())
