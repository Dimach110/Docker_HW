1. Сборка docker:
   В консоли из папки проекта прописать docker docker build . -t dj_logistic01
2. Запуск проекта:
   В консоли из папки проекта прописать docker run -d -p 80:80 --name=logistic dj_logistic01