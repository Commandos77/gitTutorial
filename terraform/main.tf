provider "aws"{
  region = "us-west-1"
  
}

# DATA BLOCKS
data "http" "myip" {
  url = "http://ipv4.icanhazip.com"
}
data "aws_ami" "ubuntu" {

    most_recent = true

    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
    }

    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }

    owners = ["099720109477"]
}
data "template_file" "userdata" {
  template = file("scripts/cloud-init.yml")
  vars = {
    vpc_id = aws_vpc.my-vpc.id
  }
}

# RESOURSES BLOCKS
# INFRA BLOCKS
resource "aws_vpc" "my-vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = var.enabled
  enable_dns_hostnames = var.enabled
}
resource "aws_subnet" "my-subnet" {
  vpc_id                  = aws_vpc.my-vpc.id
  cidr_block              = var.subnet_cidr
  availability_zone       = "us-west-1a"
  map_public_ip_on_launch = var.enabled
  tags = {
    Name = "terraform"
  }
}
resource "aws_internet_gateway" "my-igw" {
  vpc_id = aws_vpc.my-vpc.id
  tags = {
    Name = "terraform"
  }
}
resource "aws_route_table" "my-rt" {
  vpc_id = aws_vpc.my-vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my-igw.id
  }
  tags = {
    Name = "terraform"
  }
}
resource "aws_route_table_association" "my-rt-assoc" {
  subnet_id      = aws_subnet.my-subnet.id
  route_table_id = aws_route_table.my-rt.id
}

# SERVER BLOCKS
resource "aws_instance" "my-server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.small"
  vpc_security_group_ids = [aws_security_group.my-server-sg.id]
  subnet_id              = aws_subnet.my-subnet.id
  secondary_private_ips  = var.secondary_ips
  key_name               = aws_key_pair.Valdis_2.key_name
  user_data              = data.template_file.userdata.rendered
  tags = {
    Name = "terraform"
  }
}
resource "aws_security_group" "my-server-sg" {
  name        = "server access"
  description = "Allow server acces with SSH and HTTP"
  vpc_id      = aws_vpc.my-vpc.id
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["${chomp(data.http.myip.response_body)}/32"]
  }
  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "terraform"
  }
}
resource "aws_key_pair" "Valdis_2" {
  key_name   = "Valdis_2"
  public_key = file("/Valdis.pub")
}
