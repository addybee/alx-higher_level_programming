#include <Python.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"
/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to pyobject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len = PyList_Size(p);
	PyListObject *my_list = (PyListObject *) p;
	PyObject *item;
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", my_list->allocated);
	for (i = 0; i < len; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (strcmp(item->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - print some basic info about Python bytes objects.
 * @p: pointer to pyobject
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *ptr_ob;
	int i = 0;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes_ob = (PyBytesObject *) p;
	printf("  size: %li\n", ptr_ob->ob_base.ob_size);
	printf("  trying string: %s\n", ptr_ob->ob_sval);
	printf("  first %li bytes: ", ptr_ob->ob_base.ob_size < 10 ?
			ptr_ob->ob_base.ob_size + 1 : 10);
	while (ptr_ob->ob_sval[i] != '\0' && i < 9)
	{
		printf("%02x ", ptr_ob->ob_sval[i]);
		i++;
	}
	printf("%02x", ptr_ob->ob_sval[i]);
	printf("\n");
}
