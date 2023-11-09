#include "lists.h"
#include <stdlib.h>
/**
 * free_dlistint - frees a dlistint_t list.
 * @head: pointer to the dlistint head
 * Return: nothing
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *temp;

	if (!head)
		return;
	temp = head;
	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}
