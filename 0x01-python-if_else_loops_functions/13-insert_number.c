#include "lists.h"
#include <stdio.h>

/**
 * insert_node - function in C that inserts a number into a sorted
 * singly linked list
 * @head: a pointer to the head of the linked list
 * @number: the number needed to be into the new node
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}
	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	while (current)
	{
		if (number <= current->n)
		{
			new_node->next = current;
			*head = new_node;
			return (new_node);
		}
		if (number >= current->n && current->next == NULL)
		{
			new_node->next = NULL;
			current->next = new_node;
			return (new_node);
		}
		if (number >= current->n && number <= current->next->n)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}
	return (NULL);
}
