# django-online-job-portal

This is a test online job portal project created using Django 4.x. But don't worry this is a fully working project. There is no super-amazing front-end, just back-end codes with minimal html :)

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