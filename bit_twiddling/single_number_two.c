int singleNumber(int* nums, int numsSize) {
	int counts[32] = {0};

	for(int i = 0; i < numsSize; ++i) {
		for(int j = 0; j < 32; ++ j) {
			counts[j] += (nums[i] >> j) & 0x1; 
		}
	}

	int result = 0; 
	for(int i = 0; i < 32; ++i) {
		unsigned int bit = counts[i] % 3; 
		result |= (bit << i); 
	}

	return result; 
}
