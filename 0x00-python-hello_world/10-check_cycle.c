#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node, *n_node;

	if (list == NULL)
		return (0);
	else if (list->next == NULL)
		return (0);
	node = list->next;
	n_node = list->next->next;
	while (node && n_node && n_node->next)
	{
		if (node == n_node)
			return (1);
		node = node->next;
		n_node = n_node->next->next;
	}
	return (0);
}
