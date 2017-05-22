# PagerDuty pack for StackStorm
This pack enables the integration of PagerDuty into StackStorm using PagerDuty's v2 api.  It is capable of the following:

* actions
  * List all the open incidents on PD
  * Send acknowledgement of any incident(s)
  * Close and open incident(s)

## Configuration
Copy the example configuration in pagerduty.yaml.example to `/opt/stackstorm/configs/pagerduty.yaml` and edit as required.

* api_key: Version 2 API KEY
* service_api_key: API Key for a PagerDuty Service (used for creation of incidents)
* debug: optional debug flag.  Set to True for additional logging

