resource "aws_apprunner_service" "server_lr_model" {
  service_name = var.name_server_lr_model

  source_configuration {
    auto_deployments_enabled = false

    authentication_configuration {
      access_role_arn = aws_iam_role.apprunner_ecr_role.arn
    }

    image_repository {
      image_identifier      = "493395458839.dkr.ecr.us-east-1.amazonaws.com/linear-regression:c30645781ce213f594edd6b31be6ded9d4611dd1"
      image_repository_type = "ECR"

      image_configuration {
        port = var.app_port_server_lr_model
        runtime_environment_variables = {
          WANDB_API_KEY=var.wandb_api_key
        }
      }
    }
  }

  instance_configuration {
    cpu                = var.service_cpu
    memory             = var.service_memory
  }
}
