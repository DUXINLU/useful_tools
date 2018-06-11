#include<stdio.h>
#define LM 3
#define LN 5

int get_enter() {
	return 0;
}

void show_matrix(float * A, float *b) {
	for (int i = 0; i < LM; i++) {//输出转化后矩阵 与 右端向量
	for (int j = 0; j < LN; j++) {
	printf("%.1f\t", *(A + i*LN + j));
	}
	printf("%.1f", *(b + i));
	printf("\n");
	}
	printf("\n");
}

//将A[row][col]所在列 以A[row][col]为主元素 对A做初等行变换 化为单位向量
void make_unit_vector(float * A, float * b, int row, int col) {
	float _ = *(A + row*LN + col);//主元素
	for (int i = 0; i < LN; i++) {//主元素变1 主元素所在行同时变化
		*(A + row*LN + i) /= _;
		printf("%.1f ", *(A + row*LN + i));
	}
	printf("\n\n");
	*(b + row) /= _;//主元素所在行的右端向量变化
	for (int i = 0; i < LM; i++) {//对每行 减去__倍的主元素行
		if (i == row) { continue; }
		int __ = *(A + i*LN + col);
		if (__ == 0) { continue; }//是零  这行就不用算了
		for (int j = 0; j < LN; j++) {
			*(A + i*LN + j) -= __*(*(A + row*LN + j));
		}
		*(b + i) -= __*(*b + row);
	}
}

//可以优化成指针调用 节省内存
int get_leave(float A[][LN], float b[], int C[], int Xn[], int Xb[]) {
	float delta[LN - LM];
	for (int i = 0; i < LN - LM; i++) {
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
	float A[LM][LN] = { { 1,1,1,0,0 },{ 2,1,0,1,0 },{ 1,0,0,0,1 } };
	float b[LM] = { 8,10,4 };
	int C[LN] = { 8,6,0,0,0 };
	int Xb[LM] = { 2,3,4 };
	int Xn[LN - LM] = { 0,1 };
	int leave;

	//leave = get_leave(A, b, C, Xn, Xb);//测试通过

	//make_unit_vector(A[0], b, 0, 0);//测试通过

	getchar();
	return 0;
}
