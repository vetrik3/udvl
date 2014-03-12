#include <vector>

class NQueens
{
	int N = 0;
public:
	struct Queen { int r; int c; };

	int q(int r, int c);
	std::vector<Queen> solve(int NN);
};
