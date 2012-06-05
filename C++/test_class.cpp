#include <iostream>
#include <cstring>
#include <string>
using namespace std;

class Sup
{
    static inline string _IAmAString()
    {    // A static method is required to initialise a static string;
        // otherwise it would need to be initialised in the constructor.
        return string ("This is a string. It has letters that make up words.");
    }
    char* IAmAString;

public:
    Sup()
    {    // Allocate memory to the char pointer and copy the contents of the string object into it.
        int string_size =_IAmAString().size() + 1;  // Calculate string size.
        IAmAString = new char [string_size];  // Allocate enough memory to the pointer to copy the string.
        strncpy(IAmAString, _IAmAString().c_str(), string_size);  // Copy the string to the allocated char array.
    }

    ~Sup()
    {    // Free the allocated memory on destruction.
        delete [] IAmAString;
    }

    void OutputString()
    {    // Explicitly write the contents of the char array to stdout.
        cout << IAmAString;
    }
    char* ReturnString()
    {    // Return the address pointed to by the char pointer.
        return IAmAString;
    }
};

int main()
{
    Sup rawr;  // Create an object of class Sup, implicitly calling Sup's constructor.
    cout << rawr.ReturnString() << endl;  // Write the contents of the allocated array to stdout.
    return 0;  // Return from main, implicitly calling Sup's destructor and exiting the program.
}

