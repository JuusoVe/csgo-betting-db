resource "aws_db_parameter_group" "csgo-betting-db" {
  name   = "csgo-betting-db"
  family = "postgres13"

  parameter {
    name  = "log_connections"
    value = "1"
  }
}

resource "aws_db_instance" "csgo-betting-db" {
  identifier             = "csgo-betting-db"
  instance_class         = "db.t3.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "13.1"
  username               = "edu"
  password               = var.db_password
  db_subnet_group_name   = "csgo-betting-db"
  vpc_security_group_ids = [var.vpc_id]
  parameter_group_name   = aws_db_parameter_group.csgo-betting-db.name
  publicly_accessible    = true
  skip_final_snapshot    = true
}