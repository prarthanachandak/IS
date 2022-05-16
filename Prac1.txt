#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

int main()
{
	
	char str[]="Hello World";
	char str1[11];
	char str2[11];
	int i, len;
	len = strlen(str);
	cout<<"AND OPERATION"<<endl;
	for(i=0; i<len; i++)
	{
		str1[i] = str[i] & 127;
		cout<<str1[i]<<" ";
	}
	cout<<endl;
	cout<<"XOR OPERATION"<<endl;
	for(i=0; i<len; i++)
	{
		str2[i] = str[i] ^ 127;
		cout<<str2[i]<<" ";
	}
	cout<<endl;
	getch();
}

/* OUTPUT

AND OPERATION
H e l l o   W o r l d
XOR OPERATION
 ? ?  ? ? _ ( ?
 
*/
 
 
