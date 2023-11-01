#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the single linked list
 * @number: number to be inserted in the sorted linked lists
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev, *node;

	if (!head || number)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	node = *head;
	while (node->next != NULL)
	{
		if (node->n < number)
		{
			prev = node;
			node = node->next;
			continue;
		}
		break;
	}
	if (prev)
	{
		prev->next = new;
		new->next = node;
		return (new);
	}
	if (node->n > number)
	{
		*head = new;
		new->next = node;
	}
	else
	{
		node->next = new;
	}
	return (new);
}
