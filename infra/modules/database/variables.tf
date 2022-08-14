variable "vpc_id" {
  description = "ID for the VPC to use for connections"
  type        = string
}

variable "db_password" {
  description = "RDS root user password"
  type        = string
  sensitive   = true
}
