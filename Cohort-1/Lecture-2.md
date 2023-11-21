# Управління даними
## Label Studio
1. Встановити Label Studio за допомогою pip:
```
pip install label-studio
```
2. Запустіть Label Studio
```
label-studio start
```
3. Відкрийте інтерфейс Label Studio за адресою:
```
http://localhost:8080
```
[Label Studio документація](https://labelstud.io/guide/).

## DVC
1. Встановити DVC за допомогою pip:
```
pip install dvc
```
2. Ініціалізуйте проект
```
git init
dvc init
```
3. Виповніть команду ```git status``` щоб побачити, які файли строрив dvc:
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   .dvc/.gitignore
	new file:   .dvc/config
	new file:   .dvcignore
```
4. Зробіть перший коміт
```
git commit -m "Initialize DVC"
```
5. Додайте віддалений сторедж
```
dvc remote add -d storage s3://mybucket/dvcstore
```
6. Додайте файл датасету, щоб розпочати відстеження за допомогою dvc:
```
dvc add datafile
```
7. Щоб відстежити зміни за допомогою git, запустіть:
```
git add .gitignore datafile.dvc
```
8. Завантажте данні
```
dvc push
```
9. Зробіть коміт першої версії датасету
```
git commit -m "dataset v0.0.1"
```
10. Додайте новий файл до вашого датасету
```
dvc add datafile2
```
11. Для відстеження змін додайте новий файл до git
```
git add datafile2.dvc
```
12. Завантажте данні
```
dvc push
```
13. Зробіть коміт нової версії датасету
```
git commit -m "dataset v0.0.2"
```
14. Тепер використовуючи git та  checkout ви можете переключатись між версіями ваших датасетів

[DVC документація](https://dvc.org/doc).

[Git документація](https://git-scm.com/doc).
