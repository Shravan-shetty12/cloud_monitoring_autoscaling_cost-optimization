## Cost Monitoring Implementation

AWS Cost Explorer was enabled to analyze EC2 compute costs.

AWS Budgets provide financial guardrails and alert when
spending approaches defined thresholds.

Note:
Cost Explorer data is not real-time and can take 12–48 hours to appear.
During initial testing, EC2 costs may appear as $0.00 due to billing delay.

This project accounts for this behavior by using scheduled cost analysis
instead of real-time cost-based scaling.






