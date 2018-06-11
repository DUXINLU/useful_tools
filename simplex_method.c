#include<stdio.h>
#define LM 3
#define LN 5

int get_leave(int A[][LN], int b[], int C[], int Xn[], int Xb[]) {
	int delta[LN-LM];
	for (int i = 0; i < LN-LM; i++) {
		int _ = 0;
		for (int j = 0; j < LM; j++) {
			_ += A[j][Xn[i]] * C[Xb[j]];
		}
		delta[i] = C[Xn[i]] - _;
	}
	int _ = -1;
	int max = 0;
	for (int i = 0; i < LN - LM; i++) {
		if (max < delta[i]) {
			max = delta[i];
			_ = Xn[i];
		}
	}
	if (_ == -1) {//所有检验数全部小于零，达到最优解
		return -1;
	}
	return _;//返回最大检验数所在的列，即出基变量列数
}

int main() {
	int A[LM][LN] = { { 1,1,1,0,0 },{ 2,1,0,1,0 },{ 1,0,0,0,1 } };
	int b[LM] = { 8,10,4 };
	int C[LN] = { 8,6,0,0,0 };
	int Xb[LM] = { 2,3,4 };
	int Xn[LN-LM] = { 0,1 };
	int a;

	a=get_leave(A, b, C, Xn, Xb);

	printf("%d\n", a);

	getchar();
	return 0;
}
