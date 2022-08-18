variable "ecs_container_port" {
  description = "Port the"
  default     = 80
}

variable "private_subnets" {
  description = "List of subnet IDs"
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