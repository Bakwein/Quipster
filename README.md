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

[![Login]](https://github.com/Bakwein/web_proje/assets/101413263/66211506-6121-462c-8b7b-64383d38bc2a)

* Login / Register with Google OAuth2.0

* Share a tweet with photo (photo is optional)

* Tweet content correction with AI
* Like and unlike to tweet
* Reply to tweet

* Profile (Profile edit, follow, unfollow)

* Multiple languages support with cookies

* Explore page (You can find random users)

### Security
* HTTPS support, XSS attacks protection, SQL Injection protection, CSRF Protection, Clickjacking protection
