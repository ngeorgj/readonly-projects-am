# readonly-projects-am
set all the projects as readonly after the migration.

requirements
`pip install requests`

change your credentials + base_url on `config.py`

run `main.py`

----

It will create a permission scheme that grants all permissions to `jira-administrators` and set that permission scheme to all server/dc projects.
