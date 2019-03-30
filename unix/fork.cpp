#include <stdio.h>
#include <unistd.h>
int main(){
    int count = 0;
    __pid_t pid= fork();
    if(pid < 0)
        printf("error in fork!\n");
    else if(pid == 0){
        count++;
        printf("child: count = %d\n",count);
    }
    else{
        count++;
        printf("father: count = %d\n",count);
    }
    return 0;
}