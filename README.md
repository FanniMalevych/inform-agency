## Inform agency "InfoStruct"

### Here is implementation of inform agency, where you can store info about redactors and their newspapers. Also implemented ability to get detailed data and update it if needed.


- If you want to use test data run 

`python manage.py loaddata inform_agency_db_data.json`

- After loading data from fixture you can use following superuser (or create another one by yourself):
    - Login: `admin.user`
    - Password: `1qazcde3`

Feel free to add more data using admin panel, if needed.

#### main page view:

![image](assets/main.png)

### data example:

![image](assets/list.png)

### detailed page:

![image](assets/detailed.png)

### login form:

![image](assets/log_in.png)
