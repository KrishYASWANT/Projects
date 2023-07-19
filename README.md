# Projects
Make sure you have a database and table in you MySQL with the following commands
CREATE TABLE Users (
  email VARCHAR(255) PRIMARY KEY,
  password VARCHAR(255) NOT NULL,
  address1 VARCHAR(255) NOT NULL,
  address2 VARCHAR(255),
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  zip VARCHAR(10) NOT NULL
);

This is just a beginers project which is based on django and it just connects the front end HTML to the Database which in this is MySQL.
To make it work do change the settings.py and views.py for the database connection as the password and the database name will differ.

It gives lots of error if the user and password are wrong and make user=='root' as its generally used and don't keep it as "localhost@....".
