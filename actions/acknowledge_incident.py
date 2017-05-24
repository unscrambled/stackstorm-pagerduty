from lib.action import PDAction
from lib.error import UnknownUser


class AcknowldgeIncident(PDAction):
    def run(self, event_keys, **kwargs):
        """
        Acknowledgement of an incident by key
        or a comma(,) separated list of keys.
        """
        status = False
        results = {"acknowledged": {}}
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
                            "Found email {} for {} in datastore"
                            .format(email, kwargs['api_user']))

            if email is None and 'from_email' in kwargs:
                email = kwargs['from_email']
                if email:
                    self.logger.info("Found from_email in passed arguments")

            if email is None:
                self.logger.error(
                    "Could not find email from api_user {} nor from_email"
                    .format(kwargs['api_user']))
                raise UnknownUser()

            if isinstance(event_keys, basestring):
                acknowledged = results['acknowledged']
                for ek in [k.strip() for k in event_keys.split(',')]:
                    self.logger.debug(
                        'Acknowledging incident {}'.format(ek))
                    res = self.pypd.Incident.fetch(ek).acknowledge(email)
                    self.logger.debug("Result: ", res)
                    acknowledged[res['incident']['id']] = res['incident']
                status = True
            else:
                raise ValueError('Invalid event key(s)')

        except Exception as e:
            results['error'] = {'type': type(e).__name__, 'message': e.message}

        return (status, results)
