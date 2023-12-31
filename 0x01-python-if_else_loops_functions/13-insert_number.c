#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 *insert_node - insert node in sorted linked list
 *
 *@head: pointer to head
 *@number: number which is inserted
 *
 *Return: pointer to linked list
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *inserted;
listint_t *current;
listint_t *before;

before = *head;
current = *head;
inserted = malloc(sizeof(listint_t));
if (inserted == NULL)
return (NULL);

inserted->n = number;
if (*head == NULL)
*head = inserted;
else if ((*head)->n >= number)
{
inserted->next = *head;
*head = inserted;
}
else
{
while (current->next != NULL)
{
if (current->n >= number)
{
before->next = inserted;
inserted->next = current;
return (inserted); }
before = current;
current = current->next;
}
current->next = inserted;
inserted->next = NULL;
}
return (inserted);
}
