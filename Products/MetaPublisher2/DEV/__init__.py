from Products.MetaPublisher2.library import DTMLFile


class DEV:
    """Development Mix-In Class"""

    manage_options = (
        {'label': "Tasks", 'action': 'DEV_tasks_form'},
        {'label': "Comments", 'action': 'DEV_comments_form'},
        {'label': "To Do's", 'action': 'DEV_todos_form'},
        {'label': "Images", 'action': 'DEV_images_form'},
    )

    DEV_images_form = DTMLFile('images', globals())
    DEV_tasks_form = DTMLFile('tasks', globals())
    DEV_comments_form = DTMLFile('comments', globals())
    DEV_todos_form = DTMLFile('todos', globals())

    def DEV_list_product_images(self):
        """Return a list of product imagery"""

        keys = map(lambda key: 'PROD ' + key, self.misc_.MetaPublisher2._d.keys())
        for key in dir(self):
            if key.endswith('.png') or key.endswith('.gif') or key.endswith('.jpg'):
                keys.append('ATTR ' + key)
        keys.sort()
        return keys

    def _DEV_count_markers(self, order, marker):

        from Products.MetaPublisher2.library import basepath, isdir, join, listdir, split, splitext

        result = []
        total = 0
        todo = listdir(basepath)
        while todo:
            filename = todo.pop(0)
            if isdir(join(basepath, filename)):
                for x in listdir(join(basepath, filename)):
                    if not(x.startswith('_') and x != '__init__.py'):
                        todo.append(join(filename, x))
            elif splitext(filename)[1] in ['.conf', '.css', '.dtml', '.py', '.txt']:
                count = 0
                problems = []
                f = open(join(basepath, filename), 'r')
                for line in f.readlines():
                    if marker in line:
                        count = count + 1
                        problems.append(line)
                f.close()
                if count:
                    total = total + count
                    result.append({
                        'count': count,
                        'filename': split(filename)[1],
                        'path': filename,
                        'problems': problems,
                        'type': splitext(filename)[1],
                    })
        if order == 'count':
            def sort_result(x, y):
                return cmp(
                    (x['count'], x['path']),
                    (y['count'], y['path'])
                )
            result.sort(sort_result)
            result.reverse()
        elif order == 'filename':
            def sort_result(x, y):
                return cmp(
                    (x['filename'], x['path']),
                    (y['filename'], y['path'])
                )
            result.sort(sort_result)
        elif order == 'type':
            def sort_result(x, y):
                return cmp(
                    (x['type'], x['path']),
                    (y['type'], y['path'])
                )
            result.sort(sort_result)
        else:
            def sort_result(x, y):
                return cmp(
                    x['path'],
                    y['path']
                )
            result.sort(sort_result)
        result.append({
            'count': total,
            'filename': '',
            'path': 'TOTAL',
            'problems': [],
            'type': '',
        })
        return result

    def DEV_count_tasks(self, order='path'):
        """Return a list of all urgent tasks denoted by 3 exclamation marks."""

        return self._DEV_count_markers(order, '!' * 3)

    def DEV_count_uncomments(self, order='path'):
        """Return a list of all urgent tasks denoted by 3 exclamation marks."""

        return self._DEV_count_markers(order, '!' + 'TXT!')

    def DEV_count_todos(self, order='path'):
        """Return a list of all ToDo's."""

        return self._DEV_count_markers(order, 'T' + 'ODO')
