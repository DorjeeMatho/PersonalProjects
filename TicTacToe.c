#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// declaring global variables
char board[3][3]; // 2d array
const char PLAYER = 'X';
const char COMPUTER = 'O';

void printWinner(char winner);
void resetBoard() {
  for (int i = 0; i < 3; i++) // for rows
  {
    for (int j = 0; j < 3; j++) // for columns
    {
      board[i][j] = ' '; // loops through every position in the board, and sets
                         // the position i, j to empty space
    }
  }
}
void printBoard() {
  printf(" %c | %c | %c", board[0][0], board[0][1], board[0][2]);
  printf("\n---|---|---\n");
  printf(" %c | %c | %c", board[1][0], board[1][1], board[1][2]);
  printf("\n---|---|---\n");
  printf(" %c | %c | %c", board[2][0], board[2][1], board[2][2]);
  printf("\n");
}

int checkFreeSpaces() // if freespaces = 0 then game is over
{
  int freeSpaces = 9;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (board[i][j] !=
          ' ') { // checking each i, j position to find number of free spaces
        freeSpaces--;
      }
    }
  }
  return freeSpaces;
}
void playerMove() {
  int x;
  int y;
  do {
    printf("Enter Row #(1-3)");
    scanf("%d", &x);
    x--; // user doesnt know arrays start with zero so decrement x
    printf("Enter column #(1-3)");
    scanf("%d", &y);
    y--;
    if (board[x][y] != ' ') {
      printf("invalid move\n");
    } else {
      board[x][y] = PLAYER;
      break;
    }
  } while (board[x][y] !=
           ' '); // loop will repeat till the player picks a empty spot
}

void computerMove() {
  // randomly generated position for computer
  //  so lets create a seed that does such
  srand(time(0));
  int x;
  int y;

  if (checkFreeSpaces() > 0) {
    do {
      x = rand() % 3;
      y = rand() % 3;
    } while (board[x][y] != ' '); // continue generating random numbers till
                                  // there is an open position
    board[x][y] = COMPUTER;
  } else {
    printWinner(' ');
  }
}
char checkWinner() {
  // check our rows
  for (int i = 0; i < 3; i++) {
    if (board[i][0] == board[i][1] && board[i][0] == board[i][2]) {
      return board[i][0];
    }
  }
  // lets check columns now
  for (int i = 0; i < 3; i++) {
    if (board[0][i] == board[1][i] && board[0][i] == board[2][i]) {
      return board[0][i];
    }
  }
  // check diagonals
  if (board[0][0] == board[1][1] && board[0][0] == board[2][2]) {
    return board[0][0];
  }
  if (board[0][2] == board[1][1] && board[0][2] == board[2][2]) {
    return board[0][2];
  }
  return ' ';
}

void printWinner(char winner) {
  if (winner == PLAYER) {
    printf("YOU WIN!\n");
  } else if (winner == COMPUTER) {
    printf("YOU LOSE! \n");
  } else {
    printf("DRAW!\n");
  }
}
int main(void) {
  char winner = ' ';
  resetBoard();
  while (winner == ' ' && checkFreeSpaces() != 0) {
    printBoard();
    playerMove();
    winner = checkWinner();
    if (winner != ' ' || checkFreeSpaces() == 0) {
      break;
    }
    computerMove();
    winner = checkWinner();
    if (winner != ' ' || checkFreeSpaces() == 0) {
      break;
    }
  }
  printBoard();
  printWinner(winner);

  return 0;
}
