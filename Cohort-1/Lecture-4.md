# Розгортання ML моделей

## FastAPI+Docker
Приклад - [/Cohort-1/LinearRegression](/Cohort-1/LinearRegression)

Команди для білда контейнера та його запуску (локально):

```
docker build -t lr-model .

docker run -p 8080:5000 --env WANDB_API_KEY=key_id lr-model

http://localhost:8080/docs
```

curl -X 'POST' \                                                                                       11:37:41 PM
  'http://127.0.0.1:8080/predict/' \
  -H 'Content-Type: application/json' \
  -d '{"years": [2024,2002]}'


## Ray

Приклад - [/Cohort-1/YOLOv8](/Cohort-1/YOLOv8)

Перевіряємо кластер

```
ray up -y cluster-config.yaml
```
Можемо зайти на дашборд, якщо порти інстанса кластера відкриті:

```
http://3.15.175.158:8265/
```

Чи виконати команду, щоб прокинути порти:

```
ray dashboard cluster-config.yaml

http://localhost:8265/
```

Запускаємо модель локально чи через прокинуті порти на localhost:
```
serve run object_detection:entrypoint
```

Запускаємо на віддаленому кластері:

```
RAY_ADDRESS='ray://3.15.175.158:10001' serve run object_detection:entrypoint
```
Перед цим може знадобитись налаштувати python environment потрібної версії.

Наприклад, це можна зробити за допомогою conda:

Встановити [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/index.html)

```
conda create --name py3109 python=3.10.9
conda activate py3109
```

Знайти задеплоїну модель можна на дашборді Ray кластеру:

```
http://3.15.175.158:8265/#/serve
```

Щоб перевірити роботу моделі, можна скористатись файлом `test.py`, у якому прописати правильну адресу для Ray кластера, та лінк до зображення.

## dstack

Приклад - [/Cohort-1/Llama2](/Cohort-1/Llama2)

Документація - https://dstack.ai/docs/guides/services/ 

Для цього прикладу необхідно мати робочий домен. Я буду використовувати - ml.flyelephant.net

Спочатку запустимо dstack сервер:
```
dstack server
```
Тепер ініціалізуемо у папці проекта:
```
dstack init
```
Тепер створимо gateway:
```
dstack gateway create --region us-east-1 --set-default  --backend aws --domain ml.flyelephant.net
```
Ми отримаєто для нього IP адрес, який потрібно будет прописати для нашого домену у наступному форматі:
```
*.ml.flyelephant.net.  A  IP адрес
```
Тепер ми можемо задеплоїти нашу модель:
```
dstack run . -f serve-llama2.dstack.yml --gpu 1
```
Після деплою, можемо зайти на API сторінку:
```
https://great-grasshopper-1-0.ml.flyelephant.net/docs
```
А також перевірити, як вона працює:
```
curl -X POST --location https://great-grasshopper-1-0.ml.flyelephant.net/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
          "model": "NousResearch/Llama-2-7b-hf",
          "prompt": "San Francisco is a",
          "max_tokens": 70,
          "temperature": 0
        }'
```
