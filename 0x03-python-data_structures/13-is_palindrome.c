#include "lists.h"
#include <stdlib.h>
/**
 *reverse_listint - reverses a listint_t linked list.
 *
 *@head: headr pointer
 *
 *Return: return reverse listint
*/
listint_t *reverse_listint(listint_t **head)
{
listint_t *current = *head;
listint_t *prev = NULL;

if (*head == NULL)
return (NULL);

while (*head != NULL)
{
current = (*head)->next;
(*head)->next = prev;
prev = *head;
(*head) = current;
}
*head = prev;
return (*head);
}
/**
 *is_palindrome - check if linked list is palindrome or not
 *
 *@head: pointer to pointer to head of linkedlist
 *
 *Return: 1 if palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
const listint_t *current, *temp;
listint_t *reversed_linkedlist = reverse_listint(head);
current = *head;
temp = reversed_linkedlist;
while (current != NULL)
{
if (temp->n != current->n)
{
return (0);
}
current = current->next;
temp = temp->next;
}
return (1);
}

