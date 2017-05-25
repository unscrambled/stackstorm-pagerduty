from lib.action import PDAction


class OpenIncidents(PDAction):
    def run(self, statuses, maximum, sort_by):
        """List incidents with status triggered or acknowledged"""
        status = False
        results = {'incidents': []}

        try:
            if isinstance(statuses, basestring):
                statuses = [s.strip() for s in statuses.split(',')]
            results['incidents'] = self.pypd.Incident.find(
                sort_by=sort_by, statuses=statuses, maximum=maximum)
            status = True
        except Exception as e:
            results['error'] = {'type': type(e).__name__, 'message': e.message}

        return (status, results)
