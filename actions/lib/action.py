import pypd

from st2common.runners.base_action import Action

class PDAction(Action):
    def __init__(self, config):
        super(PDAction, self).__init__(config)
        self.pypd = pypd
        self.pypd.api_key = self.config['api_key']

