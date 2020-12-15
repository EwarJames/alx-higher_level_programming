#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *rev, *mid;
	size_t t = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	ptr = *head;
	while (ptr)
	{
		t++;
		ptr = tmp->next;
	}

	ptr = *head;
	for (i = 0; i < (t / 2) - 1; i++)
		ptr = tmp->next;

	if ((t % 2) == 0 && ptr->n != tmp->next->n)
		return (0);

	ptr = ptr->next->next;
	rev = reverse_listint(&ptr);
	mid = rev;

	ptr = *head;
	while (rev)
	{
		if (ptr->n != rev->n)
			return (0);
		ptr = ptr->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
