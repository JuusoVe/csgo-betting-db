terraform {
  cloud {
    organization = "juusove"

    workspaces {
      name = "cbdb-terraform-workspace"
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
  source = "./modules/database"
  vpc_id = module.networking.vpc_id
  db_password = var.db_password
  depends_on = [
    module.networking
  ]
}