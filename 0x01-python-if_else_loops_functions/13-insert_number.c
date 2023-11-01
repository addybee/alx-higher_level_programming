#include "lists.h"
#include <stdio.h>
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
	listint_t *new, *node, *prev;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	prev = *head;
	node = (*head)->next;
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
	if (node->n > number)
	{
		prev->next = new;
		new->next = node;
	}
	else
	{
		node->next = new;
	}
	return (new);
}
