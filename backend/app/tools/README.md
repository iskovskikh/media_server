

Сгенерировать приватный ключ:

`openssl genrsa -out private.pem 2048`
    
Сгенерировать публичный ключ:

`openssl rsa -in private.pem -outform PEM -pubout -out public.pem` 