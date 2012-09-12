# What is this?

This repository is a minimal Django app that illustrates a bug in pyjade template loaders.

# What is the bug?

When using Django's default template loaders, this code works fine:
(assume that `var = 'Foo'` and `exclude_list = ['']`)

    {% if not var in exclude_list %}
        Hello.
    {% endif %}

    {% if var in exclude_list %}
        This will not be printed.
    {% endif %}

However, when pyjade template loader is enabled, none of those if-statements is entered!
The only way to make it work is to rewrite the first `if` like this:

    {% if var not in exclude_list %}

(note the different position of `not`.)

# How to run this app?

These are the suggested steps:

    cd /tmp
    git clone git://github.com/siovene/pyjade-template-loader-bug.git
    cd pyjade-template-loader-bug
    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py runserver

Then visit http://localhost:8000/
