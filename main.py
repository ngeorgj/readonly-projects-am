from lib.functions import *

read_only_permission_scheme = create_read_only_permission_scheme()
projects = get_projects()

for project in projects:
    set_permission_scheme(read_only_permission_scheme['id'], project['key'])


