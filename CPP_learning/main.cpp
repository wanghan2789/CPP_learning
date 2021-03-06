#include <iostream>
#include<cstring>
#include<string>
#include<vector>
#include<cmath>
#include<istream>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
using namespace std;

istream& TestPractice8(istream& in)
{
    //输入一个流的引用，遇到文件终止符结束
    //返回之前将流重置，使之有效
    string my_list;
    while(in>>my_list)
    {
        cout<<my_list<<endl;
    }
    in.clear();//流的置位
    return in;
}

class TestAgorithm
{
public:
    static bool my_judgefunc(const string &a, const string &b)
    {
        return a.size()>b.size();
    }
    void judge(vector<string>&a)
    {
//        int (C::* pfn1)(int) = &C::fun;
//        bool (TestAgorithm::*pftr)(string) = &TestAgorithm::my_judgefunc;
        sort(a.begin(), a.end(), my_judgefunc);
//        for(auto &in : a)
//        {
//            cout<< in<< endl;
//        }
        for_each(a.begin(), a.end(), [](const string s){cout<<s<<' ';});
        cout<<endl;
    }
};



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



class TestInitial
{

friend void see(TestInitial a);

public:
    int a;
    int b;

private:
    int my_secreat = 9;
};

void see(TestInitial a)
{
    cout<<a.my_secreat<<endl;
}

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

int arrlis()
{
    int a[10];
    cout<<a<<endl;
    return 0;
}

int firstconfirm()
{
    int a[10]{};
    auto b(a);
    cout<<(b==&a[0])<<endl;
    return 0;
}

int TestFor()
{
    int arr[2] = {0,1};
    for(int start: arr)
    {
        cout<<start<<endl;
    }
    return 0;
}

int TestString()
{
    string Test = "abcdef";
    cout<<Test[2]<<endl;
    cout<<(Test[5]==Test[2])<<endl;
    cout<<Test.size()<<endl;
    for(char i: Test) i='0';
    cout<<Test<<endl;
}

int sanmuTest()
{
    int a = 10, b = 1;
    int res = a>b?a:b;
    cout<<res<<endl;
    return 0;
}

int sizeofTest()
{
    int *ptr;
    double *ptrd;
    cout<<sizeof(*ptr)<<endl;
    cout<<sizeof(ptr)<<endl;
    cout<<sizeof(*ptrd)<<endl;
    vector<int>T1(10);
    vector<double>T2(10);
    cout<<sizeof(T1)<<' '<<sizeof(T1)<<endl;
//    cout<<*ptr<<endl;
    return 0;
}

int ErrorTest()
{
    int a = 0;
    try
    {
        if(!a) throw runtime_error("this is test");
    }
    catch(exception)
    {
        cout<<a<<endl;
    }
//    catch(runtime_error err)
//    {
//        cout<<err.what()<<' '<<a<<endl;
//    }
    return 0;
}

int TestPara(int a)
{
    cout<<a<<endl;
    return 0;
}

template <typename ScalarT>
void TestTemplate(ScalarT a)
{
    cout<<a<<endl;
}

template void TestTemplate(int a);

int main()
{
//    inout();
//    ByteTest();
//    TransOfDecimal();
//    const_test();
//    auto c = 1.0+1;
//    arrlis();
//    firstconfirm();
//    TestFor();
//    char ac[8] = "abc";
//    cout<<strlen(ac)<<endl;  //3
//    TestString();
//    sanmuTest();
//    sizeofTest();
//    ErrorTest();
//    int b;
//    TestPara(b);
//    map<string, size_t> test;
//    test["my_learn"]=0;
//    cout<<test["my_learn"]<<endl;
//    auto iter = test.begin();
//    iter->second = 1;
//    cout<<test["my_learn"]<<endl;
//    set<string> ::value_type sr;
//    sr = "0000";
//    cout<<sr<<endl;

//    set<int>Test={1,2,3,4,5};
//    cout<<*Test.lower_bound(3) <<endl;

//    int a = 0;
//    TestTemplate(a);
//    TestInitial mytest;
//    see(mytest);
//    cout.width(8)<<setprecision(3)<<10.0<<endl;
//    cout<<fixed<<setw(8)<<setprecision(3)<<10.0<<endl;
    int *p = new int [10]();
    cout<<*p<<endl;
    vector<string> a = {"a", "bcde"};
    TestAgorithm ta;
    ta.judge(a);

//    cout <<mytest.a<< endl;
//    cout <<mytest.b<< endl;
//    string s = "Hello World!";
//    string c = s.substr(0,6);
//    cout<<c<<endl;
    cout << "Hello World!" << endl;
    return 0;
    //this is a re new test
}

