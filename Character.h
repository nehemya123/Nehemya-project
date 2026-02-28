#ifndef CHARACTER_H_
#define CHARACTER_H_

#include <string>
#include <memory>

class Character {
    public: 
       character { const std::string& name, int health}
     virtual ~Character(); 
     virtual void attack() = 0;
     virtual void defend() = 0;
     virtual void Specialability() = 0 ;
     virtual void displaystatus();

     bool isAlive() const ;
     const std:: string& GetName() const;
     int getHealth();

    
    protected:
      std:: string& name;
      int health;
};
#endif