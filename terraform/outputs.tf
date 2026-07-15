output "instance_id" {
  description = "EC2 Instance ID"
  value       = aws_instance.ubuntu_workspace.id
}

output "public_ip" {
  description = "Public IP Address"
  value       = aws_instance.ubuntu_workspace.public_ip
}

output "public_dns" {
  description = "Public DNS"
  value       = aws_instance.ubuntu_workspace.public_dns
}

output "instance_state" {
  description = "Current Instance State"
  value       = aws_instance.ubuntu_workspace.instance_state
}