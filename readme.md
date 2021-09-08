Basic Concepts in Django:

Project - there is only one project, contains the necessary settings for apps for a specific website. They aren't used in other projects.

App - there can be many apps within the single project and is a component of the larger website, can be used across multiple projects.

Views - contain all the necessary code that will return a specific response when requested such as template or an image and also can redirect to another page

URL mapping - `URLconf` serves as a table of contents for the app, this module finds the link within the project and redirects the request over to views file which then processes the request.


Create a project:

This will be the container for the entire project and any applications that will be created.
`django-admin startproject <projectname> .`   ( this will create a new project in the current directory)

-- `manage.py` -> command-line utility which has the same function as django-admin
-- `init.py` -> empty file that tells python that this directory should be considered a package
-- `settings.py` -> contains all settings/configuration
-- `urls.py` -> contains the URLs within the project
-- `asgi.py`/`wsgi.py` -> server as the entrypoint for webservers

Run the project:
`python manage.py runserver` (this command performs system checks and starts the development server)

Create App:
`python manage.py startapp <appname>` (this command creates the required folders and files - for the app)

Paths and Views:
Views and paths(routes) are core to web framework and are used to determine what infromation to display to user and how user will access it

Paths - all applications allow users to execute different methods or functions through different mechanisms. 
A route tells django if the user makes a certain request for a particular URL or path what function to execute
They are registered by `urlpatterns` - these patterns identify what should be looked for in the URL the user is requesting and determine which function should handle the request
these patterns are collected into a module which is `URLconf`

Views - they determine what information should be returned to user. they are functions or classes that execute in response to user request and return `HTML` or other type of responses

