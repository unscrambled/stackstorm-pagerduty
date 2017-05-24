class UnknownUser(Exception):
    default_message = ("I don't know your PagerDuty email address."
                       "Please identify yourself with "
                       "`! pagerduty email <email_address>` first.")

    def __init__(self, message, *args):
        self.message = message or self.defaul_message
        super(UnknownUser, self).__init__(message, *args)
