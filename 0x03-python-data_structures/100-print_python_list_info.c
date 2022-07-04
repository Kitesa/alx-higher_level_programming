#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Prints some basic info about a Python
 * @p: a pointer to the python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t index, length;
	PyListObject *item;
	PyVarObject *o;
	l = (PyListObject *)p;
	o = (PyVarObject *)p;
	length = Py_SIZE(o);
	printf("[*] Size of the Python List = %1i\n", length);
	printf("[*] Allocated = %1i\n", 1->allocated);
	for (index = 0; index < length; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %1i: %s\n", index, Py_TYPE(item)->tp_name);
	}
}
