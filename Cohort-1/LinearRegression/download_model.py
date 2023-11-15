import os
import wandb

wandb_api_key = os.getenv("WANDB_API_KEY")
wandb.login(key=wandb_api_key)

run = wandb.init()

artifact = run.use_artifact('dmytro-spodarets/model-registry/linear_regression:latest', type='model')
path = artifact.get_path("linear_regression_model.pth")
path.download('./')