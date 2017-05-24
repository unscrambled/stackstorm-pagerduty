# PagerDuty pack for StackStorm
This pack enables the integration of PagerDuty into StackStorm using PagerDuty's v2 api.  It is capable of the following:

* actions
  * Set PagerDuty Email **required before the Chatops Aliases will work**
  * List all the open incidents on PD
  * Send acknowledgement of any incident(s)
  * _Close and open incident(s) - Not yet Implemented_
* aliases
  * `ack {{incident id}}` - Acknowledge an incident or comma separated list of incidents
  * `set-email {{email_address}}` - Store your PagerDuty Email address in the ST2 Datastore **required for other aliases**
  * `incidents` - List open incidents

## Configuration
Copy the example configuration in pagerduty.yaml.example to `/opt/stackstorm/configs/pagerduty.yaml` and edit as required.

* api_key: Version 2 API KEY
* service_api_key: API Key for a PagerDuty Service (used for creation of incidents)
* debug: optional debug flag.  Set to True for additional logging

