#include "lists.h"
/**
 * dlistint_len - count number of elements in a linked dlistint_t list.
 * @h: head of the linked dlistint_t list.
 * Return: number of elements in a linked dlistint_t list.
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t n = 0;
	const dlistint_t *temp = h;

	while (temp != NULL)
	{
		temp = temp->next;
		n++;
	}
	return (n);
}
