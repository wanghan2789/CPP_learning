#include<bits/stdc++.h>
using namespace std;

int main()
{
    string deal;
    string order;
    //deal = "123456745689";
    //order = "idasdasdfeexxxufhioiedhadhhcoashifhaiofh";
    getline(cin, deal);
    getline(cin, order);
    auto current = deal.begin();
    bool normal_mode = true;
    for(int order_len = 0; order_len<order.length();++order_len)
    {
//        char deal_ch[70];
//        char order_ch[50];
        /*for(int de_t=0;de_t<deal.length();++de_t)
        {
            deal_ch[de_t] = deal[de_t];
        }
        for(int de_t=order_len;de_t<order.length();++de_t)
        {
            order_ch[de_t] = order[de_t];
        }*/
        char i = order[order_len];
        if(i == 'i' && normal_mode)
        {
            normal_mode = false;
            continue;
        }
        if(i == 'e' && !normal_mode)
        {
            normal_mode = true;
            continue;
        }
        if(normal_mode)
        {
            if(i == 'f')
            {
                if(order_len == order.length()-1)continue;
                i = order[++order_len];
                auto current_tmp = current;
                bool flag = true;
                ++current;
                if(current<deal.end()&&*current==i) flag = false;
                while(current<deal.end()&&*current!=i)
                {
                    ++current;
                    if(*current==i)
                    {
                        flag = false;
                        break;
                    }
                }
            if(flag)current = current_tmp;
            continue;
            }
            if(i == 'x')
            {
                current = deal.erase(current);
                current = min(current, deal.end()-1);
            }
            if(i == 'h')
            {
                --current;
                current = max(current, deal.begin());
            }
            if(i == 'l')
            {
                ++current;
                current = min(current, deal.end()-1);
            }
        }
        if(!normal_mode)
        {
            if(i!='e')
            {
//                string s;
//                s.push_back(i);
                current = deal.insert(current, order[order_len]);
                ++current;
            }
        }

    }
    cout<<deal<<endl;


    return 0;
}

