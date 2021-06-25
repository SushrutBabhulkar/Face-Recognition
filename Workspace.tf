provider "aws"{
    region = "ap-south-1"
}

resource "aws_instance" "myin" {
    ami = "ami-011c99152163a87ae"
    instance_type = "t2.micro"
    key_name = "IntelligenceWorkspace"
    tags = {
        Name = "WorkspaceUser"
  }
}

resource "aws_ebs_volume" "ebs2" {
  availability_zone = aws_instance.myin.availability_zone
  size = 10
  tags = {
    Name = "WorkspaceVol"
  }
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdf"
  volume_id   = aws_ebs_volume.ebs2.id
  instance_id = aws_instance.myin.id
  force_detach = true
  
}


output "InstanceID"{
    value = aws_instance.myin.id
}
