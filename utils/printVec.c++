#include <iostream>
using namespace std;
template <class T>
void printVec (vector<T> vec) {
  for (int i = 0; i < vec.size() - 1; i++) {
    cout << vec[i] << " ";
  }
  cout << vec[vec.size() - 1] << endl;
}
