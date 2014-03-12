#include <vector>


class SudokuSolverInterface
{
public:
	typedef std::vector<std::vector<int> > Sudoku;

	/**
	 * Vyriesi sudoku pomocou SAT solvera.
	 *
	 * @param sudoku zadanie sudoku, obsahuje nuly na prazdnych miestach
	 * @return vyriesene sudoku alebo 9x9 nul, ak nema riesenie
	 */
	virtual Sudoku solve(const Sudoku &sudoku) = 0;
};
