#include "lists.h"
#include <stdlib.h>

/**
 *is_palindrome - check if linked list is palindrome or not
 *
 *@head: pointer to pointer to head of linkedlist
 *
 *Return: 1 if palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
const listint_t *current;
unsigned int len; /* number of nodes */
int *array;
unsigned int i;

if (*head == NULL)
return (1);

current = *head;
len = 0;
while (current != NULL)
{
current = current->next;
len++;
}
array = malloc(sizeof(int) * len);
if (array == NULL)
return (0);
current = *head;
i = 0;
while (current != NULL)
{
array[i] = current->n;
current = current->next;
i += 1;
}
for (i = 0; i < len / 2; i++)
{
if (array[i] == array[len - 1 - i])
continue;
else
{
free(array);
return (0);
}
}
free(array);
return (1);
}
