Discover Flask
==============

[![Build Status](https://travis-ci.org/cassiobotaro/discover-flask.svg)](https://travis-ci.org/cassiobotaro/discover-flask)

My studies about flask using discover flask videos.

## How to run

- Clone repository
- Make a virtualenv (`mkvirtualenv discover-flask`)
- (optional) Ubuntu 14.04 requires install libffi-dev. `sudo apt-get install libffi-dev`
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

| Part |      Title                | Git Tag |
|------|---------------------------|---------|
| 1    | [Setting Up a Static Site](http://youtu.be/WfpFUmV1d0w) ([blog post](http://www.realpython.com/blog/python/introduction-to-flask-part-1-setting-up-a-static-site)) | [part1](https://github.com/realpython/discover-flask/tree/part1) |
| 2    | [Creating a login page](http://youtu.be/bLA6eBGN-_0) ([blog post](http://www.realpython.com/blog/python/introduction-to-flask-part-2-creating-a-login-page)) | [part2](https://github.com/realpython/discover-flask/tree/part2) |
| 3    | [User Authentication](http://youtu.be/BnBjhmspw4c) | [part3](https://github.com/realpython/discover-flask/tree/part3) |
| 4    | [Template Inheritance](http://youtu.be/hNzruwVPtCE) | [part4](https://github.com/realpython/discover-flask/tree/part4) |
| 5    | [Databases](http://youtu.be/_vrAjAHhUsA) | [part5](https://github.com/realpython/discover-flask/tree/part5) |
| 6    | [List Comprehensions](http://youtu.be/WqmqNC8Teeo) | N/A |
| 7    | [Unit Tests](http://youtu.be/1aHNs1aEATg) | [part7](https://github.com/realpython/discover-flask/tree/part7) |
| 8    | [Deploying to Heroku](http://youtu.be/L9uD74nHvFY) | [part8](https://github.com/realpython/discover-flask/tree/part8) |
| 9    | [SQLAlchemy](https://www.youtube.com/watch?v=kuyrL6krkwA) | [part9](https://github.com/realpython/discover-flask/tree/part9) |
| 10   | [Configuration](https://www.youtube.com/watch?v=4Eww3wVZK2I) | [part10](https://github.com/realpython/discover-flask/tree/part10) |
| 11   | [Secret Key](http://youtu.be/tqu9y4iqKVI) | [part11](https://github.com/realpython/discover-flask/tree/part11) |
| 12   | [Heroku Configuration Settings](http://youtu.be/Y-ONxFkAUJc) | [part12](https://github.com/realpython/discover-flask/tree/part12) |
| 13   | [Heroku Postgres Setup](https://www.youtube.com/watch?v=FD0p-opdyoE) | [part13](https://github.com/realpython/discover-flask/tree/part13) |
| 14   | [Local PostgreSQL Setup](https://www.youtube.com/watch?v=Up3p20rgWCw) | [part14](https://github.com/realpython/discover-flask/tree/part14) |
| 15   | [Managing Database Migrations](http://youtu.be/YJibNSI-iaE) | [part15](https://github.com/realpython/discover-flask/tree/part15) |
| 16   | [Database Downgrades with Flask-Migrate/Alembic](http://youtu.be/5UT1binVuYc) | [part16](https://github.com/realpython/discover-flask/tree/part16) |
| 17   | [Virtualenvwrapper](http://youtu.be/thHNYVrY0lU) | [part17](https://github.com/realpython/discover-flask/tree/part17) |
| 18   | [Password Hashing](http://youtu.be/LTJH5Mdgn4w) | [part18](https://github.com/realpython/discover-flask/tree/part18) |
| 19   | [Blueprints](http://youtu.be/AeI_rBeZmwg) | [part19](https://github.com/realpython/discover-flask/tree/part19) |
| 20   | [Blueprints Redux](http://youtu.be/TwNp1UagE9U) | [part20](https://github.com/realpython/discover-flask/tree/part20) |
| 21   | [User Authentication (part 2)](http://youtu.be/_pzMDIi5BuI) | [part21](https://github.com/realpython/discover-flask/tree/part21) |
| 22   | [Unit Testing with Flask-Testing](http://youtu.be/WDh_VQ41kYI) | [part22](https://github.com/realpython/discover-flask/tree/part22) |
| 23   | [Session Management with Flask-Login](http://youtu.be/rJGMOOSnHL0) | [part23](https://github.com/realpython/discover-flask/tree/part23) |
| 24   | [Testing User Login and Logout](https://www.youtube.com/watch?v=v0fp1O7zCUY) | [part24](https://github.com/realpython/discover-flask/tree/part24) |
| 25   | [User Registration (functionality and unit tests)](http://youtu.be/kt4PEa5tsVw) | [part25](https://github.com/realpython/discover-flask/tree/part25) |
| 26   | [Finalize Messaging System](http://youtu.be/WnT188ePHg4) | [part26](https://github.com/realpython/discover-flask/tree/part26) |
| 27   | [Test Coverage with coverage.py](http://youtu.be/7Aqcn0-uAr0) | [part27](https://github.com/realpython/discover-flask/tree/part27) |
| 28   | [Flask Testing!](http://youtu.be/YO2k80aDJj8) | [part28](https://github.com/realpython/discover-flask/tree/part28) |
| 29   | [Flask Testing (increase test coverage)](http://youtu.be/ASNNTb6o3pU) | [part29](https://github.com/realpython/discover-flask/tree/part29) |
| 30   | [Continuous Integration](http://youtu.be/qAe6v_6SMA8) | [part30](https://github.com/realpython/discover-flask/tree/part30) |


**You can view the entire video playlist [here](http://www.youtube.com/watch?v=WfpFUmV1d0w&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&feature=share).**
