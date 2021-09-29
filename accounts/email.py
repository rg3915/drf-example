from djoser import email


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'accounts/email/password_reset.html'
