#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node;

	if (list == NULL)
		return (0);
	else if (list->next == NULL)
		return (0);
	node = list->next;
	while (node && node->next)
	{
		if (node == list || node->next == node)
			return (1);
		node = node->next;
	}
	return (0);
}
