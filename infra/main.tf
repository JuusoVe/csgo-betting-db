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
  }
}

provider "aws" {
  region = var.region
}

module "networking" {
  source = "./modules/networking"
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