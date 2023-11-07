#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	unsigned int i, n = 0;
	int *item;

	if (!head)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	item = arr_listint(*head, &n);
	if (!item)
		return (0);
	for (i = 0; i < (n / 2); i++)
	{
		if (item[i] != item[n - 1 - i])
		{
			free(item);
			return (0);
		}
	}
	free(item);
	return (1);
}
/**
 * arr_listint - add the element of nodes of a listint_t list to an array
 * @h: pointer to head of list
 * @len: length of the array
 * Return: return the array
 */
int *arr_listint(const listint_t *h, unsigned int *len)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */
	int *item;

	current = h;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	item = (int *)malloc(n * sizeof(int));
	if (!item)
		return (NULL);
	current = h;
	*len = n;
	n = 0;
	while (current != NULL)
	{
		item[n] = current->n;
		current = current->next;
		n++;
	}
	return (item);
}
