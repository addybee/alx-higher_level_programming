#include "lists.h"
#define B_SIZE 1023
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{

	if (!head)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	if (pal_listint(*head))
		return (1);
	return (0);
}

/**
 * pal_listint - check if listint_t list with at least 2 node is a palindrone
 * @h: pointer to head of the list
 * Return: return the array
 */
int pal_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n, siz, i;
	int item[B_SIZE];
	int *ptr = item;

	siz = B_SIZE;
	current = h;
	n = 0;
	while (current != NULL)
	{
		ptr[n] = current->n;
		n++;
		if (n > siz)
		{
			siz *= 2;
			int *new = (int *)realloc(ptr, siz);

			if (!new)
				return (0);
			ptr = new;
		}
		current = current->next;
	}
	for (i = 0; i < (n / 2); i++)
	{
		if (ptr[i] != ptr[n - 1 - i])
		{
			if (n > B_SIZE)
				free(ptr);
			return (0);
		}
	}
	if (n > B_SIZE)
		free(ptr);
	return (1);
}
