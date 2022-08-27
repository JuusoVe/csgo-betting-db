variable "vpc_security_group_id" {
  description = "ID for the VPC security group to use for connections"
  type        = string
}

variable "db_password" {
  description = "RDS root user password"
  type        = string
  sensitive   = true
}

variable "subnet_group_name" {
  description = "Name of the subnet."
  type        = string
}
