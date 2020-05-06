#include "lists.h"

/**
 * is_palindrome - checks linked list for palindrome
 * @head: head of linked list
 *
 * Return: int of true or false
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0;
	listint_t *temp = (*head);

	i = temp->n;
	while (temp && temp->next)
	{
		temp = temp->next;
	}
	j = temp->n;
	if (i == j)
		return (1);
	return (0);
}
