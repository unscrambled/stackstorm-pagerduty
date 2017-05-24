from lib.action import PDAction


class AcknowldgeIncident(PDAction):
    def run(self, email, **kwargs):
        """
        Store the user's PagerDuty email in the datastore
        """
        key = '{}-pd_email'.format(kwargs['api_user'])
        return self.action_service.set_value(key, email)
