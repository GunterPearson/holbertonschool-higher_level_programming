#include "lists.h"

/**
 * is_palindrome - checks linked list for palindrome
 * @head: head of linked list
 *
 * Return: int of true or false
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = (*head);
	int i = 0, j = 0, k = 0, l = 0;
	int list[20];

	while (temp->next)
	{
		list[i] = temp->n;
		temp = temp->next;
		i++;
		if (!temp->next)
			list[i] = temp->n;
	}
	i += 1;
	list[i] = '\0';
	while (list[j])
	{
		j++;
	}
	j = j - 1;
	l = j / 2;
	while (k <= l)
	{
		if (list[k] != list[j])
			return (0);
		k++;
		j--;
	}
	return (1);
}
