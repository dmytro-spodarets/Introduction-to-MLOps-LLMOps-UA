# Створення ML моделей
## Тренування ML моделей
### dstack

Встановлення dstack
```
pip install "dstack[all]" -U
```

Конфігурування dstack за допомогою файла config.yml
```
$ ~/.dstack/server/config.yml 
projects:
- name: main
  backends:
  - type: aws
    regions: [us-east-1, us-east-2]
    creds:
      type: default
 ```
https://dstack.ai/docs/reference/server/config.yml/ 

Основні команди dstack

- `dstack server` - зупуск сервера dstack
- `dstack init` - ініціювання проекта
- `dstack run` - запуск джоби
Файли для конфігурування джоб
```
.dstack.yml чи train.dstack.yml чи *.dstack.yml
```
Приклад конфігурування vscode через файл dev-env.dstack.yml
```
type: dev-environment
python: "3.11" 
ide: vscode
```

Приклад конфігурування тренування моделі через файл train.dstack.yml

```
type: task
python: "3.11" 
commands:
  - pip install -r requirements.txt
  - python train.py
```

https://dstack.ai/docs/reference/dstack.yml/task/#example 

Приклад конфігурування тренування профілю за допомогою файла .dstack/profiles.yml
```
profiles:
  - name: MLOpsIntro
    resources:
      cpu: 16
      memory: 32
    spot_policy: auto
    default: true
```
https://dstack.ai/docs/reference/profiles.yml/ 


### Ray
Встановлення Ray
```
pip install -U "ray[all]"
```
Конфігурування кластера відбуваеться через файл `cluster-config.yaml`, який далі використовується для його запуска:
```
ray up -y cluster-config.yaml
```

Приклад `cluster-config.yaml`:
```
cluster_name: AWS-LLMOps

max_workers: 5

# Cloud-provider specific configuration.
provider:
    type: aws
    region: us-east-2

available_node_types:
  ray.head.default:
    resources: {}
    node_config:
      InstanceType: m5.large
      ImageId: ami-0aa5328ffcf5d34ac

  ray.worker.default:
    min_workers: 0
    max_workers: 5
    resources: {}
    node_config:
      InstanceType: m5.2xlarge
      ImageId: ami-0aa5328ffcf5d34ac

head_node_type: ray.head.default
```
Підключення до дашборду:
```
ray dashboard cluster-config.yaml
```

Запуск джоби на локальному кластері:
```
ray job submit --no-wait --working-dir . -- python script.py
```

Запуск джоби на віддаленому кластері:
```
RAY_ADDRESS='http://3.15.175.158:8265' ray job submit --no-wait --working-dir . -- python script.py
```

Різні команди роботи з джобами:
```
ray job logs JOB_ID
ray job status JOB_ID
ray job stop JOB_ID
ray job list
```

https://docs.ray.io/en/latest/cluster/running-applications/job-submission/cli.htm
https://docs.ray.io/en/latest/cluster/running-applications/job-submission/jobs-package-ref.html 


## Трекінг експериментів та версіювання моделей

### MLflow
Встановлення MLflow локально
```
pip install mlflow
```

Локальний запуск MLflow
```
mlflow ui
```
чи
```
mlflow server --host 127.0.0.1 --port 8080
```
Документація по роботі з MLflow - https://mlflow.org/docs/latest/index.html


### Weights & Biases
Встановлення Weights & Biases локально
```
pip install wandb
```
Локальний запуск Weights & Biases
```
wandb server start
```
Документація по роботі з Weights & Biases - https://docs.wandb.ai/