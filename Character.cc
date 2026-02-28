#include "Character.h"
#include <iostream> 
using namespace std;

character :: character( const string& name, int health) 
: name(name),health(health) {}

 character::~character() {}
 void character :: displaystatus() const {
    cout << name << " |HP: " << health << "\n";
 }
 bool character :: isAlive() const {
    return  health > 0 ;
 }
  const std::string& character :: name () const { return name; }
  int character :: getHealth() const { return health; }
  