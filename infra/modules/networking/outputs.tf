output "vpc_security_group_id" {
  description = "VPC sg id"
  value       = aws_security_group.rds.id
}

output "subnet_group_name" {
  description = "Subnet group name."
  value       = var.database_subnet_group_name
}

output "aws_alb_target_group_arn" {
  description = "Identifier of the loadbalancer target group."
  value       = aws_alb_target_group.cbdb-target-group.arn
}

output "ecs_service_security_groups" {
  description = "Security group name for the ECS service"
  value       = aws_security_group.ecs_tasks.id
}