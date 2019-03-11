provider "aws" {
  region     = "us-west-2"
}


resource "aws_instance" "interview" {
  ami           = "ami-0bbe6b35405ecebdb"
  instance_type = "t2.medium"
  key_name      = "interview"

  
}

resource "aws_security_group" "allow_all" {
  name        = "allow_all"
  description = "Allow all inbound traffic"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags {
    Name = "allow_all"
  }
}
