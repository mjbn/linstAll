#############################
##### Create a Database #####
#############################

1.Log into MariaDB:

```
mysql -u root -p
```

(`-u <user>` specifies the user, and `-p` will prompt you for the password.)
(The Script has done the 1st step if you dont want to do this steps press `^c` or `Ctrl+c` to cancell the command or type `\q` to exit the prompt)

2.You will see the MariaDB prompt. Create a database and create and grant a user permissions on the database:

```
CREATE DATABASE webdata;
GRANT ALL ON webdata.* TO 'webuser' IDENTIFIED BY 'password';
```

(In this example webdata is the name of the database, webuser is the username, and password is the user’s password.
Note that database usernames and passwords do not correlate to system user accounts.)

3.Quit MariaDB:

```
\q
```


------------------------------------------------------------------------------------------------------------------------
Coding By M.J. Bagheri Nejad (MJBN)

[WebSite](http://mjbn.ir)

[GitHub](https://github.com/mjbn)

[Src](https://github.com/mjbn/linstAll)
