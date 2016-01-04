import java.util.Scanner;

public class HeapSort {
	private static int N;

	public static void sort(int array[]) {
		max_heapify(array);
		for (int i = N; i > 0; i--) {
			swap(array, 0, i);
			N = N - 1;
			maxheap(array, 0);
		}
	}

	public static void max_heapify(int array[]) {
		N = array.length - 1;
		for (int i = N / 2; i > 0; i--) {

			// if ((2*i)>N)
			// i=0;
			maxheap(array, i);
		}
	}

	public static void maxheap(int arr[], int i) {
		int left = 2 * i;
		int right = 2 * i + 1;
		int max = i;
		if (left <= N && arr[left] > arr[i])
			max = left;
		if (right <= N && arr[right] > arr[max])
			max = right;

		if (max != i) {
			swap(arr, i, max);
			
			maxheap(arr, max);
			/*
			 * for (int j=0;j<arr.length;j++){ System.out.print(arr[j]); }
			 * maxheap(arr, max);
			 */
		}
		for (int j = 0; j < arr.length; j++) {
			System.out.print(arr[j] + "\n");
		}
	}

	public static void swap(int array[], int i, int j) {
		int temp = array[i];
		array[i] = array[j];
		array[j] = temp;
		System.out.print(" Sorted Element: " + array[j] + " " + array[i] + " ");

	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n, i;

		System.out.println("Enter array size");
		n = scan.nextInt();

		int array[] = new int[n];

		System.out.println("\nEnter numbers");
		for (i = 0; i < n; i++)
			array[i] = scan.nextInt();

		sort(array);

		System.out.println("\nElements after sorting ");
		for (i = 0; i < n; i++) {
			System.out.print(array[i] + " ");
		}

	}
}