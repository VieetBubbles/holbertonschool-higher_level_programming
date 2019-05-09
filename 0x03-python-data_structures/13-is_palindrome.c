#include "lists.h"

/**
 * reverse_ll - function that reverse a linked list
 * @head: a pointer to the head of a linked list
 *
 * Return: the reverse linked list
 */

listint_t *reverse_ll(listint_t **head)
{
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome -  function in C that checks if a singly linked
 * list is a palindrome
 * @head: a pointer to the head of a linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *reverse;

	if (!head)
		return (1);

	/* Go to the middle of the linked list if even */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/* Go to the middle if the linked list is not even */
	if (fast)
	{
		slow = slow->next;
	}
	/* reset the original list to the start */
	fast = *head;

	/* Had help from John and Tu for this part */
	/* reverse half of the linked list */
	reverse = reverse_ll(&slow);

	while (slow)
	{
		if (fast->n != slow->n)
		{
			reverse_ll(&reverse);
			return (0);
		}
		slow = slow->next;
		fast = fast->next;
	}
	reverse_ll(&reverse);
	return (1);
}
