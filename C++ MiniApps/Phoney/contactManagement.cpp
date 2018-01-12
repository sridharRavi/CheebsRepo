#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cstdlib>
class ContactBook
{
private:
std::string m_name;
std::string m_number;
std::map<std::string,std::string> m_contact;
int m_size;
public:
    ContactBook(int size):m_size(size)
    {
    }
    void EnterValue(std::string name,std::string number)
    {
        m_contact.insert(make_pair(name,number));
    }
    std::string PrintValue(std::string name)
    {
        return m_contact[name];
    }
    std::map<std::string,std::string> getContactBook()
    {
        return m_contact;
    }
    void editContact(std::string name)
    {
        std::cout<<"Enter the new number";
        std::cin>>m_number;
        m_contact[name]=m_number;

    }
    void deleteContact(std::string name)
    {

        m_contact.erase(name);
        std::cout<<"This contact is deleted :"<<name<<std::endl;
    }

};
void printContactBook(ContactBook contact)
{
    std::map<std::string,std::string> cont;
    cont=contact.getContactBook();
    if(cont.empty())
    {
        std::cout<<"-----NO CONTACTS!-----"<<std::endl;

    }
    else
    {

    std::map<std::string,std::string>::const_iterator it;
    it=cont.begin();
    std::cout<<"____________CONTACTS_______________"<<std::endl;
    while(it!=cont.end())
    {
        std::cout<<it->first<<" : "<<it->second<<std::endl;
        ++it;
        std::cout<<"- - - - - - - - - - - - - - - - -"<<std::endl;
    }
    std::cout<<"____________________________________"<<std::endl;
    }
}
int main()
{
    std::string name,number;
    int len=0;
    int ch;
    std::cout<<"Enter the size of the Phone Book!";
    std::cin>>len;
    ContactBook contact(len);
    std::cout<<"_______________PHONEY____________"<<std::endl;
    std::cout<<" 1. Add Contact"<<std::endl;
    std::cout<<" 2. Print Phone Book"<<std::endl;
    std::cout<< " 3. Delete Contact"<<std::endl;
    std::cout<<" 4. Edit Contact"<<std::endl;
    std::cout<<" 5. Exit"<<std::endl;
    std::cout<<"__________________________________"<<std::endl;
    std::cout<<"Enter your choice"<<std::endl;
    std::cin>>ch;
    while(ch!=5)
    {
    switch(ch)
        {
    case 1:
        std::cout<<"Enter the name";
        std::cin>>name;
        std::cout<<"Enter the number";
        std::cin>>number;
        contact.EnterValue(name,number);
        break;
    case 2:
        printContactBook(contact);
        break;
    case 3:
        std::cout<<"Enter the contact to be deleted";
        std::cin>>name;
        contact.deleteContact(name);
        break;
    case 4:
        std::cout<<"Enter the contact to be edited";
        std::cin>>name;
        contact.editContact(name);
        break;
    case 5:
        std::cout<<"_____BYE______"<<std::endl;
        exit(0);
        break;
    }
        std::cout<<"Enter your choice"<<std::endl;
        std::cin>>ch;
    }

return 0;
}
