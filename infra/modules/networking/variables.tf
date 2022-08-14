variable "availability_zones" {
  description = "a comma-separated list of availability zones, defaults to all AZ of the region, if set to something other than the defaults, both private_subnets and public_subnets have to be defined as well"
  default     = ["eu-central-1a", "eu-central-1b", "eu-central-1c"]
}

variable "ecs_container_port" {
  description = "Port to the actual application"
  default     = 5000
}

variable "database_subnet_group_name" {
  default = "cbdb_database_subnet_group"
}