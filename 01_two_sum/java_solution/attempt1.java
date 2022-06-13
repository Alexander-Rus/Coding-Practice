import java.util.HashMap;
import java.util.Arrays;

class Solution{
	//we are returning an array of integers, we are taking in an array called numbers, and an integer target
	public static int[] twoSum(int[] numbers, int target) {
	    int[] result = new int[2];
	    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
	    for (int i = 0; i < numbers.length; i++) {
		if (map.containsKey(target - numbers[i])) {
		    result[1] = i;
		    result[0] = map.get(target - numbers[i]);
		    return result;
		}
		map.put(numbers[i], i);
	    }
	    return result;
	}
	
	public static int multiplyByTwo(int number) {
		return number * 2;
	}
	
	public static void main(String[] args) {
		int[] arr = new int[]{1,2,3,4,5};
		int[] result = twoSum(arr, 9);
		System.out.println(Arrays.toString(result));
	}
}

