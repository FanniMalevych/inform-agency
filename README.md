## Inform agency "InfoStruct"

https://inform-agency.onrender.com/
- Login: `admin.user`
- Password: `1qazcde3`


## Getting started

1. Clone the repository

`git clone https://github.com/FanniMalevych/inform-agency.git`

2. Create virtual environment and install dependencies 

`python -m venv venv`

 `venv\Scripts\activate (on Windows)`

 `source venv/bin/activate (on macOS)`

 `pip install -r requirements.txt`

- If you want to use test data run 

`python manage.py loaddata inform_agency_db_data.json`

- After loading data from fixture you can use following superuser (or create another one by yourself):
    - Login: `admin.user`
    - Password: `1qazcde3`

Feel free to add more data using admin panel, if needed.

## Features

- list of topics, redactors and newspapers
- ability to add/update/delete data
- ability to assign/remove user to newspaper as redactor

## Links

- Repository: https://github.com/FanniMalevych/inform-agency.git
- Project page: https://inform-agency.onrender.com/

#### main page view:

![image](assets/main.png)

### data example:

![image](assets/list.png)

### detailed page:

![image](assets/detailed.png)

### login form:

![image](assets/log_in.png)
