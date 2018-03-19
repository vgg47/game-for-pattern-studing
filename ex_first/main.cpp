#include <iostream>
#include "/h/Factory_pers.h"

using namespace std;

int main() {
	unique_ptr<Knight> a = create_knight();
}