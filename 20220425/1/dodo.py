DOIT_CONFIG = {'default_tasks': ['updateTransl', 'tests', 'wheel', 'sdist']}


def task_cleanup():
    return {
        'actions': ['rm -rf po base.pot'],
    }


def task_createTransl():
    return {
        'actions': [
            'pybabel extract . -o base.pot',
            'pybabel init -l ru -i base.pot -d po'
        ],
        'targets': [
            'base.pot',
            'po/ru/LC_MESSAGES/messages.po'
        ]
    }


def task_updateTransl():
    return {
        'file_dep': ['base.pot', 'po/ru/LC_MESSAGES/messages.po'],
        'actions': [
            'pybabel update -i base.pot -d po',
            'pybabel compile -d po compiling catalog'
        ],
        'targets': ['po/ru/LC_MESSAGES/messages.mo']
    }


def task_tests():
    return {
        'actions': ['python3 -m unittest']
    }


def task_rebuild():
    return {
        'actions': [task_cleanup, task_createTransl, task_updateTransl]
    }

def task_wheel():
    return {
        'actions' : ['python3 -m build -w .']
    }

def task_sdist():
    return {
        'actions' : ['python3 -m build -s .']
    }
