DOIT_CONFIG = {'default_tasks': ['updatebabel', 'babel', 'test', 'cleanup']}

def task_test():
    return {
            'actions': ['python3 -m unittest']
    }

def task_cleanup():
    return {
            'actions': ['rm po/lineq.pot',
                        'rm po/ru/LC_MESSAGES/prog.mo']
    }

def task_updatebabel():
    return {
            'actions': ['pybabel update -D prog -i po/prog.pot -d po -l ru'],
            'file_dep': ['prog.py'],
            'targets': ['po/ru/LC_MESSAGES/prog.po']
    }

def task_babel():
    return {
            'actions': ['pybabel compile -D prog -d po -l ru'],
            'file_dep': ['po/ru/LC_MESSAGES/prog.po'],
            'targets': ['po/ru/LC_MESSAGES/prog.mo']
    }


