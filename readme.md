# Basic Concepts in Django:

*Project* - there is only one project, contains the necessary settings for apps for a specific website. They aren't used in other projects.

*App* - there can be many apps within the single project and is a component of the larger website, can be used across multiple projects.

*Views* - contain all the necessary code that will return a specific response when requested such as template or an image and also can redirect to another page

*URL mapping* - `URLconf` serves as a table of contents for the app, this module finds the link within the project and redirects the request over to views file which then processes the request.


### Create a project:

This will be the container for the entire project and any applications that will be created.
`django-admin startproject <projectname> .`   ( this will create a new project in the current directory)

- `manage.py` -> command-line utility which has the same function as django-admin
- `init.py` -> empty file that tells python that this directory should be considered a package
- `settings.py` -> contains all settings/configuration
- `urls.py` -> contains the URLs within the project
- `asgi.py`/`wsgi.py` -> server as the entrypoint for webservers

#### Run the project:
`python manage.py runserver` (this command performs system checks and starts the development server)

By default, the runserver command starts the development server on the internal IP at port 8000.
If you want to change the server’s port, pass it as a command-line argument. (`python manage.py runserver 8080`)

#### Create App:
`python manage.py startapp <appname>` (this command creates the required folders and files - for the app)

### Paths and Views:
Views and paths(routes) are core to web framework and are used to determine what infromation to display to user and how user will access it

- *Paths* - all applications allow users to execute different methods or functions through different mechanisms. 
A route tells django if the user makes a certain request for a particular URL or path what function to execute
They are registered by `urlpatterns` - these patterns identify what should be looked for in the URL the user is requesting and determine which function should handle the request
these patterns are collected into a module which is `URLconf`

- *Views* - they determine what information should be returned to user. they are functions or classes that execute in response to user request and return `HTML` or other type of responses
View functions always take at least one parameter named `request` which represents the users request - more parameters can be provided which needs to be registered when creating the route.

### Rendering the template
Django's templating engine takes the HTML template and combine it with any data that is provided and finally emit the HTML for browser - the helper function to perform is `render`.
The `render` function needs the object that represents the request which is the `request` parameter.
To pass data into the template, provide `render` with a `context` dictionary object - which contains a set of key/value pairs where each key becomes a variable in the template

The `render()` function takes the `request object` as its first argument, a `template name` as its second argument and a `dictionary` as its optional third argument. It returns an `HttpResponse object` of the given template rendered with the given context.

### Register a path
Web framework uses `path` to process user requests, which converts the portion of the URL after the name of the domain and before the query string into a function call
Paths in Django are registered by creating URLconf

```
sample path: path('',views.index,'index')
explanation: for a module called views, traffic can be routed to a function in views called index
```
The `path()` function is passed four arguments, two required: route and view, and two optional: kwargs, and name. 
- route - is a string that contains URL pattern, when processing a request Django starts at the first pattern at *urlpatterns* and makes it way down the list comparing the requested URL against them until it finds the match
- view - when Django finds a matching pattern it calls the specified view function with *HttpRequest* object as the first argument and any captured values from the route as keyword arguments
- kwargs - arbitrary keyword arguments can be passed in a dictionary to the target view
- name - naming the URL makes it to refer unambiguously from elsewhere in Django specially from templates

#### URL parameters
It's a common practice to pass parameters to an application as part of the URL. In django parameter can be specified by special syntax (`<modelname>/<datatype>:<columnname>`) which takes care of the data type that is expected as input and name

### Django templates
Templates are text files that can be used to generate text based formats such as HTML or XML. Each template contains static data that's shared across the site and can also contain placeholders for dynamic data - they control the behaviour on what will appear as the final page.

*Variables* - used to indicate a value that's evaluated at runtime.
Django provides a way to display variables in a template by using `{{ }}` syntax. The view passes the variables into a template by using the `render` function - values as well as other data including ORM queryset are also allowed to be passed to display data from the database to application.
The template system uses dot-lookup syntax to access variable attributes.

*Filters* - are great way to control how data appears when it's requested in a template.

*Tags* - used to perform loops, create text or provide other types of commands for the template engine.
We can use `if` statements for boolean logic and `for` loops for iteration.

*Template inheritance* - Django templates support shared structures through inheritance
For ex: creating child page from the parent using the `extends` keyword

*Best Practice - Template Namespacing*

Django will choose the first template it finds whose name matches, and if you had a template with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them. That is, by putting those templates inside another directory named for the application itself.

### Generic Views
This system streamlines the creation of repetitive code. 
This provides classes which contain the core code already, once inherited from the appropriate class and set a couple of properties and register an appropriate path in URLconf it will be ready to use.
- DetailView - is used to display a detail page for an item, this retrieves the item from a specified model by the `PK` and passes to the template (default template name - `<model>_detail.html`). Also, `as_view()` method will be used in the `path` entry to convert the class to view
- ListView - works mostly like `DetailView` but is designed to work with any form of query that returns multiple items - so need to overwrite `get_queryset()` function which is called by the generic view system to retrieve the items from the database

Generic views can streamline the amount of code required to enable/allow users to modify data
- CreateView - used to allows a user to create items, it walks through the preceding process and dynamically creates the form, post success it displays the detail page for the newly created item (`fields` property will be included where list of editable fields will be displayed to ensure that fields which shouldn't be edited don't appear on the form)
- UpdateView - behaves same as `CreateView` with the difference that it automatically loads an item based on the `pk` parameter

After successful creation/updation of item Django redirects to the details page of the item - it does so by retrieving the URL for the details by using `get_absolute_url` on the associated model - this can be done by using `reverse` on URLconf
- DeleteView - this allows user to delete an item by using `pk`, once done to redirect need to set `success_url` to the appropriate value and the url can be found by using `reverse_lazy`

The placeholder template ensures the form matches the rest of the site - generic views automatically create a `form` variable for the template to use (the form elements can be displayed inside `<p>` tag or as `<table>`)
the form variable contains all of the appropriate HTML to create the controls from the form. The form template must include
- `form` element with the `method` set to POST to trigger the save operation on the server
- `{% csrf_token %}` to add the CSRF (cross site request forgery) token to prevent spoofing
- `{{ form.as_p }}` or `{{ form.as_table }}` to display dynamically generated form
- `submit` button



### Django object-relational mapper
Django is focused on data-driven application, so it provides its own object-relational mapper(ORM) - which separates database calls from objects.
This can be used to design objects that represent your data and manage database operations. They act as middleware between an application and the database.

Basically ORM:
- manages creating and updating the database as needed
- handles the queries
- converts (or maps) the requests that you make through your objects into appropriate database calls

*Models in Django* - is a representation of some piece of data that your application will work with - any form of data.
This is a class that inherits a collection of functionality from `django.models.Model`
The collection includes methods (to query the database), create new entries, save updates, define fields, set metadata and establish relationship between models.
*Fields* - they define the data structure of the models - which includes piece of data that the model needs to store
*Field Options* - allows adding null or blank values or mark as unique to metadata, also allows to set validation options and provide custom messages for validation errors
 - null
 - blank
 - default
 - unique
 - min_length/max_length - used with string types to define the length
 - min_value/max_value - used with number type to define range

Some Field classes have required arguments. `CharField`, for example, requires that you give it a `max_length`. That’s used not only in the database schema, but in validation.

All applications must be registered with the project in Django by adding it to `INSTALLED_APPS` list (this will be present in `settings.py` under projects).
This tells Django that this app needs to be included when it runs the project.

#### Keys and relationships
Django's ORM will add key (primary key - an automatically incremented integer) automatically to every model that is created by adding `id` field
ORM also supports `foreign key relationship` using `ForeignKey` field  - Django automatically adds a property to the parent to provide access to all children called `<child>_set`

#### Manage the database
Django ORM could also be used to create and update the database through a process known as migrations.

*Migrations* - is a collection of updates to be performed on a database's schema, when we create our models and defined the fields we also defind the tables, columns and relationships between those tables - created our schema definition by creating our models.
They are used in creating and updating the database as the models change - they abstract the process of updating the database away from us.

- `python manage.py makemigrations` (uses current list of migrations to start and then uses the current state of models to determine the delta and then generates the necessary code to update the database)
- `python manage.py showmigrations` (lists all the migrations)
- `python manage.py sqlmigrate <app_label> <migration_name>` (command to build the appropriate `SQL` statements, any operation that happen inside a `RDBMS` require `SQL` - Django's migrations generate the appropriate `SQL` when they are run)
- `python manage.py migrate <app_label> <migration_name>` (to run a specific migration or all migrations on the database configured in `settings.py` by looking at the *INSTALLED_APPS* setting and creates the necessary database tables)
- `python manage.py shell` (interactive shell provide by Django to work on the database)

``` 
app_label is the name of your app(name of the folder that contains the app) migration_name is the name of the migration
for migrate they are optional, if either of them are not provided then all migrations will run
At the very beginning for showmigrations, Django will list multiple migrations which includes various tables for its user management system, managing sessions and other internal uses
```

The three-step guide to making model changes:
- Change your models (in `models.py`).
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.

The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also usable by other developers and in production.

Few commands for the interactive Python shell and playing around with the free API Django
```
>>> from <app_name>.models import models,... # Import the model classes
>>> <modelname>.objects.all()    # retrieve all the records for the model
>>> a = <modelname>(field1=,field2='',...) 
>>> a.save() # save the object to database
>>> <modelname>.objects.filter(pk=1) # filter and retrieve record from database
>>> a=<modelname>.object.get(id=n)     # request an id from database
>>> a.<relationship_model_name>_set.all() # display records from the related object 
>>> a.delete       # delete a specific record
>>> <modelname>._meta.fields # get list of attributes for the model
>>> <modelname>._meta.get_fields() # will display relationships   
```
Django offers a powerful and intuitive way to “follow” relationships in lookups, taking care of the SQL JOINs for you automatically, behind the scenes. To span a relationship, use the field name of related fields across models, separated by double underscores, until you get to the field you want.
`Succession_Season_Episodes.objects.filter(succession_seasons__name='Season I')`

Keyword argument queries – in `filter()`, etc. – are “AND”ed together. If you need to execute more complex queries (for example, queries with OR statements), you can use `Q objects`.


Django provides `F expressions` to allow instances of `F()` to act as a reference to a model field within a query. These references can then be used in query filters to compare the values of two different fields on the same model instance.
An `F()` object with a double underscore will introduce any joins needed to access the related object - span relationships in an `F()` object.


### Django Admin Site
Django includes a built-in admin site that can be used to manage the data in application and security - also includes authentication and authorization implementation.
It has three main types of users by default
- users -- can't access admin site or manage data/users
- staff -- by default have access to admin site but can't manage data/users
- superusers -- full access

`python manage.py createsuperuser` (to create a superuser, post which users/staffs can be created by accessing the admin site)

*manage data and register models* - to manage the data the models needs to be registered so that they are editable through the admin tool.
Add the models that needs to be registered under `<app_name>/admin.py`

```
The display in admin site shows the name that has been set the __str__ method on our objects.
The default display of any object is the value returned by __str__
```

### Django deployment considerations
- Debug mode - in `settings.py` *DEBUG* option should be set to *False* to avoid potential insights of the application from an attacker
- Secret Key - to protect sensitive information Django uses a secret key to sign any values that must not be tampered with, when to deploy to production the key should be read from more secure location
- Allowed hosts - `settings.py` contains a list of server names called *ALLOWED_HOSTS* which determines where the application can run from - this needs to be updated before deploying to production host
- Static files - these files are not part of Django templating system which include JavaScript or CSS files - in production need to configure a service to server any static files - during deployment all static files are collected into a location indicated by `STATIC_ROOT` in `settings.py` (run `python manage.py collectstatic` to collect static files)
- database - should contain the list of available connection strings


#### Deploying to HEROKU
In order to execute the application Heroku needs to set up the appropriate environment and dependencies - which is provided by a number of files
- runtime.txt - the programming language and version to use
- requirements.txt - the python component dependencies
- Procfile - a list of processes to be executed to start the application (for Django this will be the Gunicorn web app server  with a `.wsgi` script)
- wsgi.py - WSGI configuration file to call Django application in the Heroku environment

Heroku is closely integrated with the git source code version control system, using it to upload/synchronise any changes you make to the live system. It does this by adding a new heroku "remote" repository named heroku pointing to a repository for your source on the Heroku cloud.

We can't use the default `SQLite` database on Heroku because it is file-based, and it would be deleted from the ephemeral file system every time the application restarts. The Heroku mechanism for handling this situation is to use a database add-on and configure the web application using information from an environment configuration variable, set by the add-on.

During development, we used Django and the Django development web server to serve our static files (CSS, JavaScript, etc.). In a production environment we instead typically serve static files from a content delivery network (CDN) or the web server. To make it easy to host static files separately from the Django web application, Django provides the `collectstatic` tool to collect these files for deployment
Heroku automatically calls collectstatic and prepares your static files for use by `WhiteNoise` after it uploads your application.

#### Create the heroku app and upload the django project
- `heroku create <appname>` if no appname is specified heroku will  assign a random name
  - for an already existing heroku app to set the remote to the local repository use `heroku git:remote -a <appname>`
- (additional step - if there is need/feel to change the appname need to repoint the heroku git remote to a different one) 
  - `heroku apps:rename <newappname>`
  - if appname already changed via web-ui then need to update the heroku remote URL `git remote set-url heroku <newurl>`
  - `heroku git:remote -a <appname> -r <remote>` 
- `git push heroku main` (push the app to heroku repository - this will upload the app, package it in dyno, run `collectstatic` and start the site) - point to note heroku will only deploy/consider code pushed to main branch, pushing code to another branch of `heroku remote` has no effect 
  - the above will push the command from your local repository main branch to your heroku remote 
  - if you want to deploy code to heroku from non-main branch of local repository use `git push heroku non-mainbranchname:main` to ensure it's pushed to remote main branch 
- for the first time to setup the database tables to be used by the applications need to perform the migrate operation `heroku run python manage.py migrate`
- create the administration superuser `heroku run python manage.py createsuperuser`
- to open the site/app `heroku open`

To reset/purge an apps Heroku git repository use `heroku-repo` plugin
`heroku plugins:install heroku repo`
`heroku repo:reset --app <appname>`

To get the list of addons and their price-tier and state(in our case heroku-postgresql database add-on) `heroku addons`

To check the configuration variables for the site `heroku config`

To set the configuration/environment variables to be used by the site `heroku config:set DJANGO_DEBUg=False`

To set the list of allowed hosts to determine where the application can run from update `settings.py` like - 
ALLOWED_HOSTS = ['<your app URL without the https:// prefix>.herokuapp.com','127.0.0.1']
```
# For example
# ALLOWED_HOSTS = ['app--djangoproject.herokuapp.com', '127.0.0.1']
```