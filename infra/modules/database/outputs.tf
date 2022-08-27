output "test_output" {
  description = "Dev time test."
  value       = "thisBESTtest"
}

output "rds_connection_string" {
  description = "Full connection string."
  value       = "postgresql://${aws_db_instance.csgo-betting-db.username}:${var.db_password}@${aws_db_instance.csgo-betting-db.endpoint}"
}