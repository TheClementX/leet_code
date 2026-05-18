#include <stdint> 
#include <stdio> 

int reverseBits(int n) {
    uint32_t nu = (uint32_t)n;
    nu = (((nu & 0x55555555) << 1) | ((nu & 0xAAAAAAAA) >> 1));
    nu = (((nu & 0x33333333) << 2) | ((nu & 0xCCCCCCCC) >> 2));
    nu = (((nu & 0x0F0F0F0F) << 4) | ((nu & 0xF0F0F0F0) >> 4));
    nu = (((nu & 0x00FF00FF) << 8) | ((nu & 0xFF00FF00) >> 8));
    nu = (((nu & 0x0000FFFF) << 16) | ((nu & 0xFFFF0000) >> 16));

    return (int)nu;
}

int main(int argc, char *argv[]) { 
	
	return 0; 
}
