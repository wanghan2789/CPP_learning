#include <iostream>

using namespace std;

int inout()
{
    //this is a iostream practice
    int a,b;
    cin >> a >> b;
    cout << a << ' ' << b << endl;
    return 0;
}

int ByteTest()
{
    short s_max = SHRT_MAX;
    int i_max = INT_MAX;
    long l_max = LONG_MAX;
    long long ll_max = LLONG_MAX;
    cout << sizeof(s_max) << endl;
    cout << sizeof(i_max) << endl;
    cout << sizeof(l_max) << endl;
    cout << sizeof(ll_max) << endl;
    return 0;
}

int TransOfDecimal()
{
    cout<<dec<<16<<endl;
    cout<<hex<<16<<endl;
    cout<<oct<<16<<endl;
    return 0;
}

int main()
{
//    inout();
//    ByteTest();
    TransOfDecimal();
    int a = 0;
    cout << "Hello World!" << endl;
    return 0;
    //this is a re new test
}

