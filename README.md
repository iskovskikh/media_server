
# MediaApp

Проект в разработке

- [ ] страница – авторизация

- [ ] страница – файлы

- [x] страница – пользователи

- [ ] микросервис – журналирование    

## Запуск

Для запуска выполнить

`make all`

приложение запустится на [http://localhost:3000](http://localhost:3000)

по адресу [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
можно увидеть swagger схему

остановить приложение: 

`make all-down`

---

## Доступные команды:

запустить все:

`make all`
    
`make all-down`

фронт:

`make frontend`

`make frontend-down`

`make frontend-logs`

бек:

`make backend`

`make backend-down`

`make backend-logs`

`make backend-shell`

`make backend-makemigrations`

бд:

`make storages`

`make storages-down`
