import java.util.Scanner;
 
 class FLOW016
 {  
 	public static void main(String [] args)
	{
		Scanner input = new Scanner(System.in);
		int a,t,b,hcf,lcm; 
		t = input.nextInt();
	      while(t!=0)
		 	{  
			  a=input.nextInt();
			  b=input.nextInt();
				hcf=gcd(a,b);
                lcm=(a*b)/hcf;
                System.out.println(hcf+" "+lcm);			
			  t-=1;
		    }
		
				
	}
    public static int gcd(int a,int b)
	{   if(b>a)
		{a=a+b;
	     b=a-b;
		 a=a-b;
		}
	    while(b!=0)
		 {
		   int temp;
		   temp=b;
		   b=a%b;
		   a=temp;
		 }
		 return a;
	}
	

} 