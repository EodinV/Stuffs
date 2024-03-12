#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;


string filename;
string txt = ".txt";
char hello[];
float a = 0;
float b = 0;
float sum;

int main()
{
    float a = 0;
    float b = 0;
    float sum, mult, subt, subt2, div, div2, high, low, sqrt;    
    cout << "Hello! What is your name?" << endl;
    cin >> hello;
    cout << "Type a number" << endl;
    cin >> a;
    cout << "another please" << endl;
    cin >> b;
    sum = a + b;
    mult = a * b;
    subt = a - b;
    subt2 = b - a;
    div = a / b;
    div2 = b / a;
    high = fmax(a, b);
    low = fmin(a, b);
    sqrt = hypot(a, b);
    
    filename = hello + txt;
    ofstream File(filename);

    cout << "Well ";
    cout << hello;
    cout << "... The sum of your numbers is: ";
    cout << sum << endl;
    cout << "If you multiply them you get: ";
    cout << mult << endl;
    cout << "If you subtract the second from the first you get: ";
    cout << subt << endl;
    cout << "If you subtract the first from the second you get: ";
    cout << subt2 << endl;
    cout << "If you divide the first by the second you get: ";
    cout << div << endl;
    cout << "If you divide the second by the first you get: ";
    cout << div2 << endl;

    File << "Subject Name:                  ";
    File << hello << endl;
    File << "Subjects 1st number:           ";
    File << a << endl;
    File << "Subjects 2nd number:           ";
    File << b << endl;
    File << "Subjects highest number:       ";
    File << high << endl;
    File << "Subjects lowest number:        ";
    File << low << endl;
    File << "Sum of the two:                ";
    File << sum << endl;
    File << "Multiplied:                    ";
    File << mult << endl;
    File << "First minus Second:            ";
    File << subt << endl;
    File << "Second minus First:            ";
    File << subt2 << endl;
    File << "First divided by Second:       ";
    File << div << endl;
    File << "Second divided by First:       ";
    File << div2 << endl;
    File << "Hypothenuse is:                ";
    File << sqrt << endl;




    
    return 0;
}