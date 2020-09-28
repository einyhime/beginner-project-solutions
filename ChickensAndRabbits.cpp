#include <iostream>

int main()
{
    int heads = 35;
    int legs = 94;
    int chicken = heads - 1;
    int rabbit = 1;

    std::cout << "Heads\t: " << heads;
    std::cout << "\nLegs\t: " << legs;

    for (int x = 0; x < heads; x++)
    {
        if (2 * chicken + 4 * rabbit == legs)
        {
            std::cout << "\nChickens: " << chicken;
            std::cout << "\nRabbits\t: " << rabbit;
            break;
        }
        chicken--;
        rabbit++;
    }
}
