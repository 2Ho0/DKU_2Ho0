/* file MyShell,by Ho yeoung, mwilliam55@naver.com*/
#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <stdbool.h>
#include <sys/wait.h>
#include <string.h>
#define MAX 128

bool my_tty(int argc, char*argv[]);
bool my_quit(int argc, char*argv[]);
bool my_cd(int argc, char*argv[]);
bool my_help(int argc, char *argv[]);
void my_red(int argc, char *argv[]);
void my_pipe(int argc, char *argv[]);
int my_cmd(char *line[]);
int tokenize(char *buf, char *delims, char *tokens[], int max);
bool run(char *line);


struct myshell {char *command; char *ce; bool (*call_func)(int argc, char *argv[]);};
struct myshell cmd[] = {
	{"help", "Show Command", my_help},
	{"cd", "Change Directory", my_cd},
	{"tty", "Show terminal's filename", my_tty},
	{"quit", "Quit MyShell", my_quit},
	{">", "Redirection"},
	{"&", "background processing"},
	{"|", "pipe "}
	
};
bool my_tty(int argc, char*argv[]){
	printf("current tty: %s\n", ttyname(0)); 
	return true;
}
bool my_quit(int argc, char*argv[]){
		return false;	
}
int main()
{
	char line[1024], cwd[MAX];// command와 파일 주소를 입력받을 배열 선언 
	getcwd(cwd, MAX); //현재 디렉터리 경로
	while (1)
	{
		printf("%s:~$ ",cwd);
		fgets(line, sizeof(line) - 1, stdin);// (line의 사이즈-1)만큼 표준입력
		if (run(line) == false)
			break;
	}
	return 0;
}

bool my_cd(int argc, char* argv[])// cd 명령어 함수
{
	if (argc == 1) //cd만 입력했을 경우
		chdir(getenv("HOME"));
	else if (argc == 2)
	{
		if (chdir(argv[1])) //폴더 변경
			printf("%s is no directory\n", argv[1]);
	}
	else printf("USAGE: %s [dir_name]\n", argv[0]);
	return true;
}

bool my_help(int argc, char *argv[]){//명령어 출력 함수
	int i;
	printf("------------------HELP_MENU--------------------\n");
	for(i=0; i<sizeof(cmd)/sizeof(cmd[0]); i++){
		printf("%s\t %s\n", cmd[i].command, cmd[i].ce);//쉘에서 명령어들 출력
	}
	printf("------------------------------------------------\n");

	return true;
}
void my_red(int argc, char *argv[]){//redirection 함수
	int fd;
	if(argc != 4){printf("USAGE: %s input > output\n", argv[0]);}//형식이 맞지 않을 때 형식을 알려줌
	if((fd = open(argv[3], O_WRONLY | O_CREAT, 0664)) < 0) { //argv[3]에 있는 파일을 오픈하고 파일이 없다면 생성
		printf("Can't open %s file with errno %d\n", argv[3], errno);
		return;
	}
	dup2(fd, STDOUT_FILENO); //터미널에서의 파일 출력을 fd로 보냄
	argv[2] = NULL;
	close(fd);
}

void my_pipe(int argc, char *argv[]){
	
	int  fd[2], read_size=0, old_stdin;
	char bufc[MAX], bufp[MAX],wc[MAX],cwd[MAX];
	
	old_stdin = dup(STDIN_FILENO); //표준 입력 사본 지정
	
	if(argc != 4){//형식이 맞지 않을 때 형식을 알려줌
		printf("USAGE: %s file_name | file_name\n", argv[0]);
		return;
	}
	if (pipe(fd)==-1){
		fprintf(stderr, "pipe error: %s\n", strerror(errno));
		return ;
	}
	pid_t pid = fork();
	if(pid==0){
		dup2(fd[1],1); //파일 출력을 자식 프로레스의 fd[1]으로 연결
		int ste = execlp(argv[3],argv[3],argv[1],NULL);//argv[3]의 명령어를 수행하고 인자로 argv[1]를 전달
		if (ste==-1){
			fprintf(stderr, "run error: %s\n", strerror(errno));
			return;
		}
	}
	dup2(fd[0],0);//파일 입력을 부모 프로세스의 fd[0]으로 연결
	char line[255];
	while(fgets(line,sizeof(line),stdin)!=0){
		printf("%s",line);//수행된 결과를 출력
	}
	dup2(old_stdin,STDIN_FILENO);//dup2를 이용하여 변경된 STDIN_FILENO를 원상복구 
	close(fd[0]);
	close(fd[1]);
	close(old_stdin);
	return ;
}


int my_cmd(char *line[]){
	int i;
	for(i=0; line[i] != NULL; i++){
		if(!strcmp(line[i], ">")) return 1; //리다이렉션인지 체크
		if(!strcmp(line[i], "|")) {line[i] = NULL; return 2;} //파이프인지 체크
		if(!strcmp(line[i], "&")) {line[i] = NULL; return 3;} //백 그라운드 프로레싱인지 체크
	}
	return 0;
}
int tokenize(char *buf, char *delims, char *tokens[], int max){
	int count = 0;
	char *token = strtok(buf, delims);
	while(token != NULL && count < max){
		tokens[count] = token;
		count++;
		token = strtok(NULL, delims);
	}
	tokens[count] = NULL; //NULL을 이용해서 tokens의 마지막을 알림
	return count;
}
bool run(char *line){
    char delims[] = " \n";
    char *tokens[MAX];
    pid_t pid;
    int i, check,stat;
	int token_count = tokenize(line, delims, tokens, sizeof(tokens) / sizeof(char*));
	if(token_count == 0) return true; //토큰이 비어있다면 리턴 true
	check = my_cmd(tokens); //명령어 체크
	for(i = 0; i < 4; i++) {
  	if(strcmp(cmd[i].command, tokens[0]) == 0) //구조체에 있는 명령어 확인
        	return cmd[i].call_func(token_count, tokens);// 구조체에 있는 명령어 실행
    }
	if((pid=fork()) < 0){ //fork 실패시 오류 메시지 출력
		perror("fork error caused\n"); exit(-1);
	}
	else if(pid == 0) {
		
		if(check == 1){ //리다이렉션 실행
		my_red(token_count, tokens);
		execvp(tokens[0], tokens);
		}
		else if(check == 2) my_pipe(token_count, tokens); //파이프 실행
		else{
			execvp(tokens[0], tokens);
			printf("execute failed\n"); //execvp 실패시 오류 메시지 출력
			exit(-1);
		}
	}
	else {
		if(check == 3) { //백그라운드 프로세싱
			waitpid(pid, &stat, WNOHANG);
			sleep(1);
		}
		else waitpid(pid,&stat, 0);
	}
	return true;
}