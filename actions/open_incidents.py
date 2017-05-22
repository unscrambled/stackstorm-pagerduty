from lib.action import PDAction

class OpenIncidents(PDAction):
    def run(self):
        """List incidents with status triggered or acknowledged"""
        open_incident = {}
        open_incident_list = []
        for incident in self.pypd.Incident.find(sort_by="created_at:desc",
                                                statuses=['triggered',
                                                          'acknowledged']):
            open_incident = {'id': incident['id'], 'status': incident['status'],
                             'description': incident['description']}
            open_incident_list.append(open_incident)
        return open_incident_list
