package selectionSort;

import java.util.Scanner;

public class selectionSort {

	public static void main(String[] args) {
		
		
		int pivot,temp;
			
			Scanner in=new Scanner(System.in);
					
			int[] array=new int[5];
			System.out.print("Enter number :" );
			for (int i=0;i<5;i++)
				array[i]=in.nextInt();
			for (int i=4; i>=0;i--)
			{
				pivot=0;
				for(int j=1;j<=i;j++)
				{
					if(array[j]>array[pivot])
					{
						pivot=j;
					}
					temp=array[pivot];
					array[pivot]=array[i];
					array[i]=temp;
				}
			}
			
			System.out.println("Selection Sort:");
	        for (int i=0;i<5;i++){
	        	System.out.println(array[i]);
	        }
				
	      	
			
			    	
		}
	}
	
