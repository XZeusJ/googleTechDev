#include <vector> 
#include <stdlib.h>
#include <iostream>

template<typename T>
class Matrix {
	public:
		void resize(int rows, int cols) {
			data_.resize(rows * cols);
			rows_ = rows;
			cols_ = cols;
		}

		// T& is a function which returns a reference to an object of type T. This is called "return by reference" and means that the object returned is not copied Instead, you simply return a reference to its location in memory, through which the original object can be accessed. When using this, care has to be taken that the returned reference isn't used beyond the lifetime of the object to which it refers.
		// A reference is essentially an alias which is used to refer to some variable. It's often used as a safer alternative to a pointer, though unlike a pointer it is itself not an object, and you can never refer to the reference itself, and hence cannot change what it refers to.
		T& at(int row, int col) {
			// returns a reference to the element at position n in the vector.
			return data_.at(row * cols_ + col); 
		}
		int rows() const { return rows_; }
		int cols() const { return cols_; }

	private:
		std::vector<T> data_; // vector is a dynamic array which can store any types
		int rows_ = 0;
		int cols_ = 0;
};

constexpr int kMine = 9;
using std::min;
using std::max;

class MineField {
	private:
		struct Cell {
			int value = 0;
			bool visible = false;
		};
		Matrix<Cell> field;

	public:
		MineField(int rows, int cols, int num_mines) {
			field.resize(rows, cols);
			int mines_placed = 0;
			while (mines_placed < num_mines) { // generate field which has some mines
				int row = rand() % rows;
				int col = rand() % cols;
				// if the place already has mine, then pass current loop
				if (field.at(row, col).value == kMine) { continue; }
				// else we generate new mine which set the place value kMine
				// and increase surrounding places' value;
				mines_placed++;

				//A common error is to struggle to see the structure of the problem and make gigantic if clauses when looking at neighboring fields, instead of writing a simple for loop.
				// elegant realization
				for (int i = max(0, row-1); i <= min(rows-1, row+1); ++i) { 
					for (int j = max(0, col-1); j <= min(cols-1, col + 1); ++j) {
						if (i == row && j == col) { field.at(i, j).value = kMine; }
						else if (field.at(i, j).value != kMine) {
							field.at(i, j).value++;
						}
					}
				}
			}
		}

		bool OnClick(int row, int col) {
			if (row < 0 || row >= field.rows() || col < 0 || col >= field.cols()) {
				return false;
			}
			// if the cell already clicked, then we do nothing
			if (field.at(row, col).visible) { return false; }
			field.at(row, col).visible = true;
			if (field.at(row, col).value == kMine) {
				std::cout << "BOOM!" << std::endl << std::endl;
				return true;
			}
			// Exposing a zero means that there are no adjacent mines, so exposing all adjacent squares is guaranteed safe. As a convenience to the player, the game continues to expose adjacent squares until a non-zero square is reached.
			if (field.at(row, col).value != 0) { return false; }
			OnClick(row - 1, col);
			OnClick(row + 1, col);
			OnClick(row, col - 1);
			OnClick(row, col + 1);
			return false;
		}

		void Print(bool show_hidden) {
			for (int i = 0; i < field.rows(); ++i) {
				for (int j = 0; j < field.cols(); ++j) {
					if (field.at(i, j).visible || show_hidden) {
						std::cout << field.at(i, j).value << " ";
					} else {
						std::cout << ". ";
					}
				}
				std::cout << std::endl;
			}
			std::cout << std::endl;
		}

};

int main() {
	//因为默认情况下随机数种子为1，而相同的随机数种子产生的随机数是一样的,失去了随机性的意义，所以为使每次得到的随机数不一样，用函数srand()初始化随机数种子。srand()的参数，用time函数值（即当前时间），因为两次调用rand()函数的时间通常是不同的，这样就可以保证随机性了。
	srand(1);
	MineField mine_field(10, 10, 7);
	mine_field.Print(true);
	mine_field.OnClick(5, 1);
	mine_field.Print(false);
	mine_field.OnClick(2, 6);
	mine_field.Print(false);
	mine_field.OnClick(9, 3);
	mine_field.Print(false);
	mine_field.OnClick(0, 0);
	mine_field.Print(false);
	mine_field.OnClick(3, 5);
	mine_field.Print(false);
	return 0;
}