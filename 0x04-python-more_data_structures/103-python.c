#include <Python.h>
#include <stdio.h>
#include <string.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to pyobject
 */
void print_python_list(PyObject *p)
{
	PyListObject *my_list = (PyListObject *) p;
	long long x = -1, len = (long long) PyList_Size(p);
	const char *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lld\n", len);
	printf("[*] Allocated = %lld\n", (long long) my_list->allocated);
	while (++x < len)
	{
		item = my_list->ob_item[x]->ob_type->tp_name;
		printf("Element %lld: %s\n", x, item);
		if (strcmp(item, "bytes") == 0)
			print_python_bytes(my_list->ob_item[x]);
	}
}


/**
 * print_python_bytes - print some basic info about Python bytes objects.
 * @p: pointer to pyobject
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *p_byte = (PyBytesObject *) p;
	int len = PyBytes_Size(p);
	char *pointri = bytes->ob_sval;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %d\n", len);
	printf("trying string: %s\n", p_byte->ob_sval)
	len++;
	if (len > 10)
		len = 10;
	printf("  first %d bytes:", len);
	while (len--)
		printf(" %.2x", (unsigned char) *pointr++);
	printf("\n");
}
