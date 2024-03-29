# resource "aws_db_parameter_group" "csgo-betting-db" {
#   name   = "csgo-betting-db"
#   family = "postgres13"

#   parameter {
#     name  = "log_connections"
#     value = "1"
#   }
# }

resource "aws_db_instance" "csgo-betting-db" {
  identifier             = "csgo-betting-db"
  instance_class         = "db.t3.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "14.2"
  username               = "postgres"
  password               = var.db_password
  db_subnet_group_name   = var.subnet_group_name
  vpc_security_group_ids = [var.vpc_security_group_id]
  publicly_accessible    = true
  skip_final_snapshot    = true
  availability_zone      = "eu-central-1a"
}