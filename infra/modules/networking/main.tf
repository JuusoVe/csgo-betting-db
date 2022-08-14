data "aws_availability_zones" "available" {}

# SHARED FOR PRIVATE AND PUBLIC
module "vpc" {
  source               = "terraform-aws-modules/vpc/aws"
  version              = "2.77.0"
  name                 = "csgo-betting-db"
  cidr                 = "10.0.0.0/16"
  azs                  = var.availability_zones
  public_subnets       = var.public_subnets
  private_subnets      = var.private_subnets
  enable_dns_hostnames = true
  enable_dns_support   = true
  enable_nat_gateway = true
  single_nat_gateway = true
  one_nat_gateway_per_az = false
}

resource "aws_internet_gateway" "main" {
  vpc_id = module.vpc.vpc_id
}

# PUBLIC
resource "aws_subnet" "public" {
  vpc_id                  = module.vpc.vpc_id
  cidr_block              = element(var.public_subnets, count.index)
  availability_zone       = element(var.availability_zones, count.index)
  count                   = length(var.public_subnets)
  map_public_ip_on_launch = true
}

resource "aws_db_subnet_group" "csgo-betting-db" {
  name       = "csgo-betting-db"
  subnet_ids = var.private_subnets
  tags = {
    Name = "csgo-betting-db"
  }
}

resource "aws_route_table" "public" {
  vpc_id = module.vpc.vpc_id
}

resource "aws_route" "public" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.main.id
}
 
resource "aws_route_table_association" "public" {
  count          = length(var.public_subnets)
  subnet_id      = element(aws_subnet.public.*.id, count.index)
  route_table_id = aws_route_table.public.id
}

# PRIVATE
resource "aws_subnet" "private" {
  vpc_id            = module.vpc.vpc_id
  cidr_block        = element(var.private_subnets, count.index)
  availability_zone = element(var.availability_zones, count.index)
  count             = length(var.private_subnets)
}

resource "aws_nat_gateway" "main" {
  count         = length(var.private_subnets)
  allocation_id = element(aws_eip.nat.*.id, count.index)
  subnet_id     = element(aws_subnet.public.*.id, count.index)
  depends_on    = [aws_internet_gateway.main]
}
 
resource "aws_eip" "nat" {
  count = length(var.private_subnets)
  vpc = true
}

resource "aws_route_table" "private" {
  count  = length(var.private_subnets)
  vpc_id = module.vpc.vpc_id
}
 
resource "aws_route" "private" {
  count                  = length(compact(var.private_subnets))
  route_table_id         = element(aws_route_table.private.*.id, count.index)
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = element(aws_nat_gateway.main.*.id, count.index)
}
 
resource "aws_route_table_association" "private" {
  count          = length(var.private_subnets)
  subnet_id      = element(aws_subnet.private.*.id, count.index)
  route_table_id = element(aws_route_table.private.*.id, count.index)
}

# SECURITY GROUPS
resource "aws_security_group" "rds" {
  name   = "csgo-betting-db-rds"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "csgo-bettingdb-rds"
  }
}

resource "aws_security_group" "https-access-security-group" {
  name   = "https-access-security-group"
  vpc_id = module.vpc.vpc_id
 
  ingress {
   protocol         = "tcp"
   from_port        = 80
   to_port          = 80
   cidr_blocks      = ["0.0.0.0/0"]
   ipv6_cidr_blocks = ["::/0"]
  }
 
  ingress {
   protocol         = "tcp"
   from_port        = 443
   to_port          = 443
   cidr_blocks      = ["0.0.0.0/0"]
   ipv6_cidr_blocks = ["::/0"]
  }
 
  egress {
   protocol         = "-1"
   from_port        = 0
   to_port          = 0
   cidr_blocks      = ["0.0.0.0/0"]
   ipv6_cidr_blocks = ["::/0"]
  }
}

resource "aws_security_group" "ecs_tasks" {
  name   = "tasks-access-security-group"
  vpc_id = module.vpc.vpc_id
 
  ingress {
   protocol         = "tcp"
   from_port        = var.ecs_container_port
   to_port          = var.ecs_container_port
   cidr_blocks      = ["0.0.0.0/0"]
   ipv6_cidr_blocks = ["::/0"]
  }
 
  egress {
   protocol         = "-1"
   from_port        = 0
   to_port          = 0
   cidr_blocks      = ["0.0.0.0/0"]
   ipv6_cidr_blocks = ["::/0"]
  }
}

