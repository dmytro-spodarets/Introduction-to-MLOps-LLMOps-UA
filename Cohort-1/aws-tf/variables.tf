variable "name_server_lr_model" {
  description = ""
  type = string
  default = "lr_model_api"
}

variable "aws_region" {
  description = "(Optional) AWS Region."
  type = string
  default = "us-east-1"
}

variable "tags" {
  type = map(string)
  description = "(Optional) AWS Tags common to all the resources created."
  default = {}
}

variable "service_cpu" {
  type        = number
  default     = 1024
  description = "The number of CPU units reserved for container."
}

variable "service_memory" {
  type        = number
  default     = 2048
  description = "The amount (in MiB) of memory reserved for container."
}

variable "app_port_server_lr_model" {
  type        = number
  default     = 5000
  description = ""
}

variable "aws_ecr_repo_arn" {
  description = ""
  type = string
  default = "arn:aws:ecr:us-east-1:493395458839:repository/linear-regression"
}

variable "wandb_api_key" {
  description = "Weights & Biases API Key"
  type        = string
  sensitive   = true
}