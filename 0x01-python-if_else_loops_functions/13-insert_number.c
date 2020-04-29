#include "lists.h"
#include "stdlib.h"

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *temp;
  listint_t *temp2 = head;

  if (head == NULL)
    return (NULL);
  temp->next = NULL;
  temp->n = number;
  while (temp2)
    {
      if (temp2->next == NULL)
	break;
      temp2 = temp2->next;
    }
  temp2->next = temp;
  head = temp2;
  return (head);
}
