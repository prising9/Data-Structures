
#include<stdio.h>
#include<string.h>

#define FRAME_HEADER_LEN 2
typedef char uint8_t;

const uint8_t SOF[FRAME_HEADER_LEN] = {0xAB, 0xCD};

#define MAX_FRAME_SIZE 1500

// return position of SOF in a stream
int start_of_frame(uint8_t *frame, int len)
{
	int i=0;
	while (i < len-2) {
		if(memcmp(&frame[i], SOF, FRAME_HEADER_LEN) == 0) {
				return(i);
		}
		i ++;
	}
	return(-1);
}
int main() 
{
	uint8_t frame[] = {0xFF, 0xCC, 0x34, 0xAB, 0xCD, 0xAB, 0xEF, 0xFF, 0xCC, 0x34, 0xAB};

	printf("The start of frame is at position %d\n", start_of_frame(frame, 11));

}

