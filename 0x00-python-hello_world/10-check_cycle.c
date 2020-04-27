#include "lists.h"
/**
 * check_cycle - checks if link list is in loop
 * @list: starting point
 *
 * Return: int on success or fail
 */
int check_cycle(listint_t *list)
{
  listint_t *head = list;
  listint_t *temp;

  if (list == NULL)
    return (0);
  while (list)
    {
      temp = list->next;
      if (temp == head)
	return (1);
      list = list->next;
    }
  return (0);
}
