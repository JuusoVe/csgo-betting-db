terraform {
  cloud {
    organization = "juusove"

    workspaces {
      name = "cbdb-terraform-workspace"
    }
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.0.1"
    }
  }
}

provider "aws" {
  region = var.region
}

provider "tls" {

}

module "networking" {
  source          = "./modules/networking"
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets
  db_subnets      = var.db_subnets
}

module "database" {
  source                = "./modules/database"
  vpc_security_group_id = module.networking.vpc_security_group_id
  db_password           = var.db_password
  subnet_group_name     = module.networking.subnet_group_name
  depends_on = [
    module.networking
  ]
}

module "container-registry" {
  source = "./modules/container-registry"
}

module "container-service" {
  depends_on = [
    module.networking
  ]
  source                      = "./modules/container-service"
  private_subnets             = module.networking.private_subnets
  aws_alb_target_group_arn    = module.networking.aws_alb_target_group_arn
  ecs_service_security_groups = [module.networking.ecs_service_security_groups]
}