output "vpc_security_group_id" {
  description = "VPC id"
  value       = aws_security_group.rds.id
}

output "subnet_group_name" {
  description = "Subnet group name"
  value       = aws_db_subnet_group.csgo-betting-db.name
}