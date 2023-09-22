#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int N, M;
	int shuffle1, shuffle2, tmp;
	int ary[100] = { 0 };

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		ary[i] = i + 1;
	}

	for (int j = 0; j < M; j++) {
		scanf("%d %d", &shuffle1, &shuffle2);
		for (int k = shuffle1; k <= shuffle2; k++) {
			tmp = ary[k-1];
			ary[k-1] = ary[shuffle2-1];
			ary[shuffle2-1] = tmp;
			shuffle2--;
		}
	}

	for (int l = 0; l < N; l++) {
		printf("%d ", ary[l]);
	}
	return 0;
}