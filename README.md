# infra_actions
Учебный проект для изучения работы GitHub Actions

### Инструкция по запуску
- Склонируйте проект `git clone https://github.com/Andrey-Kugubaev/infra_actions.git` 
- установите и активируйте виртуальное окружение
`python -m venv venv (или python3 -m venv venv) / source venv/Scripts/activate (или source venv/bin/activate)`
- установите зависимости `pip install -r requirements.txt`
- перейдите в диреткорию `infra_project`
- для проверки проекта запустите сервер `python manage.py runserver`
- для запуска _GitHub Actions_ необходимо запушить код на _GitHub_ `git add --all` `git commit -m 'проверка GitHub Actions'` `git push`