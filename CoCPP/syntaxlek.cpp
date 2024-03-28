#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;



string hello;
float a = 0;
float b = 0;
float sum;

<<<<<<< HEAD
<<<<<<< HEAD
=======
class User
{
private:
    string Name;
    float FirstNumber;
    float SecondNumber;
public:
    void setName(string name)
    {
        Name = name;
    }
    string getName()
    {
        return Name;
    }
    void setFirst(float a)
    {
        FirstNumber = a;
    }
    float getFirst()
    {
        return FirstNumber;
    }
    void setSecond(float b)
    {
        SecondNumber = b;
    }
    float getSecond()
    {
        return SecondNumber;
    }
};


>>>>>>> 2be87641143d8205f7ff665a16900dabeb57f26f
=======
>>>>>>> 96ae1d5acb33e2510e88768603d3588a7d7e99b0


float angle(float x, float y)
{
    float ans;
    float cal1 = (x / y);
    float rad = atan(cal1);
    ans = rad * 180 / 3.1415;
    return ans;
}

void fileMake(int type, string hello, float first, float second, float sum, float mult, float subt, float subt2, float div, float div2, float high, float low, float sqrt, float ang)
{
    string filename;
    string txt;

    if (type == 1)
    {
        txt = ".html";
    }
    if (type == 2)
    {
        txt = ".json";
    }
    if (type == 3)
    {
        txt = ".txt";
    }
    
    
    

    filename = hello + txt;
    ofstream File(filename);

    if (txt == ".html")
    {       
        File << "<!DOCTYPE html>" << endl;
        File << "<html lang=\"en\" dir=\"ltr\">" << endl;
        File << "   <head>" << endl;
        File << "       <meta charset=\"utf-8\">" << endl;
        File << "       <title>" << hello << "</title>" << endl;
        File << "       <link rel=\"icon\" href=\"https://media.istockphoto.com/id/1196385489/vector/red-rooster-cock-icon-logo-graphic.jpg?s=612x612&w=0&k=20&c=mUqHzg5U1Vk4Pn6xTx9A7Do2FQWBtgtuZBGTiGQ_jDw=\">" << endl;
        File << "   </head>" << endl;
        File << endl;
        File << "<dl class=\"\"" << endl;
        File << "   <dt>Subject Name:</dt>" << endl;
        File << "   <dd>" << hello << "</dd>" << endl;
        File << "   <dt>Subjects 1st number:</dt>" << endl;
        File << "   <dd>" << first << "</dd>" << endl;
        File << "   <dt>Subjects 2nd number:</dt>" << endl; 
        File << "   <dd>" << second << "</dd" << endl;
        File << "   <dt>Subjects highest number:</dt>" << endl;
        File << "   <dd>" << high << "</dd>" << endl;
        File << "   <dt>Subjects lowest number:</dt>" << endl;
        File << "   <dd>" << low << "</dd>" << endl;
        File << "   <dt>Sum of the two:</dt>" << endl;
        File << "   <dd>" << sum << "</dd>" << endl;
        File << "   <dt>Multiplied:</dt>" << endl;
        File << "   <dd>" << mult << "</dd>" << endl;
        File << "   <dt>First minus Second:</dt>" << endl;
        File << "   <dd>" << subt << "</dd>" << endl;
        File << "   <dt>Second minus First:</dt>" << endl;
        File << "   <dd>" << subt2 << "</dd>" << endl;
        File << "   <dt>First divided by Second:</dt>" << endl;
        File << "   <dd>" << div << "</dd>" << endl;
        File << "   <dt>Second divided by First:</dt>" << endl;
        File << "   <dd>" << div2 << "</dd>" << endl;
        File << "   <dt>Hypothenuse is:</dd>" << endl;
        File << "   <dd>" << sqrt << "</dd>" << endl;
        File << "   <dt>With the angle:</dt>" << endl;
        File << "   <dd>" << ang << "</dd>" << endl;
        File << "</html>" << endl;
    }

    if (txt == ".json")
    {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 96ae1d5acb33e2510e88768603d3588a7d7e99b0
        File << "{" << endl;
        File << "   \"File\": {" << endl;
        File << "       \"title\":\"example file\"," << endl;
        File << "       \"FileDiv\": {" << endl;
        File << "           \"Entries\":{" << endl;
        File << "               \"Subject\":" << "\"" << hello << "\"," << endl;
        File << "               \"First Num\":" << "\"" << first << "\"," << endl; 
        File << "               \"Second Num\":" << "\"" << second << "\"," << endl;
        File << "               \"Higher Num\":" << "\"" << high << "\"," << endl;
        File << "               \"Lower Num\":" << "\"" << low << "\"," << endl;
        File << "               \"Sum\":" << "\"" << sum << "\"," << endl;
        File << "               \"Multiplied\":" << "\"" << mult << "\"," << endl;
        File << "               \"1st minus 2nd\":" << "\"" << subt << "\"," << endl;
        File << "               \"2nd minus 1st\":" << "\"" << subt2 << "\"," << endl;
        File << "               \"Div 1st/2nd\":" << "\"" << div << "\"," << endl;
        File << "               \"Div 2nd/1st\":" << "\"" << div2 << "\"," << endl;
        File << "               \"Hypothenuse\":" << "\"" << sqrt << "\"," << endl;
        File << "               \"Angle\":" << "\"" << ang << "\"" << endl;
        File << "           }" << endl;
        File << "       }" << endl;
        File << "   }" << endl;
        File << "}" << endl;
<<<<<<< HEAD
=======
        File << "<!DOCTYPE html>" << endl;
        File << "<html lang=\"en\" dir=\"ltr\">" << endl;
        File << "   <head>" << endl;
        File << "       <meta charset=\"utf-8\">" << endl;
        File << "       <title>" << hello << "</title>" << endl;
        File << "       <link rel=\"icon\" href=\"https://media.istockphoto.com/id/1196385489/vector/red-rooster-cock-icon-logo-graphic.jpg?s=612x612&w=0&k=20&c=mUqHzg5U1Vk4Pn6xTx9A7Do2FQWBtgtuZBGTiGQ_jDw=\">" << endl;
        File << "   </head>" << endl;
        File << endl;
        File << "<dl class=\"\">" << endl;
        File << "   <dt>Subject Name:</dt>" << endl;
        File << "   <dd>" << hello << "</dd>" << endl;
        File << "   <dt>Subjects 1st number:</dt>" << endl;
        File << "   <dd>" << first << "</dd>" << endl;
        File << "   <dt>Subjects 2nd number:</dt>" << endl; 
        File << "   <dd>" << second << "</dd>" << endl;
        File << "   <dt>Subjects highest number:</dt>" << endl;
        File << "   <dd>" << high << "</dd>" << endl;
        File << "   <dt>Subjects lowest number:</dt>" << endl;
        File << "   <dd>" << low << "</dd>" << endl;
        File << "   <dt>Sum of the two:</dt>" << endl;
        File << "   <dd>" << sum << "</dd>" << endl;
        File << "   <dt>Multiplied:</dt>" << endl;
        File << "   <dd>" << mult << "</dd>" << endl;
        File << "   <dt>First minus Second:</dt>" << endl;
        File << "   <dd>" << subt << "</dd>" << endl;
        File << "   <dt>Second minus First:</dt>" << endl;
        File << "   <dd>" << subt2 << "</dd>" << endl;
        File << "   <dt>First divided by Second:</dt>" << endl;
        File << "   <dd>" << div << "</dd>" << endl;
        File << "   <dt>Second divided by First:</dt>" << endl;
        File << "   <dd>" << div2 << "</dd>" << endl;
        File << "   <dt>Hypothenuse is:</dd>" << endl;
        File << "   <dd>" << sqrt << "</dd>" << endl;
        File << "   <dt>With the angle:</dt>" << endl;
        File << "   <dd>" << ang << "</dd>" << endl;
        File << "</dl>" << endl;
        File << "</html>" << endl;
>>>>>>> 2be87641143d8205f7ff665a16900dabeb57f26f
=======
>>>>>>> 96ae1d5acb33e2510e88768603d3588a7d7e99b0
    }
    
    if (txt == ".txt")
    {
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
        File << "With the angle:                ";
        File << ang << endl;
    }
    
    
}


int main()
{
    bool cons;
    int type = 0;
    float a = 0;
    float b = 0;
    float sum, mult, subt, subt2, div, div2, high, low, sqrt, ang;    
    cout << "Hello! What is your name?" << endl;
    cin >> hello;
    cout << "Type a number" << endl;
    cin >> a;
    cout << "another please" << endl;
    cin >> b;
    cout << "What kind of file do you want?" << endl;
    cout << "       1: HTML" << endl;
    cout << "       2: JSON" << endl;
    cout << "       3: TXT" << endl;
    cin >> type;
    if (type < 1)
    {
        type = 1;
    }
    if (type > 3)
    {
        type = 3;
    }
    cout << "Do you want the numbers printed in the console?   y = 1 / n = 0" << endl;
    cin >> cons;
    
    
    sum = a + b;
    mult = a * b;
    subt = a - b;
    subt2 = b - a;
    div = a / b;
    div2 = b / a;
    high = fmax(a, b);
    low = fmin(a, b);
    sqrt = hypot(a, b);
    ang = angle(a, b);
    
    if (cons)
    {
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
    }
    

    

    fileMake(type, hello, a, b, sum, mult, subt, subt2, div, div2, high, low, sqrt, ang);




    
    return 0;
}
