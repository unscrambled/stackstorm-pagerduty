from lib.action import PDAction

class AcknowldgeIncident(PDAction):
    def run(self, event_keys, **kwargs):
        """
        Acknowledgement of an incident by key or a comma(,) separated list of keys.
        """
        status = False
        results = {"acknowleged": {}}
        email = None

        try:
            if 'api_user' in kwargs:
                user = kwargs['api_user']
                if user:
                    # get email from datastore
                    key = '{}-pd_email'.format(kwargs['api_user'])
                    email = self.action_service.get_value(key)
                    if email:
                        self.logger.info(
                            "Found email for {} in datastore".format(kwargs['api_user']))

            if email == None and 'from_email' in kwargs:
                email = kwargs['from_email']
                if email:
                    self.logger.info("Found from_email in passed arguments")

            if email == None:
                self.logger.error("Could not find email from api_user {} nor
                                  from_email".format(kwargs['api_user']))
                return (False, "I don't know who you are")

            if isinstance(event_keys, str):
                for event_key in [key.strip() for key in event_keys.split(',')]:
                    incident = self.pypd.Incident.fetch(event_key).acknowledge(email)
                    results['acknowledged'][incident.id] = incident.json

        except Exception as e:
            results['error'] = e.message

        return (status, results)

