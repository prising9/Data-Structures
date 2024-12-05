#include <stdio.h>
#include <stdlib.h>

#define NUM_ROWS 3

// Illustrate Dynamic array allocation of multidimensional arrays
// Create a 2d ragged array and an array with same columns in each row
 int  main(int argc, char *argv[])
{
	int rowsize[NUM_ROWS] = {8, 4, 19};
	int rows, cols;

	printf("\nEnter the number of rows : ");
	scanf("%d", &rows);

	printf("\nEnter the number of cols : ");
	scanf("%d", &cols);

	int i,j;
	// create an array of 3 rows with 2 elems, 3, 4 elems respectively.

	int **ragged_arr = malloc(sizeof(*ragged_arr) * NUM_ROWS); // Necessary step
	int **even_arr = malloc(sizeof(*even_arr) * rows);

	printf("\nRagged array:");

	for (i=0;i<NUM_ROWS;i++) {
		ragged_arr[i] = malloc(rowsize[i] * sizeof(int));
	}

	for (i=0;i<NUM_ROWS;i++) {
		printf("\n");
		for (j=0;j<rowsize[i];j++) 
			printf(" %d ", ragged_arr[i][j]);
	}

	printf("\nEven array:");
	for (i=0;i<rows;i++) 
		even_arr[i] = malloc(cols * sizeof(int));

	for (i=0;i<rows;i++) {
		printf("\n");

		for (j=0;j<cols; j++) {
			printf("%d", even_arr[i][j]);
		}
	}
	printf("\n");
}