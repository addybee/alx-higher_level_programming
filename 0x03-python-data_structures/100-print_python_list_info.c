#include <Python.h>
#include <listobject.h>
#include <object.h>
#include "lists.h"
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pyobject list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_len = PyList_Size(p);;
	PyListObject *my_list = (PyListObject *) p;
	int i;

	printf("[*] Size of the Python List = %li\n", list_len);
	printf("[*] Allocated = %li\n", my_list->allocated);
	for (i = 0; i < list_len; i++)
		printf("Element %d: %s\n", i, PyList_GET_ITEM(p, i)->ob_type->tp_name);
}
