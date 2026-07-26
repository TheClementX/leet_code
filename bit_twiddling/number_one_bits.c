int hammingWeight(int n) {
	int mask1 = 0x55555555; 
	n = (n & mask1) + ((n >> 1) & mask1); 
	int mask2 = 0x33333333; 
	n = (n & mask2) + ((n >> 2) & mask2); 
	int mask3 = 0f0f0f0f; 
	n = (n & mask3) + ((n >> 4) & mask3); 
	int mask4 = 00ff00ff; 
	n = (n & mask4) + ((n >> 8) & mask4); 
	int mask5 = 0000ffff; 
	n = (n & mask5) + ((n >> 16) & mask5); 

	return n; 
}
