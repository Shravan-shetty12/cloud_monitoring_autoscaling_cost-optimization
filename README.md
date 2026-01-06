
# ☁️ Cloud Auto Scaling & Cost Optimization System (AWS)

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

**Objective:**  
Create EC2 instances that will later be managed by Auto Scaling and cost optimization rules.

### Actions

1. Open the **EC2 Console**
2. Launch ** EC2 instances** using default VPC and subnet
3. Choose:
   - Amazon Linux 2 AMI
   - Instance type: `t2.micro` (Free Tier eligible)

### Tag Configuration

Apply the following tags during instance creation:

| Key        | Value |
|-----------|-------|
| Environment | dev   |
| Project     | Cloud-AutoScale |
| AutoStop    | true  |

- Create **1 instances** with `Environment=dev`


### Outcome

- 4 EC2 instances running
- Instances are logically grouped using tags for automation

---

## Step 2: Create an Application Load Balancer (ALB)

**Objective:**  
Distribute incoming traffic evenly across EC2 instances.

### Actions

1. Open **EC2 → Load Balancers**
2. Create an **Application Load Balancer**
3. Select:
   - Scheme: Internet-facing
   - IP type: IPv4
4. Choose default VPC and public subnets

### Target Group

1. Create a **Target Group**
   - Target type: Instances
   - Protocol: HTTP
   - Port: 80
2. Register the EC2 instances

### Outcome

- Load balancer routes traffic
- Health checks enabled for instance monitoring

---

## Step 3: Create a Launch Template

**Objective:**  
Define how Auto Scaling should launch EC2 instances.

### Actions

1. Open **EC2 → Launch Templates**
2. Create a new launch template
3. Configure:
   - AMI: Amazon Linux 2
   - Instance type: `t2.micro`
   - Security Group: allow HTTP (80)

### Tagging

Add the same tags used earlier:
- Environment
- Project
- AutoStop

### Outcome

- Standardized configuration for all scaled instances

---

## Step 4: Configure Auto Scaling Group (ASG)

**Objective:**  
Automatically scale EC2 instances based on workload.

### Actions

1. Open **Auto Scaling Groups**
2. Create a new ASG using the launch template
3. Configure capacity:
   - Minimum: 1
   - Desired: 2
   - Maximum: 3

### Scaling Policy

- Policy type: **Target Tracking**
- Metric: Average CPU Utilization
- Target value: 60%

### Attach Load Balancer

- Attach the ALB target group

### Outcome

- Instances scale automatically based on demand
- High availability ensured

---

## Step 5: Monitor Resources Using CloudWatch

**Objective:**  
Observe system health and scaling behavior.

### Actions

1. Open **CloudWatch → Metrics**
2. Monitor:
   CPUUtilization
 

### Alarms

Create alarms for:
- High CPU usage (>70%)
- Low CPU usage (<20%)

### Outcome

- Real-time visibility into infrastructure behavior

---

## Step 6: Enable Cost Visibility Using Tags

**Objective:**  
Track costs by project and environment.

### Actions

1. Open **AWS Billing → Cost Allocation Tags**
2. Activate:
   - Environment
   - Project
3. Wait up to 24 hours for data to reflect

### Outcome

- Cost breakdown available in Cost Explorer

---

## Step 7: Create AWS Budget (Cost Guardrail)

**Objective:**  
Prevent unexpected cloud spending.

### Actions

1. Open **AWS Budgets**
2. Create a **Cost Budget**
3. Set:
   - Monthly EC2 threshold
   - Alert at 70% and 90%
4. Configure email notifications

### Outcome

- Proactive cost alerts
- No surprise billing

---

## Step 8: Schedule EC2 Start/Stop for Cost Optimization

**Objective:**  
Reduce costs by stopping non-production instances during off-hours.

### Actions

1. Open **Amazon EventBridge**
2. Create a scheduled rule:
   - Stop rule (night)
   - Start rule (morning)

### Systems Manager Automation

Use AWS-managed documents:
- `AWS-StopEC2Instance`
- `AWS-StartEC2Instance`

### Targeting

- Filter instances using tag:

## Conclusion


This project demonstrates a complete, real-world AWS cloud management system that balances:

- Performance

- Availability

- Cost efficiency

- Operational safety

It reflects how modern cloud platforms are operated in production environments, following best practices used by enterprises and cloud service providers.