terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.11.0"
    }
    postgresql = {
      source  = "cyrilgdn/postgresql"
      version = ">= 1.21.0"
    }
  }

  required_version = ">= 1.5.4"

#backend "local" {}
backend "remote" {
    hostname = "spodarets.scalr.io"
    organization = "env-v0o06dgi6sivpq3v2"
    workspaces {
      name = "LR-Model-API"
    }
  }
}

provider "aws" {
  region  = var.aws_region
}
