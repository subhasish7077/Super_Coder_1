#include <iostream>

using namespace std;

int main()
{
    string s = "";
    cout<< "Enter the message:- ";
    getline (cin, s);

    s = "git commit -m \"" + s +"\"";
    cout << s << endl;
    system("git add .");
    system(s.c_str());
    system("git push");

    return 0;
}