provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "misconfigured_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = false
  enable_dns_hostnames = false
}

resource "aws_security_group" "misconfigured_sg" {
  name        = "misconfigured_sg"
  description = "Allow all traffic"
  vpc_id      = aws_vpc.misconfigured_vpc.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
