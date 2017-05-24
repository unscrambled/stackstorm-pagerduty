from lib.action import PDAction


class AcknowldgeIncident(PDAction):
    def run(self, email, **kwargs):
        """
        Store the user's PagerDuty email in the datastore
        """
        api_user = kwargs['api_user']
        if api_user is not None:
            key = '{}-pd_email'.format(api_user)
            return self.action_service.set_value(key, email)
        return (False, 'This action can only be run via Chatops')
