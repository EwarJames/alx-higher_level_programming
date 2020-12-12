#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *temp;

	if (list == NULL || list->next == NULL)
		return (0);

	ptr = list->next;
	temp = list->next->next;

	while (ptr && temp && temp->next)
	{
		if (ptr == temp)
			return (1);

		ptr = ptr->next;
		temp = temp->next->next;
	}

	return (0);
}
