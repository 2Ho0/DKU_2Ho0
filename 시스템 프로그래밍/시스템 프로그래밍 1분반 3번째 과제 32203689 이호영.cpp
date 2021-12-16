/*file copy.c, by Ho yeoung, mwilliam55@naver.com*/
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/stat.h>
#define MAX_BUF 64

int main(int argc, char *argv[]){
        int fd,fd1,read_size;
        char buf[MAX_BUF];
        struct stat sb;

        if (argc != 3){
                printf("copyfile [source filename] [output filename]\n");
                exit(-1);
        }
        fd = open(argv[1],O_RDONLY);
        stat(argv[1],&sb);
        fd1 = open(argv[2],O_RDWR | O_CREAT | O_EXCL,sb.st_mode);


        while(1){
                read_size = read(fd,buf,MAX_BUF);
                if(read_size == 0)
                        break;
                write(fd1,buf,read_size);
        }
        close(fd);
        close(fd1);
}
