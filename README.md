**# cloud-autoscaling-cost-optimizer
**
**Problem statement:**
Manual cloud resource management leads to over-provisioning,
under-utilization, and unnecessary cost.

This project builds a fully automated AWS-based system that:
- Monitors EC2 resource usage
- Automatically scales infrastructure
- Identifies low-utilization waste
- Improves availability while reducing cost

The system follows an Event-Driven Architecture using native AWS services.

**Technologies Used**
- AWS EC2
- Auto Scaling Groups (ASG)
- CloudWatch Metrics & Alarms
- Target Tracking Scaling Policies
- IAM
- Event-driven monitoring

**Key Features**
✔ Real-time resource monitoring  
✔ Automatic scale-up on high load  
✔ Safe scale-down with cooldown protection  
✔ Cost-aware scaling decisions  
✔ No manual intervention required  

**How Scaling Works**
- Scale-Up: Triggered when average CPU > threshold
- Scale-Down: Triggered conservatively after cooldown
- Minimum capacity ensures availability



