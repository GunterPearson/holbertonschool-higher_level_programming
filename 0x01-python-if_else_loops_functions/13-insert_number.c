#include "lists.h"
#include "stdio.h"
#include "stdlib.h"

/**
 * insert_node - inserts new node
 * @head: head of list given
 * @number: new number to be inserted
 *
 * Return: new list
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *first, *tmp, *second;

  first = malloc(sizeof(listint_t));

  if (head == NULL)
    return (NULL);
  tmp = *head;
  first->n = number;
  first->next = NULL;
  if (*head == NULL || tmp->n > number)
    {
      *head = first;
      first->next = tmp;
      return (*head);
    }
  while (tmp->next)
    {
      if (tmp->n < number && tmp->next->n < number)
	tmp = tmp->next;
      else
	{
	  second = tmp->next;
	  tmp->next = first;
	  first->next = second;
	  return (*head);
	}
    }
  tmp->next = first;
  return (*head);
}
