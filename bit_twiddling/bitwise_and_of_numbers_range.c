int solution1(int left, int right) {
	int shifts = 0; 
	while (right > left) {
		right >>= 1; 
		left >>= 1; 
		shifts++; 
	}

	return right << shifts; 
}

int solution2(int left, int right) {
	while (right > left) {right &= (right-1);}
	return right; 
}
