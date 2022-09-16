// Importing the required libraries
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
// Linux specific library
// I am using this as I am running my code in linux subsystems
// Ref:https://www.youtube.com/watch?v=aKKdiqVHNqw&t=0s

// Open F.
// Read the sequence number N from the file.
// Close F.
// Output N and the process' PID (either on screen or test file).
// Increment N by 1
// Open F.
// Write N to F.
// Flush F.
// Close F.

// Creating a pointer for input file
// named the file input.txt
// Creating a method

void write_to_txt_file(int num)
{

   FILE *fptr = fopen("program.txt", "w");
   num++;
   printf("updated value of n is : %d", N);
   putw(num, fptr);
   fflush(fptr);
   fclose(fptr);
}

int read_from_text_file(){
   int num = 0;
   FILE *fptr = fopen("program.txt", "r");

   fscanf(fptr, "%d", &num);
   num = 5;

   printf("\n\nValue of n=%d\n\n", num);
   fclose(fptr);

   return num;
}

int process()
{
   int pid;
   FILE *fptr = fopen("program.txt", "r");
   int N = 0;
   N = read_from_text_file();
   printf("\n\nN: %d Process ID: %d\n\n", N, pid);
   write_to_txt_file(N);
   return 1;
}
// read from txt file
//  ref:https://www.programiz.com/c-programming/c-file-input-output

// ref:https://www.programiz.com/c-programming/c-file-input-output
int create_and_write_to_txt_file()
{
   int num = 10;
   FILE *fptr;

   fptr = fopen("program.txt", "w");

   if (fptr == NULL)
   {
      printf("\n\nError!\n\n");
      exit(1);
   }

   printf("Enter num:");
   scanf("%d", &num);

   fprintf(fptr, "%d", num);
   fclose(fptr);
   return 0;
}

int main()
{
   create_and_write_to_txt_file();
   int num = read_from_text_file();
   printf("\n\nThe initial value read from file is %d", num);

   int fork_id = 0;
   fork_id = fork();
   // once the fork() method is called everything from that line is going to be executed parallelly. which means that there were 2 process running.
   //  1)main process 2)child process
   //  child process is always going to return 0
   //  now as we have called the fork function
   //  every line from here on is going to be executed twice
   //  each and every time we create a child process

   // if we have n fork statements in the program then we gona have 2**n process

   // checking if the process is main process or child process
   if (fork_id == 0)
   {
      printf("\n\nprocess p1 started\n\n");
      int prc1 = process();
   }
   int fork_id1 = 0;
   fork_id1 = fork();
   // checking if the process is main process or child process
   if (fork_id1 == 0)
   {
      printf("\n\nprocess p2  started\n\n");
      int prc2 = process();
   }
   int fork_id2 = 0;
   fork_id2 = fork();
   // checking if the process is main process or child process

   if (fork_id2 == 0)
   {
      printf("\n\nprocess p3 started\n\n");
      int prc3 = process();
   }
   return 0;
}
