# 503 Service Unavailable Outage

## Summary
On Thursday, March 23, 2023, the main website went down, affecting 75% of the users. Users experienced 503 Service Unavailable errors. A misconfigured load balancer rule led to server overload and crash.

## Timeline
14:00 PST - Issue detected via monitoring alert indicating high response times.
14:05 PST - Initial investigation focused on backend servers, assumed a database issue.
14:20 PST - Backend team escalated to the network team after ruling out database issues.
14:35 PST - Network team investigated firewall rules and server connections.
15:00 PST - Misleading path: Considered DDoS attack, but traffic analysis ruled it out.
15:30 PST - Escalated to DevOps team to check load balancer configurations.
16:00 PST - Identified incorrect load balancer rule causing uneven traffic distribution.
16:15 PST - Applied correct load balancer rule and restarted the service.
17:00 PST - Monitoring showed gradual recovery, with decreasing error rates.
17:30 PST - Service fully restored, confirmed by monitoring and user reports.

## Root Cause and Resolution
The outage was caused by a misconfigured load balancer rule that directed too much traffic to a subset of servers, overwhelming them and causing them to crash. This rule was part of a recent deployment aimed at improving traffic distribution, but it inadvertently led to an uneven load.

### Resolution Steps:
- Identified the problematic load balancer rule after detailed traffic analysis.
- Corrected the load balancer rule to ensure even traffic distribution across all servers.
- Restarted affected servers to restore normal operations.
- Monitored the system to confirm stability and full recovery.

## Corrective and Preventative Measures
- Implement more robust testing for load balancer configuration changes.
- Enhance monitoring to include more granular traffic distribution alerts.
- Review and update deployment procedures to include an additional validation step for network configurations.
