#include<stdio.h>
#include<math>

#define M 3	//约束个数
#define N 5	//变量个数

//Z=CX
//AX=b

float A[M][N]={0};	//约束系数矩阵
float z=0;			//目标函数值
float C[N]={0};		//目标函数系数向量
float X[N]={0};		//变量取值
float b[M]={0};		//约束常数向量
float B[M]={0};		//哪些列是基、每个元素都是列数，从0
float CB[M]={0};	//记录基变量对应的优化函数系数
float delta[M]={0};	//检验数向量
float theta[M]={0};	//出基变量的确认

void make_RE(float A[M][N],float b[M],float B[M]){
	for(int i=0;i<M;i++){
		if(A[i][i]!=1){
			
		}
	}
}


