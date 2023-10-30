#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - loop
 *
 * Description: loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Write a C program that creates 5 zombie processes.
 *
 * Description: For every zombie process created, it
 * displays Zombie process created, PID: ZOMBIE_PID
 *
 * Return: 0
 */

int main(void)
{
	pid_t zombie_pid;
	int k;

	for (k = 0; k < 5; k++)
	{
		zombie_pid = fork();
		if (zombie_pid > 0)
			printf("Zombie process created, PID: %d\n", zombie_pid);
		else
			exit(0);
	}

	infinite_while();

	return (0);
}
