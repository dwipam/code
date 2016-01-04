package mergerSort;

import java.util.Scanner;

public class mergerSort {
	private int[] temparray;
	

	public static void main(String a[]){
        
		Scanner in=new Scanner(System.in);
		int[] array=new int[5];
		
		
		
		System.out.print("Enter number :" );
		for (int i=0;i<5;i++)
			array[i]=in.nextInt();
        mergerSort mms = new mergerSort();
        mms.sort(array);
        System.out.println("Merge Sort:");
        for (int i=0;i<5;i++){
        	while(array[i]==0)
        		i++;
        	System.out.println(array[i]);
        }
			
        }
    
     
    public void sort(int array[]) {
    	this.temparray=new int[5];
        exeMergeSort(0, 4, array);
        
    }
 
    public void exeMergeSort(int lowerIndex, int higherIndex, int array[]) {
         
        if (lowerIndex < higherIndex) {
            int middle = lowerIndex + (higherIndex - lowerIndex) / 2;
            exeMergeSort(lowerIndex, middle, array);
            exeMergeSort(middle + 1, higherIndex, array);
            mergeParts(lowerIndex, middle, higherIndex, array);
        }
    }
 
    public void mergeParts(int lowerIndex, int middle, int higherIndex, int array[]) {
 
        for (int i = lowerIndex; i <= higherIndex; i++) {
        	temparray[i] = array[i];
        }
        int c1, c2;
        int i = lowerIndex;
        int j = middle + 1;
        int k = lowerIndex;
        while (i <= middle && j <= higherIndex) {
            if (temparray[i] < temparray[j])
            {
            	   if(temparray[i] == temparray[j] )
            	   {
            		  
            		   c1=temparray[j+1];            		   
            	   temparray[j+1] = temparray[i];
                    temparray[i]=c1;
            	
            } 
            	   array[k] = temparray[i];
                   i++;
            	   
            	   }
            else 
            {
            	/*if(temparray[i] == temparray[j] )
         	   {
         		  
         		   c1=temparray[i+1];            		   
         	   temparray[i+1] = temparray[j];
                 temparray[j]=c1;
         	
         } */

            	array[k] = temparray[j];
                j++;
            	}
             k++;
            
        }
        while (i <= middle) {
            array[k] = temparray[i];
            k++;
            i++;
        }
 
    }

}
