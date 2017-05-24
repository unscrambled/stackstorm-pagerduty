from lib.action import PDAction


class OpenIncidents(PDAction):
    def run(self, statuses, limit, sort_by):
        """List incidents with status triggered or acknowledged"""
        status = False
        results = {'incidents': []}

        try:
            results['incidents'] = self.pypd.Incident.find(
                sort_by=sort_by, statuses=statuses, limit=limit)
            status = True
        except Exception as e:
            results['error'] = {'type': type(e).__name__, 'message': e.message}

        return (status, results)
