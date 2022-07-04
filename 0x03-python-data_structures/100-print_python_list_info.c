#include "Python.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;
	PyObject *object;
	struct _typeobject *type;

	if (strcmp(p->ob_typ->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Size of Python List = %ad\n", size);
		printf("[*] Allocated = %1d\n", list->allocated);
		for (i = 0; i < size; i++)
		{
			object = list->ob_item[i];
			type = object->ob_type;
			printf("Element %1d: %1d: %s\n", i, type->tp_name);
		}
	}
}
