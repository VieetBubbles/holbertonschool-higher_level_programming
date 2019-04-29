#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly
 * linked list has a cycle in it.
 * @list: a pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p;
	listint_t *fast_p;

	slow_p = list;
	fast_p = list;

	/* Traverse linked list using two pointers */
	while(slow_p && fast_p && fast_p->next)
	{
		/* Move one pointer by one node */
		slow_p = slow_p->next;

		/* Move other pointer by two nodes */
		fast_p = fast_p->next->next;

		/*  If these pointers meet at same node then there is a loop */
		/* If pointers do not meet then linked list doesn’t have loop */
		if (slow_p == fast_p)
		{
			return (1);
		}
	}
	return (0);
}
