variable "AWS_SECRET_ACCESS_KEY" {
  description = "AWS secret key"
  type        = string
  sensitive   = true
}

variable "AWS_ACCESS_KEY_ID" {
  description = "AWS access key ID"
  type        = string
  sensitive   = true
}


variable "db_password" {
  description = "RDS root user password"
  type        = string
  sensitive   = true
}

variable "region" {
  description = "AWS region to use"
  default = "eu-central-1"
  type        = string
  sensitive   = false
}