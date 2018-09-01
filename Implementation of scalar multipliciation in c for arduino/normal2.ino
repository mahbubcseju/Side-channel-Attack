#include "BigNumber.h"

// function to display a big number and free it afterwards
void printBignum (BigNumber & n)
{
  char * s = n.toString ();
  Serial.print(s);
  free (s);
}  // end of printBignum


BigNumber BigMod( BigNumber base, BigNumber pwr, BigNumber mod){
	BigNumber ret = BigNumber(1);
	base = base%mod;
	while(pwr>BigNumber(0)){
		if(pwr%BigNumber(2)==1) ret = (ret * base)% mod;
		pwr = pwr/BigNumber(2);
		base = (base * base)% mod;
		ret%=mod;
	}
	return ret;
}
BigNumber mod;
void  multiply(BigNumber base,BigNumber pwr,BigNumber &ret)
{
       
	 ret = 0;
	base = base%mod;
        int cnt=0;
	while(pwr>0){
		//cnt++;
               // Serial.print(cnt);
              //  Serial.print("line no ");
                //printBignum(pwr);
                //Serial.println();
               // Serial.println("on 1");
                if(pwr%BigNumber(2)==1) {ret = (ret +base)% mod;
              if(ret>=mod)ret-=mod;  
            }
                //  Serial.println("on 1");
		pwr = pwr/BigNumber(2);
              //  Serial.println("on 2");
		 base = (base +base);
                 if(base>=mod)base-=mod;
              //   printBignum(base);
                //  Serial.println("");
                 // Serial.println("on 3");
                 
		ret%=mod;
	}
	

	
}
void addition(BigNumber *x1,BigNumber *y1, BigNumber *x2, BigNumber *y2,BigNumber &Ax, BigNumber &Ay){
	BigNumber m;
	if(*x1==0&&*y1==0){
            Ax = *x2;
            Ay = *y2;
            return;
	}
	else if(*x2==0&&*y2==0) {
            Ax = *x1;
            Ay = *y1;
            return;
        }
	else if(*x1==*x2 && *y1==((mod-*y2)%mod+mod)%mod){
            Ax = 0;
            Ay = 0;
          return ;
        }
	else {
		if(*x1==*x2&&*y1==*y2){
                      // Serial.println("Atkaichi ??");
			//m = ((*x1)*(*x1))%mod;
                         multiply(*x1,*x2,m);
                         
                       //Serial.println("Atkai naito ");
                       
                        // Serial.println("Atkaichi 1??");
                       multiply(m,BigNumber(3),m);
                       // Serial.println("Atkai naito 1");
			//m = (m*BigNumber(3));
			//m = (m + a)%mod;
                        Serial.println("Atkaichi 2??");
			multiply( m ,BigMod(((*y1)* BigNumber(2))%mod, mod-BigNumber(2),mod),m);
                        // Serial.println("Atkai naito 2");
			m%=mod;
			
		}
		else{
			m = ((*y2-(*y1))%mod+mod);
			m = (m *BigMod((((*x2)-(*x1))%mod+mod)%mod,mod-BigNumber(2),mod))%mod;
			m%=mod;
		}
		BigNumber xx1 = ((((m*m)%mod)-(*x1)-(*x2))%mod+mod)%mod;
		BigNumber xy1 = (((((m*((*x1)-(xx1))%mod+mod)%mod))%mod - (*y1))%mod+mod)%mod;
                Ax = xx1;
                Ay = xy1;
                return;
	}
return;
}
void scalarMultiplication(BigNumber px, BigNumber py, BigNumber ord){
        BigNumber Ax=BigNumber(0);
        BigNumber Ay=BigNumber(0);
  	while(ord>0){
    
            // Serial.print("first ...............1");
		if(ord%BigNumber(2)==1){
		  addition(&Ax,&Ay ,&px,&py,Ax,Ay);
		}
            // Serial.print("first ...............2");
	        ord/=BigNumber(2);
              //printBignum(px);
          
            //  printBignum(py);
            // Serial.print("first ...............3"); 
		addition(&px,&py,&px,&py,px,py);
             // printBignum(px);
             Serial.print("first ...............4");
      
             // printBignum(py);
	}
    printBignum(Ax);
    Serial.print(" ");
    printBignum(Ax);
}

BigNumber x,y;
int cnt = 0;
String inString =""; 

void setup ()
{
  Serial.begin (9600);
  Serial.println ();
  BigNumber::begin ();  // initialize library
//      Serial.print("Hello");
  

}  // end of setup

void loop () {
  
  while(Serial.available()>0){
    int inChar = Serial.read();
    if(isDigit(inChar)){
      inString += (char)inChar;
    }
    if(inChar == ' '){
      cnt++;
      if(cnt==1) x = BigNumber(inString.c_str());
      else if(cnt==2) y = BigNumber(inString.c_str());
      else mod = BigNumber(inString.c_str());
      inString = "";
    }
  //factorials
  if(cnt==3){
    printBignum(x);
    Serial.print(" ");
    printBignum(y);
    Serial.print(" ");
    printBignum(mod);
    Serial.println("");
    scalarMultiplication(x,y,BigNumber(4));
  }
 }
}

