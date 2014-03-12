#include "nqueens.h"

#include "sat.h"
#include <iostream>


int NQueens::q(int r, int c)
{
	return r * N + c + 1;
}

std::vector<NQueens::Queen> NQueens::solve(int NN)
{
	N = NN;
	sat::SatSolver solver;
	sat::DimacsWriter w("nqueens_cnf_in.txt");

	// v kazdom riadku aspon jedna
	for(int r = 0; r < N; ++r) {
		for(int c = 0; c < N; ++c) {
			w.writeLiteral(q(r,c));
		}
		w.finishClause();
	}

	// v kazdom riadku nie su dve
	for(int r = 0; r < N; ++r)
		for(int c1 = 0; c1 < N; ++c1)
			for(int c2 = 0; c2 < c1; ++c2)
				w.writeImpl(q(r,c1), -q(r,c2));

	// v kazdom stlpci nie su dve
	for(int c = 0; c < N; ++c)
		for(int r1 = 0; r1 < N; ++r1)
			for(int r2 = 0; r2 < r1; ++r2)
				w.writeImpl(q(r1,c), -q(r2,c));


	// uhlopriecky
	for(int c1 = 0; c1 < N; ++c1)
		for(int c2 = 0; c2 < N; ++c2)
			for(int r1 = 0; r1 < N; ++r1)
				for(int r2 = 0; r2 < N; ++r2)
					if (q(r1,c1) != q(r2,c2))
						if ((r1+c1==r2+c2) || (r1+c2==r2+c1))
							w.writeImpl(q(r1,c1), -q(r2,c2));

	w.close();
	auto sol = solver.solve(&w, "nqueens_cnf_out.txt");


	std::vector<Queen> res;
	if (sol.sat) {
		for(int x : sol.vars) {
			if (x > 0) {
				x--;
				res.push_back(Queen{r: x / N, c: x % N});
			}
		}
	}
	return res;
}


int main()
{
	int N;
	std::cin >> N;

	NQueens nq;
	auto s = nq.solve(N);

	if (s.size() == 0) {
		std::cout << "Nema riesenie" << std::endl;
	}
	else {
		for(const auto q : s) {
			std::cout << q.r << " " << q.c << std::endl;
		}
	}
	return 0;
}
