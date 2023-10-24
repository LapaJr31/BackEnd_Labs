# Lab1 

### Кроки по запуску
1. Клонуємо репозиторій
2. Будуємо наш проєкт командою `docker-compose build`
3. Запускаємо командою `docker-compose up`, і також можемо додати прапорець `-d` для того, щоб процес був фоновим
4. Переходимо за [http://127.0.0.1:8080] (http://127.0.0.1:8080)
5. Щоб перевірити healthcheck endpoint в консолі використаємо curl: `curl -i http://127.0.0.1:8080/healthy` або якщо використати задеплоєний білд на [render.com] (render.com) то `curl -i https://lab1healthcheck.onrender.com/healthy`


