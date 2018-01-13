#include<iostream>
#include<cstdlib>
#include<string>
 int countVowels(char* str)
 {
     int countVowels=0;
     for(int i=0;str[i]!='\0';i++)
     {
         if(str[i]=='a' || str[i]=='e' || str[i]=='i'|| str[i]=='o'|| str[i]=='u'|| str[i]=='A'|| str[i]=='E'|| str[i]=='I'|| str[i]=='O'|| str[i]=='U')
         {
            countVowels+=1;
         }
     }
     return countVowels;

 }
int getLength(char* str)
 {
     int length=0;
for(int i=0;str[i]!='\0';i++)
     {
         length+=1;
     }
     return length;
 }
 bool StringCompare(char* string1,char* string2)
 {
     int len1=getLength(string1);
     int len2=getLength(string2);
     int count=0;
     if(len1==len2)
     {
         for(int i=0;i<len1;i++)
         {
             if(string1[i]==string2[i])
             {
                 count+=1;
             }
             else
             {
                 return false;
             }
         }
         if(count==len1)
         {
             return true;
         }
     }
     else
     {
         return false;
     }

 }
 char* makeUpperCase(char* str)
 {
     int len=getLength(str);
     for(int i=0;i<len;i++)
     {
    if(str[i]>=97 && str[i]<=122)
	    {
		str[i]=str[i]-32;
	    }
     }
     return str;
 }
 char* makeLowerCase(char *str)
 {
     int len=getLength(str);
     for(int i=0;i<len;i++)
     {
        if(str[i]>=65 && str[i]<=90)
	    {
		str[i]=str[i]+32;
	    }
     }

return str;

 }
int countConsonants(char* str)
 {
     int vcount=countVowels(str);
     return (getLength(str)-vcount);
 }


 char* reverseString(char* str)
 {
int len=getLength(str);
char* revStr=new char[100];
int len2=getLength(revStr);
int countit=0;
 for(int i=len-1;i>=0;i--)
 {
     revStr[countit]=str[i];
     countit+=1;
 }
return revStr;
}

 bool checkPalindrome(char* str)
 {
int len=getLength(str);
int count=0,i,j;
for(i=0,j=len-1;i<=j;i++,j--)
{
    if(str[i]==str[j])
    {
        count+=1;
    }
}
if(count==len)
{
    return true;
}
else
{
    return false;
}
}
char* makeConcatenation(char* str,char* newStr)
{
    char* finStr;
    int len1=getLength(str);
    int len2=getLength(newStr);
    int newLen=len1+len2;
    finStr=new char[newLen];
    int count=0;
    for(int i=0;i<len1;i++)
    {
        finStr[i]=str[i];
    }
    for(int i=len1;i<newLen;i++)
    {
        finStr[i]=newStr[count];
        count+=1;
    }
    return finStr;
}

int main()
{
    char *revStr,*String,*newStr;
    int ch=0;
    int len=0;
    bool isString=false;
    String =new char[100];
    revStr=new char[100];
    std::cout<<"Enter the string";
    std::cin>>String;
    std::cout<<"______________STRINGENT______________"<<std::endl;
    std::cout<<"--------A String Manipulation Library-----"<<std::endl;
    std::cout<<"1. Count the Vowels"<<std::endl;
    std::cout<<"2. Get String Length "<<std::endl;
    std::cout<<"3. Get the reverse of the String"<<std::endl;
    std::cout<<"4. Check Palindrome"<<std::endl;
    std::cout<<"5. Count the consonants"<<std::endl;
    std::cout<<"6. Convert to UpperCase"<<std::endl;
    std::cout<<"7. Concatenate String "<<std::endl;
    std::cout<<"8. Compare tow strings"<<std::endl;
    std::cout<<"9. Convert to LowerCase"<<std::endl;
    std::cout<<"10. Exit"<<std::endl;
    std::cout<<"_____________________________________"<<std::endl;
    std::cout<<"Enter your choice"<<std::endl;
    std::cin>>ch;
    while(ch!=10)
    {
        switch(ch)
        {
        case 1:
            std::cout<<"The No Of Vowels is: "<<countVowels(String)<<std::endl;
            break;
        case 2:
            len=getLength(String);
            std::cout<<"The length is "<<len<<std::endl;
            break;
        case 3:
            std::cout<<reverseString(String)<<std::endl;
            break;
        case 4:
            isString=checkPalindrome(String);
            std::cout<<"The String is a Palindrome? 1. True 0. False "<<isString<<std::endl;
            break;
        case 5:
            std::cout<<"The No Of Consonants is: "<<countConsonants(String)<<std::endl;
            break;
        case 6:
            std::cout<<makeUpperCase(String);
            break;
        case 7:
            std::cout<<"Enter the string to be concatenated";
            std::cin>>newStr;
            String=makeConcatenation(String,newStr);
            std::cout<<"The concatenated string is"<<String<<std::endl;
            break;
        case 8:
            std::cout<<"Enter Another string for comparison";
            std::cin>>revStr;
            std::cout<<"The String are the same? 1. True 0. False "<<StringCompare(String,revStr)<<std::endl;
            break;
        case 9:
            std::cout<<makeLowerCase(String);
            break;
        case 10:
            exit(0);
            break;

        }
    std::cout<<"Enter your choice"<<std::endl;
    std::cin>>ch;
    }

    return 0;
}
