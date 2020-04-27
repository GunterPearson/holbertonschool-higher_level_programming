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

  if (list == NULL)
    return (0);
  while (head)
    {
      if (head->next >= head)
	return (1);
      head = head->next;
    }
  return (0);
}
