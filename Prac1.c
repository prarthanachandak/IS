void main()
{
    char str[]="Hello World";
    int i,len;
    len = strlen(str);
    for(i=0;i<len;i++){
        cout<<str[i]&127;
    }
    for(int i=0;i<len;i++){
        int original, modified;
        original = str[i];
        modified = str[i]^127;
        cout<<i<<original<<original<<modified);
 }
}
