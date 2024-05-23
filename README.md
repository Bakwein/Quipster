
https://github.com/Bakwein/web_proje/assets/88441975/b1a2ebd2-ee8a-4cd5-8f27-202515f1d68e
Aşağıdaki alanda ilgili özelliğin sorumlusunu tabloda yazınız.  Projenizi amacını ve işlevlerinin kısa özetini yazınız. Talep edilen özelliklerin projeniz içerisinde nasıl uygulanacağını kısaca açıklayınız.

|No|Tech|Öğrenci No / Ad  Soyad|
| :- | :- | :- |
|1|Presentation Layer: UI Framework Using |220202115/Ahmet İdris|
|2|Business Layer: OOP Components|210202026/Şaban Murat Altun|
|3|Data Layer: ORM / Migrations Using|220202101/Sefa Tunca|
|4|Web Service Implementation|220202115/Ahmet İdris|
|5|RBAC Implementation|220202101/Sefa Tunca|
|6|Authorization Implementation|220202101/Sefa Tunca|
|7|Session / Cookie Management|210202026/Şaban Murat Altun|
|8|Extension / Third Party Library Using|220202115/Ahmet İdris|
|9|Web Security Implementation|220202101/Sefa Tunca|
|10|Cloud Service (AI) Using|210202026/Şaban Murat Altun|



Proje Özeti: 

Django , Html+Css+Javascript + Tailwind CSS , veri tabanı ve çeşitli api ve 3rd party kütüphaneleri kullanarak sosyal medya uygulaması


Özellikler:

1. Presentation Layer: UI Framework Using : Html+Css+Javascript + Tailwind CSS
1. Business Layer: OOP Components: Django models - views -> classes, methods,…
1. Data Layer: ORM / Migrations Using: Django'nun ORM için MVC (Model-View-Controller) mimarisi
1. Web Service Implementation: RESTful
1. RBAC Implementation: Roles
1. Authorization Implementation: Google Oauth
1. Session / Cookie Management: Session
1. Extension / Third Party Library Using: File System
1. Web Security Implementation: Django Crsf, vb. SQL injection,Xss atakları engelleme
1. Cloud Service (AI) Using: Cümle Önerisi(Sentence Suggestion)

## Environment file

name: .env
position: ./quipster/quipster

env file:
```
SECRET_KEY=
DEBUG=
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=
```

Env dosyası size iletilen github linki ile paylaşılmıştır.

## Start server

```
cd quipster/
docker-compose up --build

url: https://127.0.0.1:8000
```

⚡Recommended to run in chrome or brave browsers' latest versions⚡

## Features

* Login, Register, Logout

[![Login]](https://github.com/Bakwein/web_proje/assets/88441975/69abc950-a5c3-400d-8eb2-3bc50703ad67)


* Login / Register with Google OAuth2.0

[![Google Oauth2]](https://github.com/Bakwein/web_proje/assets/88441975/5729914c-ca9b-4cd2-9490-39e5fedb4c3e)


* Share a tweet with photo (photo is optional)
<img width="1552" alt="Ekran Resmi 2024-05-23 19 17 05" src="https://github.com/Bakwein/web_proje/assets/88441975/91ca8d91-d1dd-4e40-86ef-88beaeb1a1e6">


* Tweet content correction with AI

https://github.com/Bakwein/web_proje/assets/88441975/736c651b-4bcd-4cf9-8920-ee03fc7ef18a

* Explore page (You can find random users)
* Like and unlike to tweet, Follow, Unfollow

https://github.com/Bakwein/web_proje/assets/88441975/14979c53-0209-429c-9a22-99fab42125b7


* Reply to tweet


https://github.com/Bakwein/web_proje/assets/88441975/8927d519-c35b-4f2b-a157-8d51d9c2e192



* Profile (Profile edit)
  
[![Profile Edit]](https://github.com/Bakwein/web_proje/assets/88441975/d2c9f176-eb2f-48c9-bac4-eb7e3ee9d702)


* Multiple languages support with cookies



https://github.com/Bakwein/web_proje/assets/88441975/97c25247-c459-4b7a-a5fa-a31db68b75a5






### Security
* HTTPS support, XSS attacks protection, SQL Injection protection, CSRF Protection, Clickjacking protection
