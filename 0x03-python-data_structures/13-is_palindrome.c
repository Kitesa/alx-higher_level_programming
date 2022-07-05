#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to list
 * Return: 1 if palindrome 0 else
 */
int is_palindrome(listint_t **head)
{
	return (checkPalindrome(head, *head));
}

/**
 * checkPalindrome - recursive functionto check if singly linked list is pal
 * @headptr:double pointer to list
 * @tptr: pointer to the list
 *
 * Return: 1 or 0
 */
int checkPalindrome(listint_t **headptr, listint_t *tptr)
{
	int res;

	if (tptr == NULL)
		return (1);
	res = checkPalindrome(headptr, tptr->next) && ((*headptr)->n == tptr->n);
	return (res);
}
