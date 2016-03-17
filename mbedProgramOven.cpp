#include "mbed.h"
#include <stdio.h>
#include <stdlib.h>

using namespace std;

DigitalOut controlled(LED1);
DigitalOut strange(LED2);
DigitalIn control(p8);
AnalogIn myAI(p15);
AnalogOut myAO(p18);
Serial pc(USBTX, USBRX);
Timer debounce;

bool state = false;
bool prevstate = false;

int trimString(char* p,int maxInd)
{
    int count = 0;
    if (p == NULL) 
    {
        return -1;
    }
    char* s = p;
    for (int i = 0; i<maxInd; i++)
    {
        if (*p == '\n')
        {
            break;
        }
        p++;
        count++;
    }
    p = s;
    return count;
}


int main() {
    pc.printf("Hello\n");
    myAO.write(0.4/3.3);
    char buffer[256];
    strange = 1;
    wait(0.5);
    while(1)
    {
        pc.gets(buffer,256);
        int test = strcmp(buffer,"on\n");
        //pc.printf("Got %s, want %s, test compare %d\n",buffer,onBuf,test);
        //c = pc.getc();
        strange = 0;
        
        int n = trimString(buffer,256);
        char onBuf[n];
        for (int i = 0; i<n; i++)
        {
            onBuf[i] = buffer[i];
        }
            
        wait(0.5);
        if (strcmp(buffer,"on\n") == 0)
        {
            controlled = 1;
            strange = 0;
        }
        else if (strcmp(buffer,"off\n") == 0)
        {
            controlled = 0;
            strange = 0;
        }
        else 
        {
            float myfloat = atof(onBuf);
            myAO.write(myfloat);
        }
    }
/*    while(1) {
        wait(0.5);
        state = control;
        if (control){
            controlled = 1;
            float f = readAI();
            pc.printf("%f\n", f);
            prevstate = state;
        }
        else{
            controlled = 0;
            if (prevstate){
                pc.printf("EOF\n");
            }
            prevstate = state;
        }
    }*/
}

