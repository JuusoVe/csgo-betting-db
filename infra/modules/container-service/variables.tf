variable "ecs_container_port" {
  description = "Port to the container."
}

variable "private_subnets" {
  description = "List of private subnets"
}

variable "aws_alb_target_group_arn" {
  description = "Identifier for the loadbalancer target group."
}

variable "ecs_service_security_groups" {
  description = "Security groups for the ECS service."
}

variable "api_container_name" {
  description = "API container name"
  default     = "cbdb-api-container"
}