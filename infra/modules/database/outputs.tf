output "rds_username" {
  description = "RDS instance root username"
  value       = aws_db_instance.csgo-betting-db.username
  sensitive   = true
}

output "rds_passwords" {
    description = "RDS instance root password"
    sensitive   = true
}

output "test_output" {
    description = "Dev time test."
    value = "thisBESTtest"
}

output "rds_connection_string" {
    descriptions = "Full connection string."
    value = "postgresql://${aws_db_instance.csgo-betting-db.username}:${var.db_password}@${aws_db_instance.csgo-betting-db.endpoint}"
}