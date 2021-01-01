#include <iostream>

int main()
{
	int x = 99;
	std::string bottle = "bottles";

	while (x > 0) {
		std::cout << x << ' ' << bottle << " of beer on the wall, "
			<< x << ' ' << bottle << " of beer.\nTake one down, pass it around,\n";
		x--;
		if (x == 1) bottle = "bottle";

		std::cout << x << ' ' << bottle << " of beer on the wall\n\n";
	}

	std::cout << "No more bottle of beer on the wall, no more bottle of beer."
		<< "\nGo to the store and buy some more, 99 bottles of beer on the wall.";
}
