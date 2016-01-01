Discover Flask
==============

My studies about flask using discover flask videos.

## How to run

- Clone repository
- Make a virtualenv (`mkvirtualenv discover-flask`)
- Install packages `pip install -r requirements.txt`
- Setup your database uri and config 

change the file : `~/.virtualenvs/discover-flask/bin/postactivate`

with: 
```bash
#!/usr/bin/zsh
# This hook is sourced after this virtualenv is activated.
export DATABASE_URL="postgresql://user:password@localhost/discover_flask_dev"
export APP_SETTINGS="config.DevelopmentConfig"
``` 

##Original

[Github](https://github.com/realpython/discover-flask/)

[Website](http://discoverflask.com/)

##List of videos

| Part |      Title                |
|------|---------------------------|
| 1    | [Setting Up a Static Site](http://youtu.be/WfpFUmV1d0w) ([blog post](http://www.realpython.com/blog/python/introduction-to-flask-part-1-setting-up-a-static-site))|
| 2    | [Creating a login page](http://youtu.be/bLA6eBGN-_0) ([blog post](http://www.realpython.com/blog/python/introduction-to-flask-part-2-creating-a-login-page))|
| 3    | [User Authentication](http://youtu.be/BnBjhmspw4c)|
| 4    | [Template Inheritance](http://youtu.be/hNzruwVPtCE) |
| 5    | [Databases](http://youtu.be/_vrAjAHhUsA) |
| 6    | [List Comprehensions](http://youtu.be/WqmqNC8Teeo) |
| 7    | [Unit Tests](http://youtu.be/1aHNs1aEATg) |
| 8    | [Deploying to Heroku](https://www.youtube.com/watch?v=vxiHmjKqXUg) |
| 9    | [SQLAlchemy](https://www.youtube.com/watch?v=kuyrL6krkwA) |
| 10   | [Configuration](https://www.youtube.com/watch?v=4Eww3wVZK2I) |
| 11   | [Secret Key](http://youtu.be/tqu9y4iqKVI?list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM)|
| 12   | [Heroku Configuration Settings] (http://youtu.be/Y-ONxFkAUJc)|
| 13   | [Heroku Postgres Setup](https://www.youtube.com/watch?v=FD0p-opdyoE)|
| 14   | [Local PostgreSQL Setup](https://www.youtube.com/watch?v=Up3p20rgWCw)|
| 15   | [Managing Database Migrations](http://youtu.be/YJibNSI-iaE)|
| 16   | [Database Downgrades with Flask-Migrate/Alembic](http://youtu.be/5UT1binVuYc)|
| 17   | [Virtualenvwrapper](http://youtu.be/thHNYVrY0lU|

**You can view the entire video playlist [here](http://www.youtube.com/watch?v=WfpFUmV1d0w&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&feature=share).**
