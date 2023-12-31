#include <iostream>

auto main() -> int {
  int i = 0 , j  = 0;

  while ( i < 10) {
    i++;
    for (j = 0; j < 10; j++) {
      std::cout << i+j << " " << j << std::endl;
    }
  }
}
