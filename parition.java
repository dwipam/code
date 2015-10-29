package partition;

import java.util.Scanner;

public class parition {


	public void part(int[] array, int max_partition, int[] partition_blocks)
{
	
	
	int n=0;
	int v = 0;
	
	for (int i=0; i<max_partition;i++)
	{
		int temp_array[]= new int[partition_blocks[i]];
		/*if(i==max_partition-1){
			n=n-1;
		}
			else
			{*/
				for (int j=n;j<n+partition_blocks[i]; j++)
				{
					temp_array[j-n]=array[j];
									
						
				}
				
				v=v+IntraBlockDist(temp_array);
		//	}
		
			n=n+partition_blocks[i];
	}
	System.out.println("Intra Block for this partition: "+v);
}
	
	public int IntraBlockDist(int[] temp_array){
		if (temp_array.length==1)
			return 0;
		else
		{
		int calc=0;
		for (int i=0;i<temp_array.length-1;i++)
		{
			for (int j=i+1;j<temp_array.length;j++ )
			{
				calc=calc+distance(temp_array[i],temp_array[j]);
			}
		}
		
		
		return calc;
		
	}}
	public int distance(int i, int j)
	{		
		int l=0;
		l=Math.abs(i-j);
		return  l;
		}
	public static void main(String[] args) {

Scanner in=new Scanner(System.in);

		int[] array=new int[5];
		int[] partition_blocks=new int[3];
		System.out.print("Enter data elements :" );
		for (int i=0;i<5;i++)
			array[i]=in.nextInt();
		int max_partition = 3;
		
		System.out.print("Enter partition format :" );
		for (int i=0;i<3;i++)
			partition_blocks[i]=in.nextInt();
		
		parition p=new parition();
		p.part(array, max_partition, partition_blocks);
		
		
		
	}

}
