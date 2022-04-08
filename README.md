# django-online-job-portal

This is a test online job portal project created using Django 4.x. But don't worry this is a fully working project. There is no super-amazing front-end, just back-end codes with minimal html :)

## Before You Begin

1. You should generate SecretKey here <https://djecrety.ir/>
2. If you are going to use a PostreSQL database, you must first install PostreSQL/pgAdmin 4 on your operating system.
3. If you don't want to deal with it and don't want to use PostreSQL database, just activate SQL database from config/settings.py by uncommenting it.
4. If you want to use pasword reset system, you should have a gmail account and in the account security settings; 
   1. Activate two-factor authentication
   2. Create App password
5. In your IDE install project environment requirements we need.

```bash
$ git@github.com:alikasimoglu/OnlineJobPortal.git
```
Now you can access the application at <http://127.0.0.1:8007/> and the admin site
at <http://127.0.0.1:8007/controlme>.

Stack and version numbers used:

| Name           | Version |
|----------------|---------|
| Django         | 4.0.3   |
| Python         | 3.10    |


## Folder structure
```
.
├── config                  # main project files needed for configuration
├── mainsite                # mainsite app
├── media                   # media files uploaded by users
├── profiles                # profiles app (extends from django user system)
├── templates               # base templates
├── .env-example            # environments file
├── .gitignore              # determines files excluded from github
├── manage.py
├── README.md               # this file
└── requirement.txt         # project environment requirements
```

Project using PostgreSQL database on demand. But easily can be changed to SQLite in config/settings.py 