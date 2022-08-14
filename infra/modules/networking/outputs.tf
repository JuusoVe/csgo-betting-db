output "vpc_security_group_id" {
  description = "VPC id"
  value       = aws_security_group.rds.id
}

output "subnet_group_name" {
  description = "Subnet group name"
  value       = var.database_subnet_group_name
}