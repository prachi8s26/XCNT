# XCNT

## Steps to setup Database
1. Create a database in root user (You can also create a different user)
test
```
mysql -u root -p
CREATE DATABASE cashcog;
```
  Configure the same username and password in settings.py file of the project

2. 
```
$ python manage.py migrate
```
  Output of the above command will be similar to this
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  ```
  The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app

3. 
  ```
  $ python manage.py makemigrations cashcog
  ```
  By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

4.
```
$ python manage.py sqlmigrate cashcog  0001
```
  The output of the above command will be something similar to this 
```
--
-- Create model Expense
--
CREATE TABLE `cashcog_expense` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `uuid` varchar(100) NOT NULL, `description` longtext NOT NULL, `created_at` datetime(6) NOT NULL, `amount` integer NOT NULL, `currency` varchar(50) NOT NULL, `status` integer NOT NULL, `employee_uuid` varchar(100) NOT NULL, `employee_first_name` varchar(100) NULL, `employee_last_name` varchar(100) NULL);
ALTER TABLE `cashcog_expense` ADD CONSTRAINT `cashcog_expense_employee_id_075e8fa0_fk_cashcog_employee_id` FOREIGN KEY (`employee_id`) REFERENCES `cashcog_employee` (`id`);
CREATE INDEX `cashcog_expense_created_at_7ed0d740` ON `cashcog_expense` (`created_at`);
CREATE INDEX `cashcog_expense_amount_fca05cf9` ON `cashcog_expense` (`amount`);
CREATE INDEX `cashcog_expense_status_9d063b71` ON `cashcog_expense` (`status`);
```
The sqlmigrate command doesn’t actually run the migration on your database - it just prints it to the screen so that you can see what SQL Django thinks is required
  
 5.
 ```
 $ python manage.py migrate
 ```
 Output of the above command will be something similar to this
 ```
 Operations to perform:
  Apply all migrations: admin, auth, cashcog, contenttypes, sessions
Running migrations:
  Applying cashcog.0001_initial... OK
 Migrations for 'cashcog':
  cashcog/migrations/0001_initial.py
    - Create model Employee
```

# Running the development server
```
$ python manage.py runserver
```

By default, the runserver command starts the development server on the internal IP at port 8000.
http://127.0.0.1:8000/cashcog/<api-url>

e.g. http://127.0.0.1:8000/cashcog/update-expense

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:
```
$ python manage.py runserver 8080
```

# Setup Admin Account
```
$ python manage.py createsuperuser
```
Enter the admin username and password that you want

Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen


