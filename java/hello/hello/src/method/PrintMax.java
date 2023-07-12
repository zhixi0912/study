package method;

public class PrintMax {
    public static void main(String[] args) {
        printMax(32,2,3,11,44,55.5);
        printMax(new double[]{1,2,3,4,5});
    }
    // 求最大值
    public static void printMax(double... numbers) {
        if(numbers.length == 0) {
            System.out.println("No argument passed");
            return;
        }

        double result = numbers[0];
        // 排序
        for (int i = 1; i <numbers.length; i++) {
            if (numbers[i] > result) {
                result = numbers[i];
            }
        }
        System.out.println("The max value is" + result);
    }
}
