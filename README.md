
# ☁️ Cloud Monitoring Auto Scaling & Cost Optimization System (AWS)

This project implements a cloud-native, automated infrastructure management system on AWS that continuously monitors resource usage, automatically scales compute capacity based on demand, and optimizes cloud costs by eliminating idle and underutilized resources — without manual intervention.

The solution is designed using AWS-managed services and follows real-world cloud engineering and FinOps best practices, focusing on availability, scalability, and cost governance.

 
## 🎯 Problem Statement

Manual cloud resource management often leads to:

 - Over-provisioning of compute resources

 - Under-utilized instances running continuously

 - Unexpected cost spikes due to auto scaling without financial guardrails

Goal:
Build a system that can:

 - Monitor resource usage in real time

 - React automatically to workload changes

 - Control cloud costs using intelligent, safe optimization strategies

## 📜 Step-by-Step Guide

## Step 1: Launch EC2 Instances (Base Infrastructure)

 - EC2 instances are launched using Amazon Linux 2.
 - Instances are kept lightweight (t2.micro) to control cost.
 - Tags such as Environment, Project, and AutoStop are added.

## Step 2: Create an Application Load Balancer (ALB)

 - ALB routes incoming requests to healthy EC2 instances.
 - Health checks continuously monitor instance availability.
 - Unhealthy instances are automatically removed from traffic.

## Step 3: Create a Launch Template

 - AMI, instance type, security groups, and tags are standardized.
 - Any new EC2 instance launched by Auto Scaling follows this template.

## Step 4: Configure Auto Scaling Group (ASG)

 - ASG maintains a minimum number of running instances.
 - Scales out when CPU usage increases.
 - Scales in when demand drops.

## Step 5: Monitor Resources Using CloudWatch

 - CloudWatch collects metrics such as CPU utilization.
 - Alarms trigger when thresholds are crossed.
 - Enables proactive monitoring
 - Supports automated scaling decisions

## Step 6: Enable Cost Visibility Using Tags

 - Cost allocation tags are activated in the Billing console.
 - Costs are grouped by environment and project.
 - Clear cost breakdown in AWS Cost Explorer
 - Helps identify expensive or wasteful resources

## Step 7: Create AWS Budget (Cost Guardrail)

 - Monthly budget is defined for EC2 usage.
 - Alerts are sent when spending reaches set limits.
 - Acts as a financial safety net
 - Encourages cost-aware cloud usage

## Step 8: Schedule EC2 Start/Stop for Cost Optimization

 - EventBridge schedules run automatically.
 - Systems Manager Automation stops or starts EC2 instances based on tags.
 - Scheduled start and stop automation eliminates unnecessary runtime costs.

![Cloud main architecture  (2)](https://github.com/user-attachments/assets/a16fadaf-ea49-4f6d-8f68-d54588526a58)



## Conclusion


This project demonstrates a complete, real-world AWS cloud management system that balances:

- Performance

- Availability

- Cost efficiency

- Operational safety

It reflects how modern cloud platforms are operated in production environments, following best practices used by enterprises and cloud service providers.
