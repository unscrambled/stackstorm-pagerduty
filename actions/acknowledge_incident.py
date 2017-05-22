from lib.action import PDAction

class AcknowldgeIncident(PDAction):
    def run(self, event_keys):
        """
        Acknowledgement of an incident by key or a comma(,) separated list of keys.
        """

        if isinstance(event_keys, str):
            event_keys = [key.strip() for key in event_keys.split(',')]

        for event_key in event_keys:
            self.pypd.Incident.fetch(event_key).acknowledge
