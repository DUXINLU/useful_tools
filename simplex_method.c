#include<stdio.h>

void get_leave(int A[][5], int b[], int C[], int Xn[], int Xb[]) {
	int delta[2];
	for (int i = 0; i < 2; i++) {
		int _ = 0;
		for (int j = 0; j < 3; j++) {
			_ += A[j][Xn[i]] * C[Xb[j]];
		}
		printf("_:%d\n", _);
		delta[i] = C[Xn[i]] - _;
		printf("%d\n", delta[i]);
	}
}

int main() {
	int A[3][5] = { {1,1,1,0,0},{2,1,0,1,0},{1,0,0,0,1} };
	int b[3] = { 8,10,4 };
	int C[5] = { 8,6,0,0,0 };
	int Xb[3] = { 2,3,4 };
	int Xn[2] = { 0,1 };

	get_leave(A, b, C, Xn,Xb);

	getchar();
	return 0;
}
