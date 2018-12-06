#include <iostream>

using namespace std;

class Testconst
{
public:
    int a=0;
    const int b = 0;
    void test1(){}
    void test2()const{}
    void test_const() const
    {
        this->test2();
    }
    void test3()
    {
        int c = this->b + 1;
    }
};



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

int const_test()
{
    if(0){
    const int a = 0;
    int *p;
    p = const_cast<int*>(&a);
    (*p)++;
    cout << *p <<' '<< p << endl;
    cout << a <<' '<< *p << endl;
    cout<< (p == &a) <<endl;
    return 0;}
    if(0){int j;
        cin >>j;
        const int a = j;
        int &b = const_cast<int &>(a);
        b = 2;
        cout<< a << endl;}
    cout<<(0.1==0.1)<<endl;

}

int main()
{
//    inout();
//    ByteTest();
//    TransOfDecimal();
//    const_test();
    auto c = 1.0+1;
    int a = 0;
    cout << "Hello World!" << endl;
    return 0;
    //this is a re new test
}

