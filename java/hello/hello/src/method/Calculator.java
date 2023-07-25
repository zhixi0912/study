package method;
import java.util.Scanner;
public class Calculator {
    /**
     * 计算器功能，要求实现加减乘除功能，
     * 并且能够循环接收新的数据，通过用户交互实现
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(scanner);
//        recursion(scanner);
    }

    public static void recursion(int preams) {
        int number = 0;
        if (Character.isDigit(preams)) {
            System.out.println("数字");
        } else {
            System.out.println("非数字");
            if (preams == '+') {
                System.out.println("这是加号");
            }
        }

    }
}
