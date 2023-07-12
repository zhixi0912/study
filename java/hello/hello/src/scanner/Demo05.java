package scanner;
import java.util.Scanner;
public class Demo05 {
    /**
     * 输入多个数字，并求和与平均值，
     * 每输入一个数字用回车确认，
     * 通过输入非数字来结束输入并输出执行结果
     * @param args
     */
    public static void main(String[] args) {
        Scanner  scanner = new Scanner(System.in);
        double sum = 0;
        int m = 0;
        System.out.println("请输入数字：");
        while (scanner.hasNextDouble()) {
            double x = scanner.nextDouble();
            m++;
            sum = sum + x;
        }
        System.out.println("你总共输入了" + m + "次");
        System.out.println("你输入的数字总和为：" + sum);
        System.out.println("你输入的数字平均值为：" + sum/m);
        scanner.close();
    }
}
