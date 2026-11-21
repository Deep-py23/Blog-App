MyBlog

A blog application I built with Django and PostgreSQL while learning backend development. Users can sign up, write posts, and manage their own posts. Nobody else can edit or delete them.

Features

Register, log in and log out (custom function-based views on Django's built-in User model)
Create, read, update and delete posts
Only the author of a post can edit or delete it, and other users get a 403 page
Categories (one per post) and tags (many per post)
Optional image upload for each post
Home page with the latest posts, showing category, tags and date
Customised Django admin with list columns, filters and search
Custom CSS with Bootstrap and Font Awesome icons
Tech stack

Python 3, Django
PostgreSQL
Pillow (image uploads)
python-decouple (settings and secrets kept in a .env file)
HTML, CSS, Bootstrap, Font Awesome
Database models

Category: name
Tag: name
Post: title, content, author (User), category, tags, image, status, created and updated time
Post to Tag is many-to-many, Post to Category is a foreign key (kept as empty if the category is deleted), and Post to User is a foreign key (the user's posts are deleted with the user).

The site runs at http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin/.

Still to add

Hiding draft posts from other users
Pagination, search and filtering by tag or category
Success messages
Comments
profile per user and update profile