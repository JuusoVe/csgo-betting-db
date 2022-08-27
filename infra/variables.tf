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
  default     = "eu-central-1"
  type        = string
}

variable "private_subnets" {
  description = "List of private subnets."
  type        = set(string)
  default     = ["20.10.1.0/24", "20.10.2.0/24", "20.10.3.0/24"]
}

variable "public_subnets" {
  description = "List of public subnets."
  type        = set(string)
  default     = ["20.10.11.0/24", "20.10.12.0/24", "20.10.13.0/24"]
}

variable "db_subnets" {
  description = "List of db subnets."
  type        = set(string)
  default     = ["20.10.21.0/24", "20.10.22.0/24", "20.10.23.0/24"]
}

variable "ecs_container_port" {
  description = "ECS contariner port, needed in networking and container-service."
  type        = number
  default     = 5000
}

variable "name" {
  description = "Name of the app to use as prefix for resource-names"
  default     = "cbdb"
}